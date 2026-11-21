# Modular base coupling concept V01 — mechanical + electrical

**Date:** 2026-11-21 | **Maturity:** CANDIDATE CONCEPT, NO PHYSICAL VALIDATION | **Decision source:** [ADR-001](../docs/adr/ADR-001-modular-base-power.md).

## Summary / proposed direction

1. **MVP: slide-on mechanical cradle + manual internal keyed/latching cable connector.** Mechanical load goes through frame/rails/stops, **not electrical connectors**. Switch power off to change bases. The short protected cable can be disconnected in an accessible service opening.
2. **Later: self-mating, high-cycle base docking connector** (e.g., protected pogo/spring contacts or industrial blind-mate) only after durability, current, short-circuit and accessibility tests. Do not substitute a 30-cycle wire harness connector as a frequent-change dock.
3. Standardize **functions and mechanical datum**, not a premature 5 V pinout or battery chemistry. Different bases may use different battery systems provided regulated output matches the approved interface.

## Alternatives reviewed

| Approach | Benefits | Main liabilities | Verdict |
|---|---|---|---|
| Rail/slide with positive latch + manual cable plug | Low-cost, simple printing/tolerances, no forced electrical blind mating, feasible for bench supply | Less elegant; hand access needed; plug life limited | **MVP candidate** |
| Blind-mate guided multipin connector | Single insertion; repeatable geometry if engineered correctly | Requires alignment tolerance stack, costly mating parts, high-cycle data and safe energized contact design | **Later candidate** |
| Pogo/spring contacts plus magnets/alignment | Quick user base changes, potentially high cycle count | Exposed contacts, debris, contact-resistance heating, servo surges, accidental shorting, magnetic retention not sufficient for tip loads | **Not MVP** |
| Magnet-only electrical coupling | Easy conceptual attachment | No positive tensile retention, contact and safety risks | **Reject** |

### Relevant real connector family for **manual MVP harness only**
- Molex **Micro-Fit 3.0** series 43025 receptacle and 43020 mating plug is polarized, latched, 3.0 mm pitch, 2–24 circuits in this family. The manufacturer quotes **typical mechanical durability 30 cycles** for the family; maximum current depends on terminal/wire gauge/circuit count/thermal derating, NOT an unconditional 10.5 A per pin.
- Consequently **it is not approved for frequent consumer base swapping**. Consider for accessible development harness with limited disconnects only. Exact 12-position housing, contact, compatible mate, tool and current derating must be checked before ordering.
- Manufacturer: https://www.molex.com/en-us/products/part-detail/430251200 and https://www.molex.com/content/dam/molex/molex-dot-com/en_us/pdf/datasheets/987650-5984.pdf?inline=
- No approved connector BOM yet; this is a researched **component candidate**, not a selection.

## Mechanical concept — explicit provisional geometry

See [SVG concept](../docs/diagrams/base-coupling-concept-v01.svg). Illustration is a **2D conceptual diagram, NOT to scale**, not a dimensioned CAD file.

- A rigid **core-side lower interface plate** on the fixed torso, opposite the articulated head and away from CSI/LCD cables.
- A **base-side recessed slide cradle**, mechanically keyed asymmetrically to prevent 180° reversed insertion.
- Two lateral guiding rails, end-stop in insertion direction, **positive latch** with deliberate release actuation. Add safety strap/captive screws in early prototypes if printed latch properties untested.
- Base retains center of gravity and tip stability; account for worst-case head tilt and servo loads.
- Cable passes through a **protected service opening** with strain relief; leave finger access to unplug without pulling wires.
- Keep any electrical terminals recessed in the base; no accessible live conductors.
- Avoid fastening into or relying on Waveshare P4 PCB mounting holes as the primary structural load path.
- **Do not freeze rail spacing, rail thickness, screw positions or clearance now.** Measure actual torso geometry, moving-head clearance, structural load and 3D-print material/tolerance first.
- Preliminary packaging goal: coupling should fit within the nominal 125×100 mm torso footprint, but this is unverified; it should not increase the nominal 150 mm overall height without explicit trade-off review.

## Electrical interface / harness domains (FUNCTIONAL, NO PIN NUMBERS)

| Domain | Direction | Required behavior |
|---|---|---|
| CORE_PWR / CORE_GND | base to core | Protected, regulated power suitable for P4+display+camera+audio peak load; 5 V is provisional |
| SERVO_PWR / SERVO_GND | base to core (if servos live in core) | Independently current-limited and filtered from logic; size for startup/stall; never from 3.3 V P4 |
| BASE_PRESENT / BASE_ID | base to core | Unknown/open/invalid base forces stationary safe idle |
| BASE_DATA | bidirectional optional | Future low-voltage protocol, base telemetry and requests; voltage-level/ESD isolation pending |
| BATT/CHG telemetry | base to core logical | Battery percentage/health/charger state; base never sends raw unregulated cell voltage to core without appropriate conditioning |

**No pinout, rail maximum current, 5 V electrical wiring, ground routing or voltage-level converter is approved.** Do not assume MCU USB-C can be back-powered at the same time from base input: power-source ORing/isolation is a separate test/feature. Default on prototypes is use one power source at a time.

Mobile base wheel motors and their drivers draw power **within the base** directly from a protected motor power subsystem, not through the shared core electrical connector. Mobile commands are mediated by a deterministic controller with local emergency stop behavior.

## Prototype sequence / acceptance gates

| Stage | Deliverable | Gate |
|---|---|---|
| P0 | Test P4 kit and display/camera with board's manufacturer-supported USB supply | Measured idle/peak current; stable boot; never power servos off MCU 3.3 V |
| P1 | Develop bench fixture, current-limited regulated supply, protected servo feed, accessible harness | Measured servo start/stall transients, brownout behavior and common ground |
| P2 | Print disposable rail/latch coupon using measured core envelope | Stable latch, no wobble, no collision, no live terminals exposed |
| P3 | Define connector family and routed harness from full electrical loads | Datasheets, derating, fit and at least 30 deliberate manual mating events without damage (not proof of high-cycle endurance) |
| P4 | Create desk battery base, chemistry-specific BMS/charger and charging behavior | Heat and short tests; charging while running only after tested power-path |
| P5 | Mobile base and high-cycle docking if base changes are frequent | Tested base ID/no-motion fallback, cycle life and independent wheel safety |

**Current procurement:** Core kit + SPI LCD + MG90S prototypes are plausible. Do not order batteries, pogo contacts, magnetic base, final connectors or charger based on this concept alone.
