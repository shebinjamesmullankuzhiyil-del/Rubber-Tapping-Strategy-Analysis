# Data-Driven Optimization of Rubber Tapping Strategies

## Project Overview

This project analyzes and compares two rubber tapping strategies:

- **With Medicine**
- **Without Medicine**

The main objective is to identify the better-performing tapping strategy based on **latex production, revenue, working days, time efficiency, tapping frequency, and recorded bark consumption**.

The project uses **Python for data cleaning and analysis** and **Power BI for interactive dashboard visualization**.

> **Note:** The conclusions are based on the observed 4-month dataset and should not be considered universal or causal conclusions about rubber tree health or long-term tree lifespan.

---

## Objectives

The main objectives of this project are:

- Compare latex production between two tapping strategies.
- Analyze total and daily revenue.
- Compare the number of working/tapping days.
- Analyze total working hours and time efficiency.
- Calculate latex production per working day.
- Calculate latex production per working hour.
- Calculate revenue per working day.
- Calculate revenue per working hour.
- Compare recorded bark consumption.
- Analyze the actual tapping gap between tapping sessions.
- Identify the better-performing tapping strategy.
- Develop an interactive Power BI dashboard for decision-making.

---

## Problem Statement

Traditional rubber tapping may require frequent tapping operations, which can increase the number of working days, labor effort, and bark consumption.

This project investigates whether a medicine-based tapping strategy can achieve higher latex productivity and revenue while requiring fewer tapping operations.

The study compares observed data from two plantations over a **4-month period** and uses data analytics to identify the better-performing strategy.

---

## Dataset

The dataset contains **100 daily rubber tapping records** collected over a 4-month study period.

### Main Features

| Column | Description |
|---|---|
| Date | Date of tapping |
| Plantation | Plantation number |
| Treatment | Tapping strategy indicator |
| Latex | Quantity of latex produced |
| Unit | Unit of latex measurement |
| Dry Weight | Dry weight of latex |
| Time Taken | Time required for the tapping operation |
| Bark | Recorded bark consumption |
| Expense | Recorded tapping-related expense |
| Income | Recorded revenue from latex |
| Number | Number/reference associated with the tapping record |

### Strategies

| Treatment | Strategy |
|---|---|
| 1 | With Medicine |
| 0 | Without Medicine |

---

## Technology Stack

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Excel**
- **Power BI**
- **GitHub**

---

## Project Workflow

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
Revenue & Productivity Analysis
      ↓
Bark & Tapping Gap Analysis
      ↓
Power BI Dashboard
      ↓
Final Recommendation
```

---

# Analysis Results

The analysis was performed on **100 observed tapping records**.

### Overall Dataset

| Metric | Value |
|---|---:|
| Total Records | 100 |
| Total Latex | **6,352 kg** |
| Total Revenue | **₹5,39,920** |
| Total Recorded Tapping Expense | **₹1,09,066** |
| Total Working Days | **100 days** |
| Total Working Hours | **682 hours** |

---

# Strategy Comparison

| Metric | With Medicine | Without Medicine |
|---|---:|---:|
| Working Days | **41** | **59** |
| Total Latex | **3,735 kg** | **2,617 kg** |
| Latex per Working Day | **91.10 kg/day** | **44.36 kg/day** |
| Total Revenue | **₹3,17,475** | **₹2,22,445** |
| Revenue per Working Day | **₹7,743/day** | **₹3,770/day** |
| Total Working Hours | **328 hours** | **354 hours** |
| Average Time per Working Day | **8 hours** | **6 hours** |
| Latex per Working Hour | **11.39 kg/hour** | **7.39 kg/hour** |
| Revenue per Working Hour | **₹967.91/hour** | **₹628.38/hour** |
| Recorded Bark Consumption | **20.5 cm** | **29.5 cm** |
| Average Tapping Gap | **3.05 days** | **2.10 days** |

---

# Key Findings

### 1. Higher Latex Production

The **With Medicine** strategy produced **3,735 kg** of latex, compared with **2,617 kg** for the Without Medicine strategy.

This represents an observed difference of:

**1,118 kg more latex with the With Medicine strategy.**

---

### 2. Higher Daily Productivity

The average latex production was:

- **With Medicine:** 91.10 kg/day
- **Without Medicine:** 44.36 kg/day

Therefore, the With Medicine strategy showed substantially higher observed latex productivity per working day.

---

### 3. Higher Revenue

The With Medicine strategy generated:

**₹3,17,475**

while the Without Medicine strategy generated:

**₹2,22,445**

The observed revenue difference was:

**₹95,030**

in favor of the With Medicine strategy.

---

### 4. Higher Revenue per Working Day

The observed revenue per working day was:

- **With Medicine:** ₹7,743/day
- **Without Medicine:** ₹3,770/day

This indicates that the With Medicine strategy generated considerably higher revenue for each observed working day.

---

### 5. Fewer Working Days

The With Medicine strategy required:

**41 working days**

while the Without Medicine strategy required:

**59 working days**

Therefore, the With Medicine strategy used **18 fewer working days** during the observed 4-month period.

This suggests that the longer tapping interval reduced the number of tapping operations in the observed dataset.

---

### 6. Better Overall Time Efficiency

The With Medicine strategy required **328 total working hours**, while the Without Medicine strategy required **354 hours**.

Therefore, even though the average working session was longer with medicine:

- With Medicine: **8 hours/day**
- Without Medicine: **6 hours/day**

the With Medicine strategy required **26 fewer total working hours** during the study period.

---

### 7. Higher Revenue per Working Hour

Revenue per working hour was:

- **With Medicine:** ₹967.91/hour
- **Without Medicine:** ₹628.38/hour

This shows higher observed revenue efficiency per working hour for the With Medicine strategy.

---

### 8. Higher Latex Production per Working Hour

The observed latex production per working hour was:

- **With Medicine:** 11.39 kg/hour
- **Without Medicine:** 7.39 kg/hour

Therefore, the With Medicine strategy also showed better observed latex productivity relative to working time.

---

### 9. Lower Recorded Bark Consumption

Recorded bark consumption was:

- **With Medicine:** 20.5 cm
- **Without Medicine:** 29.5 cm

The With Medicine strategy used **9 cm less recorded bark** during the study period.

This represents approximately **30.5% lower recorded bark consumption** compared with the Without Medicine strategy.

Lower bark consumption means less bark was removed during the observed tapping operations, leaving more bark available for future tapping operations.

---

### 10. Longer Average Tapping Gap

The calculated average tapping gap was:

- **With Medicine:** 3.05 days
- **Without Medicine:** 2.10 days

Therefore, the With Medicine strategy showed an average tapping gap approximately **0.95 days longer**.

A longer interval between tapping sessions provides more time between tapping operations and may reduce the frequency of repeated bark removal.

---

# Bark Consumption and Tapping Sustainability

The analysis shows lower recorded bark consumption and a longer average tapping gap for the With Medicine strategy.

The observed relationship can be represented as:

```text
Longer Tapping Gap
        ↓
Fewer Tapping Operations
        ↓
Less Frequent Bark Removal
        ↓
Lower Recorded Bark Consumption
        ↓
Potentially Better Long-Term Tapping Sustainability
```

The With Medicine strategy therefore shows **better potential for sustainable long-term tapping** based on the observed dataset.

However, the current 4-month dataset is not sufficient to prove long-term changes in tree health or productive tree life.

---

# Revenue Analysis

Revenue was used instead of profit as the main financial performance measure.

The observed results were:

| Revenue Metric | With Medicine | Without Medicine |
|---|---:|---:|
| Total Revenue | ₹3,17,475 | ₹2,22,445 |
| Revenue per Working Day | ₹7,743 | ₹3,770 |
| Revenue per Working Hour | ₹967.91 | ₹628.38 |

The With Medicine strategy generated **₹95,030 more observed revenue** during the study period.

> **Important:** The recorded Expense column represents tapping-related expenses available in the dataset and does not represent complete annual plantation costs. Therefore, the project does not use profit as the primary financial conclusion.

---

# Optimization and Recommendation

The strategies were compared using multiple performance indicators:

1. Total latex production
2. Total revenue
3. Latex per working day
4. Revenue per working day
5. Revenue per working hour
6. Total working days
7. Total working hours
8. Recorded bark consumption
9. Average tapping gap

Based on the observed dataset, the **With Medicine** strategy performed better across the major productivity, revenue, time-efficiency, and bark-consumption indicators.

## Recommended Strategy

### **WITH MEDICINE**

The With Medicine strategy demonstrated:

- Higher latex production
- Higher revenue
- Higher latex production per working day
- Higher revenue per working day
- Higher latex production per working hour
- Higher revenue per working hour
- Fewer working days
- Fewer total working hours
- Lower recorded bark consumption
- Longer average tapping gap

---

# Power BI Dashboard

An interactive Power BI dashboard was developed to visualize the analysis.

### Dashboard Components

- Strategy selector
- Working Days comparison
- Total Latex KPI
- Total Revenue KPI
- Average Tapping Gap
- Revenue per Working Hour
- Average Latex per Working Day
- Total Latex by Strategy
- Bark Consumption by Strategy
- Strategy recommendation

The dashboard allows users to compare the two tapping strategies visually and support data-driven decision-making.

---

# Important Limitation

This project is based on an observed **4-month dataset**.

Therefore:

- The findings represent the conditions observed in this dataset.
- The results should not be treated as universal conclusions.
- The analysis does not prove that medicine directly causes higher latex production.
- The analysis does not prove that medicine increases rubber tree lifespan.
- Long-term tree health and productive tapping life require longer-term observations.
- The recorded Expense column does not represent complete plantation cost accounting.

### Long-Term Hypothesis

The study hypothesizes that:

```text
Longer Tapping Interval
        ↓
Less Frequent Bark Removal
        ↓
Lower Bark Consumption
        ↓
Potentially Better Long-Term Sustainability
        ↓
Potentially Longer Productive Tapping Life
```

Whether this could extend productive tapping life over many years requires long-term field data and further validation.

---

# Conclusion

The **With Medicine** strategy demonstrated better overall observed performance than the Without Medicine strategy during the 4-month study period.

It produced **1,118 kg more latex**, generated **₹95,030 more revenue**, required **18 fewer working days**, used **26 fewer total working hours**, and recorded **9 cm less bark consumption**.

The strategy also showed higher revenue and latex productivity per working day and per working hour, along with a longer average tapping gap.

Therefore, based on the available observations, **With Medicine is recommended as the better-performing tapping strategy for the conditions represented in this dataset**.

> **Final conclusion:** The With Medicine strategy showed higher observed productivity, revenue efficiency, time efficiency, and lower recorded bark consumption, indicating better potential for sustainable rubber tapping under the conditions studied.
