import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# 1. LOAD EXCEL FILE
# =========================================================

data = pd.read_excel(
    "C:/Users/shebi/Downloads/rubber data set.xlsx"
)

print("\nFIRST 5 ROWS:")
print(data.head())


# =========================================================
# 2. CLEAN COLUMN NAMES
# =========================================================

data.columns = data.columns.str.strip()

print("\nCOLUMN NAMES:")
print(data.columns.tolist())


# =========================================================
# 3. CHECK MISSING VALUES
# =========================================================

print("\nMISSING VALUES:")
print(data.isnull().sum())

print("\nDUPLICATE ROWS:")
print(data.duplicated().sum())

# Remove duplicate rows
data = data.drop_duplicates()


# =========================================================
# 4. CLEAN DATE
# =========================================================

# Correct wrong year 5025 → 2025
data["Date"] = (
    data["Date"]
    .astype(str)
    .str.replace("5025", "2025", regex=False)
)

# Convert to date
data["Date"] = pd.to_datetime(
    data["Date"],
    errors="coerce"
)

print("\nINVALID DATES:")
print(data[data["Date"].isna()])


# =========================================================
# 5. CHECK TREATMENT VALUES
# =========================================================

print("\nTREATMENT VALUES:")
print(data["Treatment"].value_counts())


# =========================================================
# 6. CHECK ORIGINAL DATA
# =========================================================

print("\nINCOME AND PROFIT CHECK:")
print(
    data[
        ["Latex", "Income", "Expense", "Profit"]
    ].head()
)


# =========================================================
# 7. WORKING DAYS
# =========================================================

working_days = data.groupby(
    "Plantation"
)["Date"].nunique()

print("\nWORKING DAYS:")
print(working_days)


# =========================================================
# 8. TOTAL LATEX
# =========================================================

total_latex = data.groupby(
    "Plantation"
)["Latex"].sum()

print("\nTOTAL LATEX:")
print(total_latex)


# =========================================================
# 9. TOTAL INCOME
# =========================================================

total_income = data.groupby(
    "Plantation"
)["Income"].sum()

print("\nTOTAL INCOME:")
print(total_income)


# =========================================================
# 10. TOTAL EXPENSE
# =========================================================

total_expense = data.groupby(
    "Plantation"
)["Expense"].sum()

print("\nTOTAL EXPENSE:")
print(total_expense)


# =========================================================
# 11. TOTAL PROFIT
# =========================================================

total_profit = data.groupby(
    "Plantation"
)["Profit"].sum()

print("\nTOTAL PROFIT:")
print(total_profit)


# =========================================================
# 12. LATEX PER DAY
# =========================================================

latex_per_day = (
    total_latex / working_days
)

print("\nLATEX PER WORKING DAY:")
print(latex_per_day)


# =========================================================
# 13. INCOME PER DAY
# =========================================================

income_per_day = (
    total_income / working_days
)

print("\nINCOME PER WORKING DAY:")
print(income_per_day)


# =========================================================
# 14. EXPENSE PER DAY
# =========================================================

expense_per_day = (
    total_expense / working_days
)

print("\nEXPENSE PER WORKING DAY:")
print(expense_per_day)


# =========================================================
# 15. PROFIT PER DAY
# =========================================================

profit_per_day = (
    total_profit / working_days
)

print("\nPROFIT PER WORKING DAY:")
print(profit_per_day)


# =========================================================
# 16. CONVERT TIME TAKEN INTO HOURS
# =========================================================

data["Time_Hours"] = (
    data["Time Taken"]
    .astype(str)
    .str.replace("h", "", regex=False)
    .str.strip()
)

data["Time_Hours"] = pd.to_numeric(
    data["Time_Hours"],
    errors="coerce"
)

print("\nTIME VALUES:")
print(data["Time_Hours"].value_counts())


# =========================================================
# 17. AVERAGE TIME
# =========================================================

average_time = data.groupby(
    "Plantation"
)["Time_Hours"].mean()

print("\nAVERAGE TIME PER DAY:")
print(average_time)


# =========================================================
# 18. TOTAL WORKING HOURS
# =========================================================

total_working_hours = (
    working_days * average_time
)

print("\nTOTAL WORKING HOURS:")
print(total_working_hours)


# =========================================================
# 19. BARK CONSUMPTION
# =========================================================

average_bark = data.groupby(
    "Plantation"
)["Bark"].mean()

total_bark = data.groupby(
    "Plantation"
)["Bark"].sum()

print("\nAVERAGE BARK:")
print(average_bark)

print("\nTOTAL BARK:")
print(total_bark)


# =========================================================
# 20. LATEX PER HOUR
# =========================================================

latex_per_hour = (
    total_latex / total_working_hours
)

print("\nLATEX PER HOUR:")
print(latex_per_hour)


# =========================================================
# 21. PROFIT PER HOUR
# =========================================================

profit_per_hour = (
    total_profit / total_working_hours
)

print("\nPROFIT PER HOUR:")
print(profit_per_hour)


# =========================================================
# 22. CREATE FINAL PLANTATION SUMMARY
# =========================================================

summary = pd.DataFrame({

    "Working Days": working_days,

    "Total Latex (kg)": total_latex,

    "Latex per Day (kg)": latex_per_day,

    "Total Income (Rs)": total_income,

    "Total Expense (Rs)": total_expense,

    "Total Profit (Rs)": total_profit,

    "Income per Day (Rs)": income_per_day,

    "Expense per Day (Rs)": expense_per_day,

    "Profit per Day (Rs)": profit_per_day,

    "Average Time (hours)": average_time,

    "Total Working Hours": total_working_hours,

    "Latex per Hour (kg)": latex_per_hour,

    "Profit per Hour (Rs)": profit_per_hour,

    "Average Bark (cm)": average_bark,

    "Total Bark (cm)": total_bark
})


# =========================================================
# 23. DISPLAY PLANTATION SUMMARY
# =========================================================

print("\n")
print("======================================================")
print("              PLANTATION SUMMARY")
print("======================================================")

print(summary.round(2))


# =========================================================
# 24. STRATEGY COMPARISON
# =========================================================

strategy = data.groupby("Treatment").agg({

    "Latex": "sum",

    "Income": "sum",

    "Expense": "sum",

    "Profit": "sum",

    "Date": "nunique",

    "Time_Hours": "sum",

    "Bark": "sum"
})


# Rename columns
strategy = strategy.rename(columns={

    "Latex": "Total Latex",

    "Income": "Total Income",

    "Expense": "Total Expense",

    "Profit": "Total Profit",

    "Date": "Working Days",

    "Time_Hours": "Total Working Hours",

    "Bark": "Total Bark"
})


# =========================================================
# 25. STRATEGY NAMES
# =========================================================

strategy["Strategy"] = strategy.index.map({

    1: "With Medicine",

    0: "Without Medicine"

})


# =========================================================
# 26. CALCULATE STRATEGY PERFORMANCE
# =========================================================

strategy["Latex per Day"] = (

    strategy["Total Latex"] /

    strategy["Working Days"]

)


strategy["Income per Day"] = (

    strategy["Total Income"] /

    strategy["Working Days"]

)


strategy["Expense per Day"] = (

    strategy["Total Expense"] /

    strategy["Working Days"]

)


strategy["Profit per Day"] = (

    strategy["Total Profit"] /

    strategy["Working Days"]

)


strategy["Latex per Hour"] = (

    strategy["Total Latex"] /

    strategy["Total Working Hours"]

)


strategy["Profit per Hour"] = (

    strategy["Total Profit"] /

    strategy["Total Working Hours"]

)


# =========================================================
# 27. DISPLAY STRATEGY COMPARISON
# =========================================================

print("\n")
print("======================================================")
print("             TAPPING STRATEGY COMPARISON")
print("======================================================")

print(

    strategy[
        [
            "Strategy",
            "Working Days",
            "Total Latex",
            "Total Income",
            "Total Expense",
            "Total Profit",
            "Latex per Day",
            "Profit per Day",
            "Total Working Hours",
            "Latex per Hour",
            "Profit per Hour",
            "Total Bark"
        ]
    ].round(2)

)


# =========================================================
# 28. FIND BEST STRATEGY
# =========================================================

strategy["Score"] = 0


# Highest total latex
strategy.loc[
    strategy["Total Latex"].idxmax(),
    "Score"
] += 1


# Highest total profit
strategy.loc[
    strategy["Total Profit"].idxmax(),
    "Score"
] += 1


# Highest profit per day
strategy.loc[
    strategy["Profit per Day"].idxmax(),
    "Score"
] += 1


# Highest latex per day
strategy.loc[
    strategy["Latex per Day"].idxmax(),
    "Score"
] += 1


# Lowest working days
strategy.loc[
    strategy["Working Days"].idxmin(),
    "Score"
] += 1


# Highest profit per hour
strategy.loc[
    strategy["Profit per Hour"].idxmax(),
    "Score"
] += 1


# Lowest bark consumption
strategy.loc[
    strategy["Total Bark"].idxmin(),
    "Score"
] += 1


# =========================================================
# 29. BEST STRATEGY
# =========================================================

best_treatment = strategy["Score"].idxmax()

best_strategy = strategy.loc[
    best_treatment,
    "Strategy"
]


print("\n")
print("======================================================")
print("              OPTIMIZATION RESULT")
print("======================================================")

print(
    "\nRecommended Tapping Strategy:"
)

print(
    ">>>", best_strategy
)


print("\nStrategy Scores:")

print(

    strategy[
        ["Strategy", "Score"]
    ]

)


# =========================================================
# 30. SAVE COMPLETE ANALYSIS
# =========================================================

output_file = (
    "C:/Users/shebi/Downloads/"
    "rubber_analysis_summary.xlsx"
)


with pd.ExcelWriter(output_file) as writer:

    summary.to_excel(
        writer,
        sheet_name="Plantation Summary"
    )

    strategy.to_excel(
        writer,
        sheet_name="Strategy Comparison"
    )

    data.to_excel(
        writer,
        sheet_name="Cleaned Data",
        index=False
    )


print("\n")
print("======================================================")
print("       ANALYSIS FILE SAVED SUCCESSFULLY")
print("======================================================")

print(output_file)


# =========================================================
# 31. GRAPH 1 - WORKING DAYS
# =========================================================

working_days.plot(
    kind="bar"
)

plt.title(
    "Working Days Comparison"
)

plt.xlabel(
    "Plantation"
)

plt.ylabel(
    "Number of Days"
)

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()


# =========================================================
# 32. GRAPH 2 - TOTAL LATEX
# =========================================================

total_latex.plot(
    kind="bar"
)

plt.title(
    "Total Latex Production"
)

plt.xlabel(
    "Plantation"
)

plt.ylabel(
    "Latex (kg)"
)

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()


# =========================================================
# 33. GRAPH 3 - TOTAL INCOME
# =========================================================

total_income.plot(
    kind="bar"
)

plt.title(
    "Total Income Comparison"
)

plt.xlabel(
    "Plantation"
)

plt.ylabel(
    "Income (Rs)"
)

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()


# =========================================================
# 34. GRAPH 4 - TOTAL PROFIT
# =========================================================

total_profit.plot(
    kind="bar"
)

plt.title(
    "Total Profit Comparison"
)

plt.xlabel(
    "Plantation"
)

plt.ylabel(
    "Profit (Rs)"
)

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()


# =========================================================
# 35. GRAPH 5 - PROFIT PER DAY
# =========================================================

profit_per_day.plot(
    kind="bar"
)

plt.title(
    "Profit per Working Day"
)

plt.xlabel(
    "Plantation"
)

plt.ylabel(
    "Profit per Day (Rs)"
)

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()


# =========================================================
# 36. GRAPH 6 - LATEX PER DAY
# =========================================================

latex_per_day.plot(
    kind="bar"
)

plt.title(
    "Latex Production per Working Day"
)

plt.xlabel(
    "Plantation"
)

plt.ylabel(
    "Latex per Day (kg)"
)

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()


# =========================================================
# 37. GRAPH 7 - PROFIT PER HOUR
# =========================================================

profit_per_hour.plot(
    kind="bar"
)

plt.title(
    "Profit per Working Hour"
)

plt.xlabel(
    "Plantation"
)

plt.ylabel(
    "Profit per Hour (Rs)"
)

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()


# =========================================================
# 38. FINAL MESSAGE
# =========================================================

print("\n")
print("======================================================")
print("             ANALYSIS COMPLETED")
print("======================================================")

print(
    "\nBest-performing strategy:",
    best_strategy
)

print(
    "\nNote: The recommendation is based on the "
    "observed dataset."
)