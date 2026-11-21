#!/usr/bin/env python3
"""Download the *manufacturer* mechanical CAD ZIP and create a provenance manifest.

Run in CI. No vendor STEP binaries committed to Git by default, as
redistribution/license and model precision must be checked.
"""
import hashlib
import json
import os
from pathlib import Path
import urllib.request
import zipfile

URL="https://files.waveshare.com/wiki/ESP32-P4-Module-DEV-KIT/ESP32-P4-Module-DEV-KIT-20250427.zip"
OUT=Path(os.getenv("CAD_AUDIT_OUT","mechanics/vendor_audit"))
OUT.mkdir(parents=True,exist_ok=True)
zip_path=OUT/"waveshare_p4_20250427.zip"
req=urllib.request.Request(URL,headers={"User-Agent":"robot-companion-engineering/0.1"})
with urllib.request.urlopen(req,timeout=60) as response:
    zip_path.write_bytes(response.read())
data=zip_path.read_bytes()
manifest={"source":URL,"sha256":hashlib.sha256(data).hexdigest(),
          "size_bytes":len(data),"files":[]}
with zipfile.ZipFile(zip_path) as archive:
    bad=archive.testzip()
    if bad: raise RuntimeError("Vendor archive CRC error: "+bad)
    for item in archive.infolist():
        manifest["files"].append({"path":item.filename,
              "bytes":item.file_size,
              "is_step":item.filename.lower().endswith((".step",".stp")),
              "is_drawing":item.filename.lower().endswith((".dxf",".dwg",".pdf"))})
manifest["step_count"]=sum(f["is_step"] for f in manifest["files"])
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
print(json.dumps(manifest,indent=2))
if not manifest["step_count"]:
    print("WARNING: ZIP has no .step/.stp; inspect associated CAD or drawings manually")
