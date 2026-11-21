# Manufacturer CAD provenance — Issue #5

## Objective
Acquire exact manufacturer STEP + drawing package for the **Waveshare ESP32-P4-Module-DEV-KIT** before claiming fit of the development board and its connectors inside the 125-mm provisional body.

Original Waveshare resources: https://docs.waveshare.com/ESP32-P4-Module-DEV-KIT/Resources-And-Documents

Manufacturer package linked from page: 
`https://files.waveshare.com/wiki/ESP32-P4-Module-DEV-KIT/ESP32-P4-Module-DEV-KIT-20250427.zip`

### Reproducible retrieval
Run `python3 mechanics/tools/fetch_waveshare_step.py`. The script downloads, CRC-checks, SHA-256 hashes and inventories the vendor archive. GitHub Actions performs this check on a relevant branch and publishes **metadata only**. No manufacturer binaries are automatically copied into this public repo.

### Engineering gate (still not complete)
1. Confirm exact board model/revision and ensure downloaded CAD matches the purchased board.
2. Validate STEP/other model against maker dimensioned views and actual connector, screw hole and cable retention locations.
3. Import as an assembly into FreeCAD, orient axes consistently with current OpenSCAD drafts.
4. Measure actual PCB mounting holes, protrusions, USB/Ethernet service clearance and routed cable envelopes.
5. Record measurements in an annotated drawing with model/version/hash.
6. Replace arbitrary 95×70×18-mm board proxy with verified geometry in **new** `_v02.scad` revision and auto-generate PNG/STL/GLB.
7. Check camera CSI FFC motion-cycle fatigue separately. STEP does not prove safe flexible cabling.

**A successful download is evidence of artifact availability, NOT proof of physical fit.**
