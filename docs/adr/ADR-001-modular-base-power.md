# ADR-001 — Power lives in interchangeable bases

**Date:** 2026-11-21  
**Status:** ACCEPTED (system architecture); electrical and connector details NOT YET VERIFIED.

## Decision
Robot Companion will have a **reusable electronics-and-head core** (rounded-square head with LCD, OV5647 camera, neck mechanism, P4+C6 processor, audio and core firmware). **No traction/main energy battery belongs in the reusable core**. Power storage, external input/charging implementation and eventual wheel drive belong to the **interchangeable base**. The core shall be usable on the workbench from an external regulated supply through the same conceptual power interface.

The words "same head" in the product discussion refer to reusing the head **and its electronics/control assembly**, not necessarily fitting the entire Waveshare P4 dev board inside the articulated head. Current CAD keeps the P4 in the stationary torso; changing this needs its own mechanical ADR and cable analysis.

## Target base variants
1. **Bench prototype:** external regulated power via a test adapter/stand; no battery.
2. **Desktop base:** replaceable battery or stationary powered dock; optional power-path charger for seamless operation if engineered and validated.
3. **Mobile base:** protected battery, power distribution, motor driver, wheels, encoders, obstacle/cliff/bumper safety and optional charge dock.
4. **Future variants:** larger-energy base, stationary charging display stand, experimental locomotive form factor.

The core should discover/declare the attached base's capabilities; NEVER blindly execute drive commands. Any high-current motor control and safety interlock must remain deterministic; no external AI/cloud dependency.

## Base-to-core requirements (NOT final connector pinout)
- Regulated core power plus reference ground with **defined maximum current**, thermal protection, reverse-polarity and short-circuit protection.
- Additional independently protected servo/motor rail(s) if appropriate after measurement; **never** drive servos from the P4 3.3 V rail.
- Base presence/type detection and optional telemetry (battery state, temperature, charger/external power).
- Optional low-voltage control/data bus for wheel controller and base-specific sensors.
- Safe mechanical retention, keying against wrong orientation, connector rated for repeated mating; no exposed energized contacts.
- Defined hot-swap policy: initial prototype **power-off-only swap**. Seamless live swapping is a future feature, not currently promised.
- On disconnect, brownout, invalid base or sensor fault: actuators go to safe state.
- Charger/BMS must match exact chemistry and configuration, with dedicated power-path/load-sharing if charging while operating is required.
- A common 5 V power rail is a *candidate interface*, not an approved specification until P4+audio+camera+LCD+servo consumption and cable drops are measured.

## Alternatives considered
- Battery permanently installed in head/core: rejected for now; extra mass, thermal load, volume, less modularity.
- Power bank inside core: rejected as baseline; bulky and awkward service.
- Different battery types per base: allowed if each provides electrically compatible **regulated interface** to the core.

## Consequences
- Desk core should be designed around electrical and mechanical mating planes, not around a battery compartment.
- Battery allocation and center of gravity become base-specific; mobile power sized later for motors and traction.
- Prototype can begin with a supply and breakout interposer before battery hardware purchase.
- Existing concept shell/neck SCAD V01/V02 **remain historical studies**; no old revision is deleted or relabeled as approved.

## Validation gates
1. Measure peak/idle current for P4+C6, OV5647, LCD, speaker and servos separately.
2. Verify exact P4 power input, boot/undervoltage and reverse polarity risks.
3. Select a base connector with complete datasheet, pin assignment, current, insertion lifetime, protection and cable pullout measures.
4. Define low-voltage data bus and ability to identify base type safely.
5. Create CAD interface drawing and powered/unpowered test fixture, then mate/demate stress tests.
6. Select battery chemistry and charger/BMS **per base**; calculate real autonomy with measured load.
7. Update BOM only for selected parts, document test evidence and create new source CAD revision with matching PNG/STL/GLB.

See [BASE_INTERFACE_V01](../../electronics/BASE_INTERFACE_V01.md).
