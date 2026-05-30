# No-Show Cost Calculator for Medical Practices

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen.svg)](#)

A CLI tool that calculates the real financial impact of patient no-shows and estimates the ROI of automated reminder systems.

---

## Why This Matters

In Italy, **15-20% of medical appointments result in no-shows** ([AGENAS 2024](https://www.agenas.gov.it/)). Each missed appointment costs **EUR 80-150** in lost revenue plus fixed costs that the practice still has to pay.

For a practice with **100 appointments/day**, that translates to:

| Metric | Conservative | Realistic |
|--------|-------------|-----------|
| Daily no-shows | 15 | 20 |
| Cost per no-show | EUR 80 | EUR 150 |
| **Annual loss** | **EUR 60,000** | **EUR 150,000** |

Most practices underestimate this cost because they only count the missed fee, ignoring staff time, room costs, and the opportunity cost of slots that could have been filled.

---

## Quick Start

```bash
# No installation needed — just Python 3.8+
git clone https://github.com/SynapticaSolution/noshow-cost-calculator.git
cd noshow-cost-calculator

# Run with your practice's numbers
python noshow_calculator.py --appointments 100 --rate 18 --avg-fee 85
```

Or with pip (coming soon):

```bash
pip install noshow-calculator
noshow-calc --appointments 100 --rate 18 --avg-fee 85
```

---

## How It Works

The calculator uses a three-layer cost model:

### 1. Direct Cost (Lost Revenue)
The fee you would have collected for the appointment.

```
direct_cost = no_shows × avg_fee
```

### 2. Indirect Cost (Fixed Overhead)
Staff time, room cost, equipment depreciation, utilities — costs you pay regardless of whether the patient shows up. Estimated at **30% of direct cost** based on healthcare industry benchmarks.

```
indirect_cost = direct_cost × 0.30
```

### 3. Opportunity Cost
The slot could have been filled by another patient. This is the hardest to quantify but often the largest component. The calculator uses a conservative **fill rate of 60%** for freed slots.

```
opportunity_cost = no_shows × avg_fee × fill_rate
```

### Total Annual Loss

```
total_loss = (direct_cost + indirect_cost + opportunity_cost) × working_days
```

---

## Example Output

```
$ python noshow_calculator.py --appointments 100 --rate 18 --avg-fee 85

╔══════════════════════════════════════════════════════════════╗
║              NO-SHOW COST CALCULATOR                        ║
║              For Medical Practices                          ║
╚══════════════════════════════════════════════════════════════╝

  Practice Profile
  ─────────────────────────────────────────────
  Daily appointments:        100
  No-show rate:              18.0%
  Average fee per visit:     EUR 85.00
  Working days per year:     250

  Daily Impact
  ─────────────────────────────────────────────
  Daily no-shows:            18
  Direct lost revenue:       EUR 1,530.00
  Indirect costs (30%):      EUR 459.00
  Opportunity cost (60%):    EUR 918.00
  Total daily loss:          EUR 2,907.00

  Annual Impact
  ─────────────────────────────────────────────
  Annual no-shows:           4,500
  Total annual loss:         EUR 726,750.00

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ROI of WhatsApp Reminders (40% reduction)
  ─────────────────────────────────────────────
  No-shows after reminders:  10.8 / day
  Annual loss after:         EUR 436,050.00
  Annual savings:            EUR 290,700.00
  Reminder system cost:      EUR 2,400.00 / year
  Net ROI:                   EUR 288,300.00 / year
  ROI multiplier:            121x
```

---

## CLI Usage

```bash
# Basic usage
python noshow_calculator.py --appointments 100 --rate 18 --avg-fee 85

# Custom working days (default: 250)
python noshow_calculator.py --appointments 80 --rate 15 --avg-fee 120 --working-days 230

# Short flags
python noshow_calculator.py -a 100 -r 18 -f 85 -d 250
```

### All Options

| Flag | Description | Default |
|------|-------------|---------|
| `-a`, `--appointments` | Daily appointments | *required* |
| `-r`, `--rate` | No-show rate (%) | *required* |
| `-f`, `--avg-fee` | Average fee per visit (EUR) | *required* |
| `-d`, `--working-days` | Working days per year | 250 |

---

## Python API

You can also use it as a library:

```python
from noshow_calculator import NoShowCalculator

calc = NoShowCalculator(
    daily_appointments=100,
    noshow_rate=18.0,
    avg_fee=85.0,
    working_days=250
)

results = calc.calculate()

print(f"Annual no-shows: {results['annual_noshow_count']:,.0f}")
print(f"Total annual loss: EUR {results['total_annual_loss']:,.2f}")
print(f"ROI with WhatsApp reminders: EUR {results['net_roi']:,.2f}/year")
```

---

## Reduction Strategies

| Strategy | No-Show Reduction | Staff Cost | Source |
|----------|-------------------|------------|--------|
| **WhatsApp reminders** | 35-45% | None (automated) | Clinical studies, [ClinicFlow data](https://synaptica-solution.com/clinicflow/) |
| SMS reminders | 20-30% | None (automated) | Systematic reviews |
| Email reminders | 10-15% | None (automated) | Meta-analysis |
| Phone calls | 25-35% | High (manual) | Healthcare surveys |

**Best results** come from combining WhatsApp/SMS reminders with a structured follow-up protocol. Automated systems pay for themselves within the first month for most practices.

---

## Related Resources

Maintained by **[Synaptica Solution](https://synaptica-solution.com)**, Italian software studio for SME automation.

| If you need… | See… |
|---|---|
| Automated no-show reduction for medical practices | [ClinicFlow](https://synaptica-solution.com/clinicflow/) |
| Guide: no-show significato e come ridurlo | [No-Show: Significato](https://synaptica-solution.com/knowledge/cos-e-no-show-significato/) |
| WhatsApp reminders for medical appointments | [Guida riduzione no-show](https://synaptica-solution.com/guida-riduzione-no-show-studi-medici/) |
| All open source tools | [Open Source Hub](https://synaptica-solution.com/open-source/) |

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

Made by [Synaptica Solution](https://synaptica-solution.com) — AI & Process Automation for Italian SMEs
