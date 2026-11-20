#!/usr/bin/env python3
"""Generate PNG, STL and GLB for versioned OpenSCAD sources.

Examples:
  python scripts/render_cad_assets.py
  python scripts/render_cad_assets.py mechanics/cad/head_layout_v01.scad

Exports are placed in mechanics/exports/<stem>.(png|stl|glb).
Never overwrites historical generated files unless --force is explicitly given.
"""
import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CAD_DIR = ROOT / "mechanics" / "cad"
EXPORT_DIR = ROOT / "mechanics" / "exports"

def run(*cmd):
    print("+", " ".join(map(str,cmd)), flush=True)
    subprocess.run(cmd, check=True)

def export_file(src, force=False):
    if src.suffix.lower() != ".scad":
        raise ValueError("Only .scad sources are supported")
    EXPORT_DIR.mkdir(parents=True,exist_ok=True)
    paths={s:EXPORT_DIR/(src.stem+s) for s in (".png",".stl",".glb")}
    if not force and all(p.is_file() for p in paths.values()):
        print(f"SKIP {src.name}: complete assets already exist")
        return
    missing={s for s,p in paths.items() if force or not p.is_file()}
    if ".png" in missing:
        run("xvfb-run","-a","openscad","-o",str(paths[".png"]),
            "--viewall","--autocenter","--imgsize=1200,900",str(src))
    if ".stl" in missing or ".glb" in missing:
        run("openscad","-o",str(paths[".stl"]),str(src))
    if ".glb" in missing:
        import trimesh
        mesh=trimesh.load(paths[".stl"],force="mesh")
        if mesh.is_empty:
            raise RuntimeError(f"Empty geometry: {src.name}")
        mesh.export(paths[".glb"])
    for suffix,path in paths.items():
        if not path.is_file() or path.stat().st_size < 32:
            raise RuntimeError(f"Empty or missing export: {path}")
    print("OK",src.name,"=>",*[p.name for p in paths.values()],flush=True)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources",nargs="*",type=Path,help="Optional explicit SCAD paths")
    parser.add_argument("--force",action="store_true",help="Regenerate existing exports (use only when authorized)")
    args=parser.parse_args()
    sources=args.sources or sorted(CAD_DIR.glob("*.scad"))
    if not sources:
        parser.error("No SCAD files found")
    for src in sources:
        export_file(src.resolve(),force=args.force)

if __name__=="__main__":
    main()
