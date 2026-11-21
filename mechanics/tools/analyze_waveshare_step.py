#!/usr/bin/env python3
"""Compute manufacturer STEP assembly bounding box with OpenCascade (CadQuery).

NOT a mechanical fit guarantee; orientation, mounting, cables, and board revision
must still be checked. Only logs dimensions and file provenance, no CAD redistribution.
"""
from pathlib import Path
import json
import zipfile
import hashlib
import tempfile
import sys

try:
    import cadquery as cq
except ImportError as e:
    raise SystemExit("Install cadquery==2.6.1 on supported Python 3.11: "+str(e))
archive=Path(sys.argv[1] if len(sys.argv)>1 else "mechanics/vendor_audit/waveshare_p4_20250427.zip")
out=Path(sys.argv[2] if len(sys.argv)>2 else "mechanics/vendor_audit/bbox.json")
if not archive.is_file(): raise SystemExit(f"Missing archive: {archive}")
with zipfile.ZipFile(archive) as z:
    steps=[p for p in z.namelist() if p.lower().endswith((".stp",".step"))]
    if len(steps)!=1: raise SystemExit(f"Expected exactly one STEP; found {steps}")
    with tempfile.TemporaryDirectory() as d:
        # Never extract arbitrary paths; read exact member and write basename only.
        cad=Path(d)/Path(steps[0]).name
        cad.write_bytes(z.read(steps[0]))
        wp=cq.importers.importStep(str(cad))
        shapes=list(wp.objects)
        if not shapes: raise SystemExit("STEP produced no shapes")
        compound=cq.Compound.makeCompound(shapes)
        bb=compound.BoundingBox()
        data={"source_archive_sha256":hashlib.sha256(archive.read_bytes()).hexdigest(),
              "step_member":steps[0],
              "step_bytes":cad.stat().st_size,
              "shape_count":len(shapes),
              "absolute_bounds_mm":{
                "xmin":bb.xmin,"xmax":bb.xmax,"ymin":bb.ymin,
                "ymax":bb.ymax,"zmin":bb.zmin,"zmax":bb.zmax},
              "axis_extent_mm":{"x":bb.xlen,"y":bb.ylen,"z":bb.zlen},
              "warning":"Unoriented whole STEP assembly bounds, NOT PCB outline or enclosure clearance"}
        out.parent.mkdir(parents=True,exist_ok=True)
        out.write_text(json.dumps(data,indent=2)+"\n")
        print(json.dumps(data,indent=2))
