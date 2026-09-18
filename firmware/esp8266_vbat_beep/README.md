# ESP8266 pack-voltage nag

Bench / bag only. Not flown, not soldered into the airframe. Beeps GPIO2 when a cell drops
below 3.50 V so a pack doesn't sit forgotten in a bag past storage voltage.

**Status: design-stage.** The calibration constants below (`PACK_FULL_ADC`, `PACK_FULL_V`)
are illustrative starting points, not measurements — this hasn't run on physical hardware
yet. Calibrate them for real before trusting the beep threshold.

## Wiring

```mermaid
flowchart LR
    VBAT["Pack V+"] -->|100k| A0["ESP8266 A0"]
    A0 -->|20k| GND["Pack GND"]
```

Divider: `VBAT -- 100k -- A0 -- 20k -- GND`. Target board is a bare ESP-01 module
(`esp01_1m`) — an external divider into A0, no onboard scaling. Swapping to a dev board
with its own onboard A0 divider (e.g. a Wemos D1 Mini) means re-deriving the constants
below from scratch; don't reuse these numbers on a different board.

## Build and flash

Requires [PlatformIO](https://platformio.org/) (`pip install platformio`, or the VS Code
extension).

```bash
cd firmware/esp8266_vbat_beep
pio run                       # compile
pio run --target upload       # flash
pio device monitor             # watch the adc=/pack=/cell= serial log
```

## Calibration walkthrough

The constants in `src/main.cpp` are bench numbers, not measured ones. Before trusting the
beep:

1. Charge the pack to full and flash the firmware.
2. Read the `adc=` value printed over serial at that moment.
3. Measure the real pack voltage with a multimeter at the same moment.
4. Set `PACK_FULL_ADC` to the reading from step 2, `PACK_FULL_V` to step 3.
5. Reflash, then verify `pack=`/`cell=` in the serial log track the multimeter across a
   discharge.

## License

MIT, same as the rest of the repo.
