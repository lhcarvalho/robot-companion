# Open questions, blockers and risks

Every item should be resolved with **evidence**, an issue/PR link and an updated status. No guessed numbers.

| ID | Priority | Question / missing evidence | Blocking |
|---|---|---|---|
| Q-001 | CRITICAL | Manufacturer STEP obtained and outer bounding extents measured (88.359×57.091×20.100mm); actual PCB revision, connector/mount-hole coordinates and local fit still unknown? | Final torso CAD, purchase |
| Q-002 | CRITICAL | Can OV5647 15-pin CSI FFC and LCD harness safely survive repeated pan/tilt movement? Cable length/radius/strain relief/cycle life? | Moving head |
| Q-003 | HIGH | LCD actual board mounting hole pattern, active-area offsets, connector/backlight load? | Front face printing |
| Q-004 | HIGH | OV5647 lens mechanical center, protrusion, connector orientation and usable field of view? | Camera/window geometry |
| Q-005 | HIGH | P6 schematic contacts transcribed in PR #21; which candidate SPI/servo GPIOs are conflict-free on the physical board revision and what is actual pin-1 orientation? | Schematic/firmware |
| Q-006 | HIGH | 5V supply current with servo startup/stall + screen/audio peak; appropriate regulators and protection? | Safe power |
| Q-007 | HIGH | Actual complete moving head mass, CG and torque/tilt margin, desk tip stability? | Final servo/neck selection |
| Q-008 | HIGH | Kit A includes 8Ω/2W speaker; what are the included unit's manufacturer part, dimensions, mate connector and acoustic/microphone route? | Torso enclosure |
| Q-009 | MED | Face-display actual visible window is ~49×37 mm: does it meet aesthetic goal? | Cosmetic approval |
| Q-010 | MED | Can P4 use CSI capture, SPI animations, audio, Wi-Fi concurrently at useful rate? | Performance acceptance |
| Q-011 | HIGH | What local face recognition flow works robustly in household lighting and protects children's biometric templates? | Offline behavior |
| Q-012 | HIGH | What mechanical/electrical connector will let desk and future wheel base swap safely? | Mobile modularity |
| Q-013 | MED | What exact materials/print tolerances, screws/inserts, printer/outsourced manufacturing constraints? | Printable production |
| Q-014 | MED | How to route microphone port and accessible mute switch/button? | Audio/privacy |

## Known engineering hazards
- Power servo from protected regulated rail, **never** logic 3.3V; common reference ground, noise management.
- Physical stops and movement safety must work without LLM or network.
- No cyclic cable reliability proof; standard FFC is not automatically flex-rated.
- Never assume GPIO reservation conflicts have been cleared.
- Reject cosmetic mockup as mechanical qualification.
- Mobile version needs cliff/bumper sensors, speed limits and supervised use around children.

## Evidence expectation
Vendor mechanical drawing/STEP, firmware and logs from hardware tests, photographs with actual measuring scale, electrical schematic or calculations. Label all inferred or estimated information. Close each issue only when the specific criterion is met.
