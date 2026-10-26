# 7th CPC Pay Data (India)

Open, plain-CSV reference data for Indian central government pay under the 7th Central Pay Commission, maintained by **[8th Pay Calculator](https://8thpaycalculator.in/)**.

## Files

| File | What it holds |
|---|---|
| `pay-matrix-entry-pay.csv` | Entry (first cell) basic pay for each 7th CPC Pay Matrix level, 1 to 18 |
| `da-history-7th-cpc.csv` | Dearness Allowance / Dearness Relief rates since 1 January 2016 |
| `cpi-iw-2016-series.csv` | Monthly All-India CPI-IW (base 2016=100) from January 2025, with the Labour Bureau release date and press-release PDF for each month |

## Current DA / DR status

- **60%** of basic pay, effective **1 January 2026** (official).
- The July 2026 instalment is **not yet announced**. This repo is updated only after a PIB Cabinet release or a Department of Expenditure Office Memorandum.

## Notes

- DA instalments due 1 January 2020, 1 July 2020 and 1 January 2021 were frozen during COVID-19; the rate was restored to 28% from 1 July 2021 with no arrears for the frozen period.
- Always check the official order before acting on these figures. Primary sources: [PIB](https://pib.gov.in/), [Department of Expenditure](https://doe.gov.in/), [DoPPW](https://doppw.gov.in/), [Labour Bureau (CPI-IW)](https://labourbureau.gov.in/).

## How DA is worked out from CPI-IW

DA % = ((12-month average CPI-IW x 2.88) - 261.42) / 261.42 x 100, rounded down to a whole number. The 2.88 linking factor converts the 2016 series to the 2001 base used by the 7th CPC formula. Projections from this file are estimates only; the rate is fixed by the Cabinet and the Department of Expenditure.

## Calculators using this data

- [8th Pay Commission salary calculator](https://8thpaycalculator.in/)
- [Pension calculator](https://8thpaycalculator.in/pension-calculator/)
- [DA hike tracker](https://8thpaycalculator.in/da-hike-tracker/)
- [8thpaycalculator.in/expected-da-january-2027/](https://8thpaycalculator.in/expected-da-january-2027/) (month-by-month DA projection from this CPI-IW series)

## License

Data: CC BY 4.0. Please credit 8thpaycalculator.in when reusing.

Spotted an error? Open an issue.
