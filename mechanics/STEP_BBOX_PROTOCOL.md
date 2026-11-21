# P4 board STEP bounding-box extraction — Issue #5

The Waveshare manufacturer package was successfully retrieved on GitHub Actions, containing a STEP file (~29.9 MB) and accompanying DXF/PDF. SHA-256 recorded in the [vendor CAD audit workflow](https://github.com/lhcarvalho/robot-companion/actions/workflows/vendor-cad-audit.yml); source [Waveshare resources](https://docs.waveshare.com/ESP32-P4-Module-DEV-KIT/Resources-And-Documents).

## Automated next measurement
`mechanics/tools/analyze_waveshare_step.py` parses the official STEP with OpenCascade/CadQuery and produces axis-aligned extents and hash, using Python 3.11 and CadQuery 2.6.1 in GitHub Actions. It does not commit or redistribute the vendor STEP itself.

### What the result means
- A bounding box is the minimum axis-aligned envelope of the entire model in **the source STEP coordinate frame**. It may include ports and protrusions, not just PCB.
- Axes are **not** necessarily the same as our head/torso sketch conventions.
- It is **not** a validated mount or physical fit. Need pin1, manufacturer revision, mounting-hole centers, board thickness, connector service clearance, cable bend and physical measurements.

### Next mechanical task after STEP dimensions
Orient STEP relative to actual torso, position mounting holes and USB/Ethernet service openings, run collision test against new parametric shell; publish a **new CAD V02** plus PNG/STL/GLB, preserving V01. After that, design CSI moving cable solution and 2-axis neck.

The prior 95×70×18-mm motherboard size in desk CAD is an **unverified proxy** and MUST NOT be treated as measured dimensions.
