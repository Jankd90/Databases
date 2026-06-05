# Tutorial 3: Climate Analysis with SQLite

**Tool:** DB Browser for SQLite

**Goal:** Use the climate readings from Tutorial 2 to build useful weather-station or smart-home indoor climate analysis.

## Step 1: Continue With the Same Database

Open `climate_station.db` from Tutorial 2.

Run:

```sql
PRAGMA foreign_keys = ON;
```

If your database only contains a few live ESP readings, add extra rows with `../02_sql_real_work/sample_data_starter.sql` so your analysis has enough variation.

## Step 2: Add Analysis Tables

Copy `analysis_schema_starter.sql` to your own work file and complete the TODO sections.

The starter schema adds:

1. A location hierarchy for smart-home or weather-station structure.
2. alert rules that define comfort or safety thresholds.
3. alert events generated from readings.

## Step 3: Query Location Hierarchies

Copy `recursive_queries_starter.sql` to your own work file.

Complete recursive CTE queries for questions such as:

1. Which rooms belong to a floor or building?
2. Which readings were captured below a chosen location in the hierarchy?
3. Which locations have active alerts?

## Step 4: Analyze Climate Patterns

Copy `climate_analysis_queries_starter.sql` to your own work file.

Complete SQL queries for questions such as:

1. Which locations are outside the comfort profile most often?
2. Which time of day has the highest humidity?
3. Is pressure rising or falling?
4. Which rooms have similar climate behavior?

## Deliverables

- Completed analysis schema
- At least one location hierarchy
- At least three recursive CTE queries
- At least four climate analysis queries
- Short explanation of what the data says about the weather station or smart-home indoor climate
