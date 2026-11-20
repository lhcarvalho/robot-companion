#!/usr/bin/env python3
"""Ensure each versioned OpenSCAD source has a valid PNG, STL and GLB."""
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
CAD=ROOT/"mechanics"/"cad"
OUT=ROOT/"mechanics"/"exports"

def check():
    errors=[]
    scads=sorted(CAD.glob("*.scad"))
    if not scads:
        errors.append("no SCAD sources")
    for src in scads:
        if not re.search(r"_v[0-9]{2,}\.scad$",src.name):
            errors.append(f"not versioned: {src}")
        for ext in [".png",".stl",".glb"]:
            path=OUT/(src.stem+ext)
            if not path.exists():
                errors.append(f"missing {path.relative_to(ROOT)}")
                continue
            if path.stat().st_size < 32:
                errors.append(f"empty {path.relative_to(ROOT)}")
                continue
            with path.open("rb") as f: header=f.read(16)
            if ext==".png" and not header.startswith(b"\x89PNG\r\n\x1a\n"):
                errors.append(f"bad PNG header: {path}")
            if ext==".glb" and not header.startswith(b"glTF"):
                errors.append(f"bad GLB header: {path}")
            if ext==".stl" and path.stat().st_size<84:
                errors.append(f"invalid STL size: {path}")
    for item in errors:
        print("ERROR:",item)
    print(f"CAD sources: {len(scads)} | Errors: {len(errors)}")
    return int(bool(errors))

if __name__=="__main__":
    sys.exit(check())
