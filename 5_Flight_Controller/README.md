# 5 · Betaflight map

`serialrx_provider = CRSF`
`motor_pwm_protocol = DSHOT300`
QUADX mixer. Dump `diff` from the real target after you solder.

Target FC: F405 50A AIO (per [BOM](../6_BOM/README.md)). Exact Betaflight target name is
TBD until a specific board is purchased.

## Resource map (template)

Fill in after flashing real hardware — these are placeholders, not a working `diff`:

```
# diff all

# resources
resource MOTOR 1 <TBD>
resource MOTOR 2 <TBD>
resource MOTOR 3 <TBD>
resource MOTOR 4 <TBD>
resource SERIAL_RX <TBD>

set serialrx_provider = CRSF
set motor_pwm_protocol = DSHOT300
```

## Motor layout

Standard QUADX, props-out, matching Betaflight's `mixerQuadX` convention:

| Motor | Position | Rotation |
|---|---|---|
| M1 | Rear-right | CW |
| M2 | Front-right | CCW |
| M3 | Rear-left | CCW |
| M4 | Front-left | CW |

[`kite5/mixer.py`](../kite5/mixer.py) (`kite5 mixer --throttle --roll --pitch --yaw`) is a
teaching/reference implementation of stick-to-motor math matching this table and
Betaflight's actual `mixerQuadX[]` coefficients — it is not firmware and never flies
anything. Once real hardware exists, the target's own `diff all` output is authoritative;
verify against that, not this script.

## Tuning

PID/rates: not tuned. Defaults until first flights — no fabricated tuning data here.
