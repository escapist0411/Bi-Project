# Power BI DAX Formulas 

Here are some helpful DAX (Data Analysis Expressions) formulas you can use to build your Job Market Demand Analysis Dashboard based on the dataset we mocked.

### 1. Total Job Openings
Identify the total volume of opportunities in your dataset.
```dax
Total Jobs = COUNTROWS('dataset')
```

### 2. Average Salary
Calculate the average salary across the board.
```dax
Average Salary = AVERAGE('dataset'[Salary])
```

### 3. High Demand Roles Flag
Create a calculated column that flags whether a job is high demand (e.g., if it appears frequently). You can adjust the threshold dynamically.
```dax
High Demand Flag = 
VAR RoleCount = CALCULATE(COUNT('dataset'[Job Title]), ALLEXCEPT('dataset', 'dataset'[Job Title]))
RETURN IF(RoleCount > 15, "High Demand", "Normal Demand")
```

### 4. Average Experience Required
Use this as a KPI card metric.
```dax
Avg Experience % = AVERAGE('dataset'[Experience Level])
```

### 5. Salary by Location (Measure)
Calculate total or average salary dynamically based on location filter context.
```dax
Avg Salary By Location = CALCULATE(AVERAGE('dataset'[Salary]), ALLEXCEPT('dataset', 'dataset'[Location]))
```

### 6. Senior Level Opportunities Count
Assuming an Experience Level > 80% represents "Senior".
```dax
Senior Level Jobs = CALCULATE(COUNTROWS('dataset'), 'dataset'[Experience Level] >= 80)
```

## How to use these in Power BI:
1. Open **Power BI Desktop** and load your `dataset.csv`.
2. Go to the **Modeling** tab at the top.
3. Click **New Measure** for aggregated numbers (like averages and totals) or **New Column** for row-by-row calculations (like the High Demand Flag).
4. Paste the scripts directly into the formula bar.
