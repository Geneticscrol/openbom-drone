# 6 · BOM

[`kite5.json`](kite5.json) is the single source of truth for Kite-5's parts, mass, and
example cost — the only BOM dataset in this repo. INR is order-of-magnitude, not a shop
price; there are deliberately no shop links here, so this file can't drift the way a
shop-catalog copy would.

| Item | Qty | Grams | INR (example) |
|---|---|---|---|
| 5-inch freestyle frame | 1 | 120 | 2800 |
| 2207 1950KV motor | 4 | 32 each | 1400 each |
| 5in 3-blade props | 4 | 4 each | 80 each |
| F405 50A AIO FC+ESC | 1 | 18 | 4500 |
| ELRS 2.4 GHz RX | 1 | 1 | 900 |
| 5.8 GHz analog VTX | 1 | 8 | 1800 |
| Nano analog camera | 1 | 6 | 1500 |
| XT60, pads, screws | 1 | 25 | 400 |
| 4S 1500 mAh LiPo | 1 | 175 | 2200 |

Total: 497 g, ~₹20,020 example cost, against a 650 g target — see
[`3_Mass_and_Power/`](../3_Mass_and_Power/README.md) for the breakdown and
`kite5 mass` to regenerate this table from the live JSON.

## Proposing a BOM change

1. Edit `kite5.json`.
2. Run `kite5 mass` locally and sanity-check the new totals.
3. Open a PR — see [`CONTRIBUTING.md`](../CONTRIBUTING.md).
