from __future__ import annotations

import argparse

from kite5 import hover_power, mass_budget
from kite5.bom import load
from kite5.mixer import mix


def _cmd_mass(args: argparse.Namespace) -> None:
    doc = load()
    mass_budget.print_report(doc, mass_budget.summarise(doc))


def _cmd_hover(args: argparse.Namespace) -> None:
    hover_power.print_report(hover_power.report(args.thrust_g, args.disk_cm, args.fom))


def _cmd_mixer(args: argparse.Namespace) -> None:
    for name, value in mix(args.throttle, args.roll, args.pitch, args.yaw).items():
        print(f"{name}: {value:.3f}")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="kite5", description="Kite-5 design-stage engineering calculators."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    mass_p = sub.add_parser("mass", help="Sum the BOM mass/cost budget from 6_BOM/kite5.json")
    mass_p.set_defaults(func=_cmd_mass)

    hover_p = sub.add_parser("hover", help="Estimate induced hover power")
    hover_p.add_argument("--thrust-g", type=float, default=497.0)
    hover_p.add_argument("--disk-cm", type=float, default=12.7)
    hover_p.add_argument("--fom", type=float, default=0.65)
    hover_p.set_defaults(func=_cmd_hover)

    mixer_p = sub.add_parser("mixer", help="Run the QUADX stick-to-motor reference mixer")
    mixer_p.add_argument("--throttle", type=float, default=0.5)
    mixer_p.add_argument("--roll", type=float, default=0.0)
    mixer_p.add_argument("--pitch", type=float, default=0.0)
    mixer_p.add_argument("--yaw", type=float, default=0.0)
    mixer_p.set_defaults(func=_cmd_mixer)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
