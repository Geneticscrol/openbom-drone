# 1 · Project description

**Name:** Kite-5
**Status:** Design / pre-build. No physical airframe exists yet.
**Goal:** One reference 5-inch build an Indian club pilot can copy, weigh, and flash without
a forum thread.

## In / out

**In:** frame, 2207 motors, 5in props, AIO, ELRS, analog VTX, 4S, mass + induced power.
**Out:** live store prices, digital goggle stacks as the default, autopilots.

## Who this is for

A club pilot who wants a copyable, calculable reference build — not a shop, not a forum
thread, not a "buy this exact link" list. Someone who can read a BOM, run a Python script,
and solder a harness.

## Design philosophy

- Reproducible: every number in this repo comes from a script or a spec sheet, not a gut
  feeling.
- Calculable: mass and power are budgets you can check with a kitchen scale and a script,
  not marketing claims.
- Honest about build status: nothing here claims to be flown or measured until it actually
  is.
- No vendor lock-in: parts are described by category and spec, not by a single shop link.

## Success criteria

| Metric | Target | Verified by |
|---|---|---|
| All-up weight | Within 40 g of the BOM sheet | Kitchen scale, once built |
| Hover current | Same band as `kite5 hover` estimate | Bench current-meter, once built |
| Mass budget | Under 650 g target | `kite5 mass` (today: 497 g, 153 g margin) |

## Map

- [`2_Architecture/`](../2_Architecture/README.md) — system diagram, interconnects
- [`3_Mass_and_Power/`](../3_Mass_and_Power/README.md) — mass budget, hover power
- [`4_Wiring_and_Harness/`](../4_Wiring_and_Harness/README.md) — harness, power-up checklist
- [`5_Flight_Controller/`](../5_Flight_Controller/README.md) — Betaflight map, motor layout
- [`6_BOM/`](../6_BOM/README.md) — parts list
