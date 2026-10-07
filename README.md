# Data-Driven Optimization of Rubber Tapping Strategies

## Project Overview

This project analyzes and compares two rubber tapping strategies:

- *With Medicine*
- *Without Medicine*

The main goal is to identify the better-performing strategy based on latex production, profitability, working effort, and bark consumption.

The project uses *Python for data analysis* and *Power BI for interactive visualization and dashboard creation*.

> *Note:* The conclusions are based on the observed 4-month dataset and should not be considered as a universal or causal conclusion about rubber tree health.

---

## Objectives

The main objectives of this project are:

- Compare rubber latex production between two tapping strategies.
- Analyze income, expense, and profit.
- Compare the number of working/tapping days.
- Analyze working time and effort.
- Calculate latex production per day and per hour.
- Calculate profit per day and per hour.
- Compare recorded bark consumption.
- Identify the better-performing tapping strategy.
- Build an interactive Power BI dashboard for decision-making.

---

## Problem Statement

Traditional rubber tapping can require frequent tapping operations, which may increase labor requirements and bark consumption.

This project investigates whether a medicine-based tapping strategy can provide better productivity and profitability while requiring fewer tapping days.

The analysis compares real-world observations from two plantations over a 4-month period.

---

## Dataset

The dataset contains daily rubber tapping records.

### Main Features

| Column | Description |
|---|---|
| Date | Date of tapping |
| Plantation | Plantation number |
| Treatment | Tapping strategy |
| Latex | Latex quantity produced |
| Unit | Latex measurement unit |
| Dry Weight | Dry weight of latex |
| Time Taken | Time required for tapping |
| Bark | Bark consumed/removed |
| Expense | Daily tapping-related expense |
| Income | Income generated |
| Profit | Profit after expense |
| Number | Record/worker reference |

### Strategies

| Treatment | Strategy |
|---|---|
| 1 | With Medicine |
| 0 | Without Medicine |

---

## Technology stack Used

- *Python*
- *Pandas*
- *NumPy*
- *Matplotlib*
- *Seaborn*
- *Scikit-learn*
- *Excel*
- *Power BI*
- *GitHub*

---

##  Project Workflow

```text
Data Collection
      ↓
Excel Dataset
      ↓
Data Cleaning & Preprocessing
      ↓
Python Data Analysis
      ↓
Performance Calculations
      ↓
Strategy Comparison
      ↓
Optimization Analysis
      ↓
Power BI Dashboard
      ↓
Final Recommendation
```

## Findings

Based on the analysis of the 4-month rubber tapping dataset, the following findings were obtained:
1. With Medicine produced more latex.
The medicine-based strategy produced 3,735 kg of latex compared with 2,617 kg without medicine.
2. Higher daily productivity was observed with medicine.
Average latex production was 91.10 kg/day with medicine, compared with 44.36 kg/day without medicine.
3. Fewer tapping days were required.
The With Medicine strategy required 41 working days, while the Without Medicine strategy required 59 working days. This indicates that the longer tapping gap can reduce the number of tapping operations in the observed period.
4. Higher profit was achieved with medicine.
Total profit was ₹264,872 with medicine compared with ₹165,982 without medicine.
5. Profit per working day was significantly higher.
The With Medicine strategy generated approximately ₹6,460/day, while the Without Medicine strategy generated approximately ₹2,813/day.
6. Better time efficiency was observed.
Although the medicine strategy required 8 hours per working day, compared with 6 hours without medicine, it required fewer total working hours: 328 hours vs. 354 hours.
7. Profit per hour was higher with medicine.
The With Medicine strategy achieved approximately ₹807.54 profit/hour, compared with ₹468.88/hour without medicine.
8. Lower recorded bark consumption was observed.
Total recorded bark consumption was 20.5 cm with medicine compared with 29.5 cm without medicine. This supports the project's idea that fewer tapping operations may help reduce bark usage.
9. The medicine strategy showed better overall performance.
Considering latex production, profit, working days, productivity per hour, and recorded bark consumption, With Medicine was the best-performing strategy in the observed dataset.
10. Potential sustainability benefit.
A longer tapping gap may provide more recovery time for the trees and reduce repeated bark removal. Proper fertilizer management may further support tree growth and recovery. However, the current 4-month data is not sufficient to prove long-term tree-health effects.
## Final Finding
The With Medicine strategy demonstrated better overall productivity, profitability, time efficiency, and lower recorded bark consumption than the Without Medicine strategy in the observed 4-month dataset. Therefore, it is recommended as the better-performing strategy for the conditions represented in this study.
