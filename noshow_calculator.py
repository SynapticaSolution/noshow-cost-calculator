#!/usr/bin/env python3
"""
No-Show Cost Calculator for Medical Practices

Calculates the real financial impact of patient no-shows and estimates
the ROI of automated reminder systems (WhatsApp, SMS, etc.).

Zero dependencies — runs on Python 3.8+.

https://github.com/SynapticaSolution/noshow-cost-calculator
Made by Synaptica Solution — https://synaptica-solution.com
"""

import argparse
import sys

__version__ = "1.0.0"

# Cost model constants
INDIRECT_COST_RATIO = 0.30  # 30% of direct cost (staff, room, equipment)
OPPORTUNITY_FILL_RATE = 0.60  # 60% of freed slots could be filled
WHATSAPP_REDUCTION_RATE = 0.40  # 40% reduction with WhatsApp reminders
WHATSAPP_MONTHLY_COST = 200.0  # EUR/month for reminder system


class NoShowCalculator:
    """Calculate the financial impact of patient no-shows."""

    def __init__(
        self,
        daily_appointments: int,
        noshow_rate: float,
        avg_fee: float,
        working_days: int = 250,
    ):
        self.daily_appointments = daily_appointments
        self.noshow_rate = noshow_rate / 100.0  # Convert percentage
        self.avg_fee = avg_fee
        self.working_days = working_days

    def calculate(self) -> dict:
        """Run the full cost calculation and return results."""
        # Daily figures
        daily_noshows = self.daily_appointments * self.noshow_rate
        direct_daily = daily_noshows * self.avg_fee
        indirect_daily = direct_daily * INDIRECT_COST_RATIO
        opportunity_daily = daily_noshows * self.avg_fee * OPPORTUNITY_FILL_RATE
        total_daily = direct_daily + indirect_daily + opportunity_daily

        # Annual figures
        annual_noshows = daily_noshows * self.working_days
        total_annual = total_daily * self.working_days

        # ROI of WhatsApp reminders
        reduced_noshows_daily = daily_noshows * (1 - WHATSAPP_REDUCTION_RATE)
        reduced_direct = reduced_noshows_daily * self.avg_fee
        reduced_indirect = reduced_direct * INDIRECT_COST_RATIO
        reduced_opportunity = (
            reduced_noshows_daily * self.avg_fee * OPPORTUNITY_FILL_RATE
        )
        reduced_total_daily = reduced_direct + reduced_indirect + reduced_opportunity
        reduced_total_annual = reduced_total_daily * self.working_days

        annual_savings = total_annual - reduced_total_annual
        reminder_annual_cost = WHATSAPP_MONTHLY_COST * 12
        net_roi = annual_savings - reminder_annual_cost
        roi_multiplier = (
            annual_savings / reminder_annual_cost if reminder_annual_cost > 0 else 0
        )

        return {
            # Daily
            "daily_noshow_count": daily_noshows,
            "direct_daily_loss": direct_daily,
            "indirect_daily_loss": indirect_daily,
            "opportunity_daily_loss": opportunity_daily,
            "total_daily_loss": total_daily,
            # Annual
            "annual_noshow_count": annual_noshows,
            "total_annual_loss": total_annual,
            # ROI
            "reduced_noshows_daily": reduced_noshows_daily,
            "reduced_total_annual": reduced_total_annual,
            "annual_savings": annual_savings,
            "reminder_annual_cost": reminder_annual_cost,
            "net_roi": net_roi,
            "roi_multiplier": roi_multiplier,
        }


def print_results(
    daily_appointments: int,
    noshow_rate: float,
    avg_fee: float,
    working_days: int,
    results: dict,
) -> None:
    """Pretty-print the calculation results."""
    print()
    print("\u2554" + "\u2550" * 62 + "\u2557")
    print("\u2551" + "              NO-SHOW COST CALCULATOR".ljust(62) + "\u2551")
    print("\u2551" + "              For Medical Practices".ljust(62) + "\u2551")
    print("\u255a" + "\u2550" * 62 + "\u255d")
    print()

    # Practice profile
    print("  Practice Profile")
    print("  " + "\u2500" * 45)
    print(f"  Daily appointments:        {daily_appointments}")
    print(f"  No-show rate:              {noshow_rate:.1f}%")
    print(f"  Average fee per visit:     EUR {avg_fee:,.2f}")
    print(f"  Working days per year:     {working_days}")
    print()

    # Daily impact
    print("  Daily Impact")
    print("  " + "\u2500" * 45)
    print(f"  Daily no-shows:            {results['daily_noshow_count']:.0f}")
    print(f"  Direct lost revenue:       EUR {results['direct_daily_loss']:,.2f}")
    print(f"  Indirect costs (30%):      EUR {results['indirect_daily_loss']:,.2f}")
    print(f"  Opportunity cost (60%):    EUR {results['opportunity_daily_loss']:,.2f}")
    print(f"  Total daily loss:          EUR {results['total_daily_loss']:,.2f}")
    print()

    # Annual impact
    print("  Annual Impact")
    print("  " + "\u2500" * 45)
    print(f"  Annual no-shows:           {results['annual_noshow_count']:,.0f}")
    print(f"  Total annual loss:         EUR {results['total_annual_loss']:,.2f}")
    print()

    print("  " + "\u2501" * 45)
    print()

    # ROI section
    print("  ROI of WhatsApp Reminders (40% reduction)")
    print("  " + "\u2500" * 45)
    print(f"  No-shows after reminders:  {results['reduced_noshows_daily']:.1f} / day")
    print(f"  Annual loss after:         EUR {results['reduced_total_annual']:,.2f}")
    print(f"  Annual savings:            EUR {results['annual_savings']:,.2f}")
    print(
        f"  Reminder system cost:      EUR {results['reminder_annual_cost']:,.2f} / year"
    )
    print(f"  Net ROI:                   EUR {results['net_roi']:,.2f} / year")
    print(f"  ROI multiplier:            {results['roi_multiplier']:.0f}x")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Calculate the real cost of patient no-shows for medical practices.",
        epilog="Made by Synaptica Solution — https://synaptica-solution.com",
    )
    parser.add_argument(
        "-a",
        "--appointments",
        type=int,
        required=True,
        help="Number of daily appointments",
    )
    parser.add_argument(
        "-r",
        "--rate",
        type=float,
        required=True,
        help="No-show rate as percentage (e.g., 18 for 18%%)",
    )
    parser.add_argument(
        "-f",
        "--avg-fee",
        type=float,
        required=True,
        help="Average fee per visit in EUR",
    )
    parser.add_argument(
        "-d",
        "--working-days",
        type=int,
        default=250,
        help="Working days per year (default: 250)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"noshow-calculator {__version__}",
    )

    args = parser.parse_args()

    # Validate inputs
    if args.appointments <= 0:
        print("Error: appointments must be a positive number.", file=sys.stderr)
        sys.exit(1)
    if not (0 < args.rate <= 100):
        print("Error: rate must be between 0 and 100.", file=sys.stderr)
        sys.exit(1)
    if args.avg_fee <= 0:
        print("Error: avg-fee must be a positive number.", file=sys.stderr)
        sys.exit(1)
    if args.working_days <= 0:
        print("Error: working-days must be a positive number.", file=sys.stderr)
        sys.exit(1)

    calc = NoShowCalculator(
        daily_appointments=args.appointments,
        noshow_rate=args.rate,
        avg_fee=args.avg_fee,
        working_days=args.working_days,
    )

    results = calc.calculate()
    print_results(
        args.appointments, args.rate, args.avg_fee, args.working_days, results
    )


if __name__ == "__main__":
    main()
