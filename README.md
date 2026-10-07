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
