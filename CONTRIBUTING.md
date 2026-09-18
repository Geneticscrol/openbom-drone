# Contributing to OpenBOM-Drone

Thanks for looking at Kite-5. This is an early-stage, small-team project — response times
vary, but PRs and issues are genuinely welcome.

## Repository layout

| Path | Contents |
|---|---|
| `1_Project_Description/` | Goals, non-goals, success criteria |
| `2_Architecture/` | System block diagram, protocol/interconnect table |
| `3_Mass_and_Power/` | Mass budget, hover power estimate |
| `4_Wiring_and_Harness/` | Harness diagram, connector table, power-up checklist |
| `5_Flight_Controller/` | Betaflight resource map, motor/mixer layout |
| `6_BOM/` | `kite5.json` — single source of truth for parts, mass, price |
| `kite5/` | Installable Python package: mass/hover/mixer calculators |
| `firmware/` | ESP8266 pack-voltage beep (PlatformIO) |
| `tests/` | pytest suite for `kite5/` |

## Proposing a BOM change

Edit `6_BOM/kite5.json`, run `kite5 mass` locally to sanity-check the new totals, then open
a PR. `kite5.json` is the only BOM dataset in the repo — don't add a second one.

## Code standards

- **Python** — stdlib-only runtime dependencies unless discussed in an issue first. Run
  `ruff check .` and `ruff format --check .` before pushing. Test with `pytest -q`.
- **Firmware** — PlatformIO project under `firmware/`. Document any board or pin changes in
  the firmware README, and keep calibration constants commented (what they mean, how to
  re-derive them).
- **Docs** — keep the numbered-folder convention (`1_Project_Description` … `6_BOM`).
  Diagrams stay as Mermaid in Markdown, no binary image assets, unless there's a concrete
  reason (e.g. once real photos/CAD exist).

## Local setup

```bash
pip install -e ".[dev]"
ruff check .
ruff format --check .
pytest -q
```

## Pull request checklist

- [ ] Tests pass locally (`pytest -q`)
- [ ] Lint and format are clean (`ruff check .`, `ruff format --check .`)
- [ ] Docs updated if BOM data or calculator behavior changed
- [ ] No fabricated hardware or flight-test claims — Kite-5 is design-stage; if you haven't
      measured it on real hardware, say so
- [ ] Linked issue, if applicable

See also the [Code of Conduct](CODE_OF_CONDUCT.md) and the issue templates under
`.github/ISSUE_TEMPLATE/`.
