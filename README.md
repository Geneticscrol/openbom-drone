# OpenBOM-Drone — Kite-5 reference 5-inch airframe

Engineering package for a **5-inch, 4S, analog + ELRS** freestyle / trainer quad.

This is not a shopping website. The repo is the design: mass budget, power estimate, harness, Betaflight resource map, and small pieces of code you can run or flash.

## Airframe

| Item | Choice |
|---|---|
| Class | 5-inch quad, X mix |
| Battery | 4S 1300–1500 mAh LiPo |
| Target AUW | ≤ 650 g with pack |
| Control | ELRS 2.4 GHz |
| Video | Analog 5.8 GHz, PIT on the bench |
| FC | F4/F7 AIO or stack, Betaflight |

Not an armed airframe.

## Tree

```
1_Project_Description/
2_Architecture/
3_Mass_and_Power/
4_Wiring_and_Harness/
5_Flight_Controller/
6_BOM/
software/     mass budget + hover power (CLI)
firmware/     ESP8266 pack-voltage beep
```

## Run the numbers

```bash
python software/mass_budget.py
python software/hover_power.py --thrust-g 650 --disk-cm 12.7
```

## License

MIT.
