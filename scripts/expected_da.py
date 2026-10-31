#!/usr/bin/env python3
"""Running 7th CPC Dearness Allowance (DA) figure from the CPI-IW (2016=100) series.

Formula used by the 7th CPC (central government):
    DA % = ((12-month average CPI-IW x 2.88) - 261.42) / 261.42 x 100

* 2.88 is the Labour Bureau linking factor from the 2016 series to the 2001 series.
* 261.42 is the 12-month average CPI-IW (2001=100) on which 7th CPC pay is based.
* The official rate is the whole number below the result (fraction dropped).

The half-year DA is set from the 12 months ending in the month before it is due:
January DA uses Jan-Dec of the previous year, July DA uses Jul-Jun.

When the current window is not yet complete, the missing months are held at the
latest published index (the "flat" case). This is an estimate only; the rate is
fixed by the Cabinet and notified by the Department of Expenditure.

Usage:
    python3 scripts/expected_da.py [path/to/cpi-iw-2016-series.csv]

Data: https://github.com/Techno212-eng/-7th-cpc-pay-data
Calculator: https://8thpaycalculator.in/expected-da-january-2027/
"""
import csv
import math
import os
import sys

LINKING_FACTOR = 2.88
BASE = 261.42


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("month") and r.get("cpi_iw_base_2016_100"):
                rows.append((r["month"].strip(), float(r["cpi_iw_base_2016_100"])))
    rows.sort()
    return rows


def da_percent(avg_2016_series):
    """Return (exact DA %, DA % truncated to 2 decimals, whole-number DA %)."""
    exact = (avg_2016_series * LINKING_FACTOR - BASE) / BASE * 100
    two_dp = math.floor(exact * 100) / 100
    return exact, two_dp, math.floor(exact)


def window_for(last_month):
    """The six-month DA window that last_month falls in: (due label, months list)."""
    y, m = map(int, last_month.split("-"))
    if m <= 6:  # Jul (prev year) .. Jun -> DA due 1 July of this year
        start = (y - 1, 7)
        due = f"1 July {y}"
    else:      # Jan .. Dec -> DA due 1 January next year
        start = (y, 1)
        due = f"1 January {y + 1}"
    months = []
    yy, mm = start
    for _ in range(12):
        months.append(f"{yy:04d}-{mm:02d}")
        mm += 1
        if mm > 12:
            yy, mm = yy + 1, 1
    return due, months


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "..", "cpi-iw-2016-series.csv")
    rows = load(path)
    if not rows:
        sys.exit("No CPI-IW rows found in " + path)
    index = dict(rows)
    last_month, last_value = rows[-1]
    due, months = window_for(last_month)

    have = [m for m in months if m in index]
    missing = [m for m in months if m not in index]
    values = [index.get(m, last_value) for m in months]
    avg = sum(values) / 12
    exact, two_dp, whole = da_percent(avg)

    print(f"Latest CPI-IW: {last_month} = {last_value}")
    print(f"DA due {due}: window {months[0]} to {months[-1]}")
    print(f"Published months in window: {len(have)} of 12")
    if missing:
        print(f"Held flat at {last_value}: {', '.join(missing)}")
    print(f"12-month average (2016=100): {avg:.4f}")
    print(f"Running DA: {two_dp:.2f}%  -> expected rate {whole}% (estimate)")


if __name__ == "__main__":
    main()
