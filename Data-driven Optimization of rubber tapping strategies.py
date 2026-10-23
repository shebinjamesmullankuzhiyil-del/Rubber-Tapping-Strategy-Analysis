# ============================================================
# DATA-DRIVEN OPTIMIZATION OF RUBBER TAPPING STRATEGIES
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# ============================================================
# 1. LOAD DATA
# ============================================================

input_file = r"C:\Users\shebi\Downloads\rubber data set.xlsx"

df = pd.read_excel(input_file)

print("\n================ ORIGINAL DATA ================\n")
print(df.head())

print("\nColumns:")
print(df.columns.tolist())


# ============================================================
# 2. CLEAN COLUMN NAMES
# ============================================================

df.columns = df.columns.str.strip()

print("\n================ CLEANED COLUMNS ================\n")
print(df.columns.tolist())


# ============================================================
# 3. REMOVE PROFIT COLUMN IF IT EXISTS
# ============================================================

if "Profit" in df.columns:
    df = df.drop(columns=["Profit"])

print("\nProfit column removed if it existed.")


# ============================================================
# 4. CHECK MISSING VALUES
# ============================================================

print("\n================ MISSING VALUES ================\n")
print(df.isnull().sum())


# ============================================================
# 5. CHECK DUPLICATE ROWS
# ============================================================

duplicates = df.duplicated().sum()

print("\n================ DUPLICATES ================\n")
print("Number of duplicate rows:", duplicates)

if duplicates > 0:
    df = df.drop_duplicates()


# ============================================================
# 6. CORRECT AND CONVERT DATE VALUES
# ============================================================

df["Date"] = df["Date"].astype(str)

# Correct incorrect year 5025 to 2025 if present
df["Date"] = df["Date"].str.replace(
    "5025",
    "2025",
    regex=False
)

# IMPORTANT:
# Excel dates are already YYYY-MM-DD.
# Do NOT use dayfirst=True.

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

print("\n================ DATE CHECK ================\n")
print(df["Date"].head())

print("\nNumber of invalid dates:",
      df["Date"].isna().sum())


# ============================================================
# 7. CHECK TREATMENT VALUES
# ============================================================

print("\n================ TREATMENT VALUES ================\n")
print(df["Treatment"].value_counts())


# ============================================================
# 8. CONVERT TIME TAKEN INTO HOURS
# ============================================================

df["Time_Hours"] = (
    df["Time Taken"]
    .astype(str)
    .str.extract(r"(\d+\.?\d*)")[0]
    .astype(float)
)

print("\n================ TIME CHECK ================\n")
print(df[["Time Taken", "Time_Hours"]].head())


# ============================================================
# 9. BASIC DATA INFORMATION
# ============================================================

print("\n================ DATA INFORMATION ================\n")

print("Number of records:", len(df))
print("Number of columns:", len(df.columns))

print("\nData types:")
print(df.dtypes)


# ============================================================
# 10. OVERALL TOTALS
# ============================================================

total_latex = df["Latex"].sum()
total_revenue = df["Income"].sum()
total_expense = df["Expense"].sum()
total_working_days = len(df)
total_working_hours = df["Time_Hours"].sum()

print("\n================ OVERALL TOTALS ================\n")

print("Total Latex:", total_latex, "kg")
print("Total Revenue: ₹", total_revenue)
print("Total Recorded Tapping Expense: ₹", total_expense)
print("Total Working Days:", total_working_days)
print("Total Working Hours:", total_working_hours)


# ============================================================
# 11. CALCULATE TAPPING GAP
# ============================================================

df = df.sort_values(
    ["Plantation", "Date"]
)

df["Tapping_Gap_Days"] = (
    df.groupby("Plantation")["Date"]
    .diff()
    .dt.days
)

print("\n================ TAPPING GAP ================\n")

print(
    df[
        [
            "Plantation",
            "Date",
            "Tapping_Gap_Days"
        ]
    ].head(20)
)


# ============================================================
# 12. PLANTATION SUMMARY
# ============================================================

summary = df.groupby("Plantation").agg(

    Working_Days=("Date", "count"),

    Total_Latex=("Latex", "sum"),

    Total_Revenue=("Income", "sum"),

    Recorded_Tapping_Expense=("Expense", "sum"),

    Total_Working_Hours=("Time_Hours", "sum"),

    Average_Time_Hours=("Time_Hours", "mean"),

    Average_Bark=("Bark", "mean"),

    Total_Bark=("Bark", "sum"),

    Average_Tapping_Gap=("Tapping_Gap_Days", "mean")

)


# ============================================================
# 13. CALCULATED METRICS
# ============================================================

summary["Latex_per_Day"] = (
    summary["Total_Latex"] /
    summary["Working_Days"]
)

summary["Revenue_per_Day"] = (
    summary["Total_Revenue"] /
    summary["Working_Days"]
)

summary["Expense_per_Day"] = (
    summary["Recorded_Tapping_Expense"] /
    summary["Working_Days"]
)

summary["Latex_per_Hour"] = (
    summary["Total_Latex"] /
    summary["Total_Working_Hours"]
)

summary["Revenue_per_Hour"] = (
    summary["Total_Revenue"] /
    summary["Total_Working_Hours"]
)

# Study period = 4 months
summary["Average_Working_Days_per_Month"] = (
    summary["Working_Days"] / 4
)


# ============================================================
# 14. ADD STRATEGY NAME
# ============================================================

summary["Strategy"] = summary.index.map({
    1: "With Medicine",
    2: "Without Medicine"
})


# ============================================================
# 15. REORDER COLUMNS
# ============================================================

summary = summary[
    [
        "Strategy",
        "Working_Days",
        "Average_Working_Days_per_Month",
        "Total_Latex",
        "Latex_per_Day",
        "Total_Revenue",
        "Revenue_per_Day",
        "Recorded_Tapping_Expense",
        "Expense_per_Day",
        "Average_Time_Hours",
        "Total_Working_Hours",
        "Latex_per_Hour",
        "Revenue_per_Hour",
        "Average_Bark",
        "Total_Bark",
        "Average_Tapping_Gap"
    ]
]


# ============================================================
# 16. DISPLAY PLANTATION SUMMARY
# ============================================================

print("\n================ PLANTATION SUMMARY ================\n")
print(summary)


# ============================================================
# 17. STRATEGY COMPARISON
# ============================================================

comparison = df.groupby("Treatment").agg(

    Total_Latex=("Latex", "sum"),

    Total_Revenue=("Income", "sum"),

    Recorded_Tapping_Expense=("Expense", "sum"),

    Working_Days=("Date", "count"),

    Total_Working_Hours=("Time_Hours", "sum"),

    Average_Time_Hours=("Time_Hours", "mean"),

    Average_Bark=("Bark", "mean"),

    Total_Bark=("Bark", "sum"),

    Average_Tapping_Gap=("Tapping_Gap_Days", "mean")

)


# ============================================================
# 18. CALCULATE STRATEGY METRICS
# ============================================================

comparison["Latex_per_Day"] = (
    comparison["Total_Latex"] /
    comparison["Working_Days"]
)

comparison["Revenue_per_Day"] = (
    comparison["Total_Revenue"] /
    comparison["Working_Days"]
)

comparison["Latex_per_Hour"] = (
    comparison["Total_Latex"] /
    comparison["Total_Working_Hours"]
)

comparison["Revenue_per_Hour"] = (
    comparison["Total_Revenue"] /
    comparison["Total_Working_Hours"]
)


# ============================================================
# 19. RENAME TREATMENT VALUES
# ============================================================

comparison.index = comparison.index.map({
    1: "With Medicine",
    0: "Without Medicine"
})


# ============================================================
# 20. DISPLAY STRATEGY COMPARISON
# ============================================================

print("\n================ STRATEGY COMPARISON ================\n")
print(comparison)


# ============================================================
# 21. RULE-BASED STRATEGY SCORING
# ============================================================

comparison["Score"] = 0


# Higher total latex
winner = comparison["Total_Latex"].idxmax()
comparison.loc[winner, "Score"] += 1


# Higher total revenue
winner = comparison["Total_Revenue"].idxmax()
comparison.loc[winner, "Score"] += 1


# Higher revenue per day
winner = comparison["Revenue_per_Day"].idxmax()
comparison.loc[winner, "Score"] += 1


# Higher latex per day
winner = comparison["Latex_per_Day"].idxmax()
comparison.loc[winner, "Score"] += 1


# Lower working days
winner = comparison["Working_Days"].idxmin()
comparison.loc[winner, "Score"] += 1


# Higher revenue per hour
winner = comparison["Revenue_per_Hour"].idxmax()
comparison.loc[winner, "Score"] += 1


# Lower bark consumption
winner = comparison["Total_Bark"].idxmin()
comparison.loc[winner, "Score"] += 1


# ============================================================
# 22. FINAL RECOMMENDATION
# ============================================================

recommendation = comparison["Score"].idxmax()

print("\n================ FINAL RECOMMENDATION ================\n")

print("Recommended Strategy:", recommendation)

print("\nScore:")
print(comparison["Score"])


# ============================================================
# 23. IMPORTANT DIFFERENCES
# ============================================================

with_medicine = comparison.loc["With Medicine"]

without_medicine = comparison.loc["Without Medicine"]


latex_difference = (
    with_medicine["Total_Latex"]
    - without_medicine["Total_Latex"]
)


revenue_difference = (
    with_medicine["Total_Revenue"]
    - without_medicine["Total_Revenue"]
)


working_day_difference = (
    without_medicine["Working_Days"]
    - with_medicine["Working_Days"]
)


revenue_day_difference = (
    with_medicine["Revenue_per_Day"]
    - without_medicine["Revenue_per_Day"]
)


working_hour_difference = (
    without_medicine["Total_Working_Hours"]
    - with_medicine["Total_Working_Hours"]
)


bark_difference = (
    without_medicine["Total_Bark"]
    - with_medicine["Total_Bark"]
)


revenue_hour_difference = (
    with_medicine["Revenue_per_Hour"]
    - without_medicine["Revenue_per_Hour"]
)


gap_difference = (
    with_medicine["Average_Tapping_Gap"]
    - without_medicine["Average_Tapping_Gap"]
)


print("\n================ KEY DIFFERENCES ================\n")

print(
    "Additional Latex with Medicine:",
    latex_difference,
    "kg"
)

print(
    "Additional Revenue with Medicine: ₹",
    revenue_difference
)

print(
    "Fewer Working Days with Medicine:",
    working_day_difference
)

print(
    "Revenue per Day Advantage: ₹",
    revenue_day_difference
)

print(
    "Fewer Total Working Hours:",
    working_hour_difference
)

print(
    "Lower Bark Consumption:",
    bark_difference,
    "cm"
)

print(
    "Revenue per Hour Advantage: ₹",
    revenue_hour_difference
)

print(
    "Average Tapping Gap Advantage:",
    gap_difference,
    "days"
)


# ============================================================
# 24. BARK CONSUMPTION REDUCTION
# ============================================================

bark_reduction_percentage = (
    bark_difference /
    without_medicine["Total_Bark"]
) * 100

print(
    "\nBark Consumption Reduction:",
    round(bark_reduction_percentage, 2),
    "%"
)


# ============================================================
# 25. CREATE GRAPHS
# ============================================================

strategies = comparison.index


# ------------------------------------------------------------
# GRAPH 1: WORKING DAYS
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    strategies,
    comparison["Working_Days"]
)

plt.title("Working / Tapping Days")
plt.xlabel("Strategy")
plt.ylabel("Number of Days")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# GRAPH 2: TOTAL LATEX
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    strategies,
    comparison["Total_Latex"]
)

plt.title("Total Latex Production")
plt.xlabel("Strategy")
plt.ylabel("Latex (kg)")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# GRAPH 3: TOTAL REVENUE
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    strategies,
    comparison["Total_Revenue"]
)

plt.title("Total Revenue")
plt.xlabel("Strategy")
plt.ylabel("Revenue (₹)")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# GRAPH 4: REVENUE PER WORKING DAY
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    strategies,
    comparison["Revenue_per_Day"]
)

plt.title("Revenue per Working Day")
plt.xlabel("Strategy")
plt.ylabel("Revenue per Day (₹)")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# GRAPH 5: LATEX PER WORKING DAY
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    strategies,
    comparison["Latex_per_Day"]
)

plt.title("Latex per Working Day")
plt.xlabel("Strategy")
plt.ylabel("Latex per Day (kg)")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# GRAPH 6: REVENUE PER WORKING HOUR
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    strategies,
    comparison["Revenue_per_Hour"]
)

plt.title("Revenue per Working Hour")
plt.xlabel("Strategy")
plt.ylabel("Revenue per Hour (₹)")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# GRAPH 7: TOTAL BARK CONSUMPTION
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    strategies,
    comparison["Total_Bark"]
)

plt.title("Total Recorded Bark Consumption")
plt.xlabel("Strategy")
plt.ylabel("Bark (cm)")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# GRAPH 8: AVERAGE TAPPING GAP
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    strategies,
    comparison["Average_Tapping_Gap"]
)

plt.title("Average Tapping Gap")
plt.xlabel("Strategy")
plt.ylabel("Gap (Days)")

plt.tight_layout()
plt.show()


# ============================================================
# 26. SAVE FINAL EXCEL FILE
# ============================================================

output_file = r"C:\Users\shebi\Downloads\rubber_analysis_summary.xlsx"

with pd.ExcelWriter(
    output_file,
    engine="openpyxl"
) as writer:

    # Cleaned Data
    df.to_excel(
        writer,
        sheet_name="Cleaned Data",
        index=False
    )

    # Plantation Summary
    summary.to_excel(
        writer,
        sheet_name="Plantation Summary"
    )

    # Strategy Comparison
    comparison.to_excel(
        writer,
        sheet_name="Strategy Comparison"
    )


# ============================================================
# 27. FINAL OUTPUT MESSAGE
# ============================================================

print("\n===================================================")
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("===================================================")

print("\nRecommended Strategy:")
print(recommendation)

print("\nFinal Excel file:")
print(output_file)

print("\nSheets created:")
print("1. Cleaned Data")
print("2. Plantation Summary")
print("3. Strategy Comparison")

print("\n===================================================")
