# 7th CPC Pay Data (India)

Open, plain-CSV reference data for Indian central government pay under the 7th Central Pay Commission: Dearness Allowance (DA) / Dearness Relief (DR) rates, the monthly CPI-IW index that drives them, and Pay Matrix entry pay. Maintained by [8th Pay Calculator](https://8thpaycalculator.in/).

## What is in the repo

| File | What it holds |
|---|---|
| `da-dr-history-7th-cpc.csv` | Central DA/DR rate by effective date, 1 January 2016 (0%) to 1 July 2026 (63%). Columns: `effective_date`, `da_percent`, `source` (the Department of Expenditure Office Memorandum number, date and PDF link for each rate) |
| `cpi-iw-2016-series.csv` | Monthly All-India CPI-IW (base 2016=100) from January 2025, with the Labour Bureau release date and press-release PDF for each month |
| `pay-matrix-entry-pay.csv` | Entry (first cell) basic pay for each 7th CPC Pay Matrix level, 1 to 18 |
| `scripts/expected_da.py` | Works out the running DA figure for the next instalment from `cpi-iw-2016-series.csv` |
| `da-history-7th-cpc.csv` | Earlier version of the DA table (to 1 January 2026), kept so existing links keep working. Use `da-dr-history-7th-cpc.csv` for current data |

## Current DA / DR

- **63%** of basic pay from **1 July 2026** (DoE OM No. 1/2(i)/2026-E.II(B) dated 29.10.2026, [PDF](https://doe.gov.in/files/whats_new_documents/7thCPCEng.pdf)). It was 60% from 1 January 2026.
- Dearness Relief for central government pensioners moves at the same rate as DA.
- DA instalments due 1 January 2020, 1 July 2020 and 1 January 2021 were frozen during COVID-19, so DA stayed at 17%. It was restored to 28% from 1 July 2021 and then raised to 31% from the same date, with no arrears for the frozen period.

## How DA is worked out from CPI-IW

```
DA % = ((12-month average CPI-IW x 2.88) - 261.42) / 261.42 x 100
```

The 2.88 linking factor converts the 2016-base series to the 2001 base used by the 7th CPC formula, and 261.42 is the 2001-base average on which 7th CPC pay is fixed. The fraction is dropped to get the whole-number rate. January DA uses the January to December average of the previous year; July DA uses July to June.

Run the script to see the running figure (Python 3, no extra packages):

```
python3 scripts/expected_da.py
```

With CPI-IW published up to September 2026 and October to December held at the September index, it prints a running figure of 67.85% for 1 January 2027. This is an estimate only: the rate is fixed by the Cabinet and notified by the Department of Expenditure.

## Data sources

- **CPI-IW:** [Labour Bureau](https://labourbureau.gov.in/), monthly press releases (linked row by row in the CSV).
- **DA rates:** [Department of Expenditure](https://doe.gov.in/) Office Memoranda (linked row by row in the CSV), cross-checked against the [DoPPW Dearness Relief table](https://pensionersportal.gov.in/DRRATE_7CPC.aspx).
- **Pay Matrix:** 7th CPC Pay Matrix as notified in the CCS (Revised Pay) Rules, 2016.

Always check the official order before acting on these figures. The repo is updated only after a Department of Expenditure Office Memorandum or a Labour Bureau release.

## Calculators

- [8th Pay Commission salary calculator](https://8thpaycalculator.in/)
- [Expected DA for January 2027](https://8thpaycalculator.in/expected-da-january-2027/): month-by-month projection from the CPI-IW series in this repo
- [Pension calculator](https://8thpaycalculator.in/pension-calculator/)
- [DA hike tracker](https://8thpaycalculator.in/da-hike-tracker/)

## License

Data: CC BY 4.0. Please credit [8thpaycalculator.in](https://8thpaycalculator.in/) when reusing.

Spotted an error? Open an issue.

Last updated 31 Oct 2026
