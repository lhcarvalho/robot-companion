# Head mechanical layout — V0.1

**Status: feasibility mockup only. NOT ready for printing or assembly.**

## Approved decisions
- Robot nominal height: 150 mm (target range 120–180 mm).
- Head shape: rounded rectangle.
- Nominal head envelope: **105 W × 85 H × 60 D mm**.
- Display: Waveshare **2.4inch LCD Module**, ILI9341, SKU 18366, SPI.
- Camera: Waveshare **RPi Camera (B)**, OV5647, included with the P4-A kit.

## Sources and verified envelopes
- LCD PCB: **70.5 × 43.3 mm**; active display: **48.96 × 36.72 mm** in landscape.
  https://www.waveshare.com/product/displays/lcd-oled/2.4inch-lcd-module.htm
- Camera PCB: **32 × 32 mm**; vendor selection guide states 43° diagonal field of view. Another vendor wiki lists different optical data; verify specific physical revision before buying.
  https://www.waveshare.com/product/rpi-camera-b.htm
  https://www.waveshare.com/wiki/RPi_Camera_%28B%29
- P4-A includes RPi Camera (B) and 15-pin CSI cable.
  https://www.waveshare.com/product/mcu-tools/development-boards/esp32-p4-module-dev-kit.htm

## Coordinate convention and model assumptions
X = head width; Y = head height; Z = head depth (positive toward face).
- LCD PCB center: (0,-15,+23) mm.
- Camera PCB center: (0,+22,+10) mm.
- Shell wall = 2.4 mm, corner radius = 14 mm.
- **PCB thickness (1.6 mm), active-area placement (PCB-centered), camera lens diameter (14 mm), and lens projection (19 mm) are stand-ins**, NOT measured vendor dimensions.
- The lens opening is temporarily 16 mm. The real lens may require a different hole or bracket.
- A lower keepout volume shows a *potential* cable/neck zone, not a finished mechanism.

## Preliminary fit calculation
- LCD nominal top edge: -15 + (43.3/2) = **+6.65 mm**.
- Camera nominal bottom edge: +22 - (32/2) = **+6.0 mm**.
- Result: **0.65 mm vertical overlap in projection**; the PCBs are in *different Z planes* and thus do not overlap physically in this proxy.
- Camera top edge = +38 mm; shell inside top is +40.1 mm. Nominal gap is only **2.1 mm**, before fasteners, connector and tolerance requirements. This is **not a validated installation**.
- The model includes no actual FFC connector dimensions or cable routing. Camera FFC passing through a moving neck is a high-priority feasibility risk.

## Validation gates
- [ ] Confirm camera PCB lens center, lens barrel height, optical clearance and mounting hole locations with real drawing or measurement.
- [ ] Confirm LCD board active area offset, actual glass / PCB stack height, connector placement, mounting points and backlight circuitry.
- [ ] Import verified STEP models (or dimensioned vendor drawings) for the exact parts.
- [ ] Test camera/display electrical co-existence on the chosen P4 board.
- [ ] Design pan/tilt neck; validate permissible cable radius, cyclic flex and strain relief.
- [ ] Add speaker, microphone acoustic route, service access, assembly screws/inserts and print clearances.
- [ ] Check collision and mass/servo torque with full assembly.
- [ ] Produce a proper split shell with retention features and test-print before declaring printable design.

## Generate models
```bash
openscad -o head_layout_v01.stl -D 'show_components=false' -D 'show_clearance=false' head_layout_v01.scad
xvfb-run -a openscad -o head_layout_v01.png --viewall --autocenter --imgsize=1000,750 --camera=0,0,0,15,0,20,300 -D 'show_clearance=false' head_layout_v01.scad
```
The resulting STL is a **placeholder volume-only shell**. Do not send it to manufacturing expecting working mounting and wiring.
