# Chapter 11 — Functions

---

## AGGREGATE FUNCTIONS

SQL provides **aggregate functions** — they **summarize** many values into **one**.

| Function | Purpose |
|---------|--------|
| `COUNT()` | Number of rows |
| `SUM()`   | Total of values |
| `AVG()`   | Average |
| `MIN()`   | Lowest value |
| `MAX()`   | Highest value |

> **Syntax:**  
> ```sql
> <function>(field_name)
> ```

---

## AGGREGATE FUNCTION ON ITS OWN

Used **alone** after `SELECT` — returns **one value**.

### Example 1 — Debut Week

```sql
SELECT MIN(week)
FROM   charts
WHERE  record_no = 50;
````

> **Result:** Debut week of record 50 (Lowest week it appeared in Top 10)

---

### Example 2 — Number of Hits


```sql
SELECT COUNT(record_no)
FROM   records
WHERE  artist_no = 15;
```

> **Result:** Number of Beatles hits (artist 15)

---

## AGGREGATE FUNCTIONS WITH A FIELD

You want the **group** (e.g., country) **and** the **summary**.

### Example — Artists per Country

```sql
SELECT country, COUNT(artist_no)
FROM   artists
GROUP BY country;
```

> **Rule:** In SELECT, only:
> 
> - The **grouping field** (country)
> - **Aggregate functions**

---

### Example — Records per Record Company

```sql
SELECT rec_co, COUNT(record_no)
FROM   records
GROUP BY rec_co;
```

---

## SORTING — ORDER BY

Sorts the **final result** Placed at the **end** of the command


```sql
SELECT week, position
FROM   charts
WHERE  record_no = 50
ORDER BY position;
```

> **Note:** Tables in relational databases are **not sorted** ORDER BY does **not require** the field to be in SELECT

```sql
-- Valid: sort by week, show only position
SELECT position
FROM   charts
WHERE  record_no = 50
ORDER BY week;
```

> Add DESC for **descending** order

---

## LINKING FILES (JOIN)

Files are related → **link** them using **matching fields**

### Syntax

```sql
SELECT ...
FROM   table1, table2
WHERE  table1.field = table2.field;
```

---

### Example — Titles + Artist Names (Capitol Records)

```sql
SELECT title, name
FROM   records, artists
WHERE  records.artist_no = artists.artist_no
  AND  rec_co = 19;
```

> **Critical:**
> 
> - List **all tables** after FROM
> - **Prefix ambiguous fields** with table name
> - **Missing link** → **Cartesian product** (all vs all = disaster!)

---

## LINKS IN TOP10USA

```text
artists.artist_no  = records.artist_no
records.rec_co     = rec_comp.rec_co
charts.record_no   = records.record_no
```

---

## Questions 2

### a. Records in **week 20**

```sql
SELECT record_no
FROM   charts
WHERE  week = 20;
```

---

### b. Include **positions**

```sql
SELECT record_no, position
FROM   charts
WHERE  week = 20;
```

---

### c. **Order by position**

```sql
SELECT record_no, position
FROM   charts
WHERE  week = 20
ORDER BY position;
```

> This is the **Top 10 for week 20**

---

### d. Include **titles**

```sql
SELECT records.record_no, position, title
FROM   charts, records
WHERE  charts.record_no = records.record_no
  AND  week = 20
ORDER BY position;
```

---

### e. Include **artist names** and **record company**


```sql
SELECT 
  position, title, name, rec_comp.name AS company
FROM   
  charts, records, artists, rec_comp
WHERE  
  charts.record_no = records.record_no
  AND records.artist_no = artists.artist_no
  AND records.rec_co = rec_comp.rec_co
  AND week = 20
ORDER BY position;
```

> **Full hitparade!**

---

### f. **Debut week** per record


```sql
SELECT record_no, MIN(week) AS debut_week
FROM   charts
GROUP BY record_no;
```

---

### g. **No.1 hits** of The Beatles (artist_no = 15)

```sql
-- Step 1: Beatles records
SELECT record_no
FROM   records
WHERE  artist_no = 15;

-- Step 2: Filter for position = 1
SELECT title
FROM   records, charts
WHERE  records.record_no = charts.record_no
  AND  artist_no = 15
  AND  position = 1;
```

---

### h. Record companies that released **Beatles** records

```sql
SELECT DISTINCT rec_co
FROM   records
WHERE  artist_no = 15;
```

---

### i. Include **song titles**

```sql
SELECT title, rec_co
FROM   records
WHERE  artist_no = 15;
```

---

## CREATING 'FILES' — SAVE AS

End a query with **Save As…** → creates a **new table**

```sql
SELECT artists.name, records.title
FROM   artists, records
WHERE  artists.artist_no = records.artist_no;

-- File → Save As → 'songs'
```

> New table: SONGS(name, title)

---

### Why Use Files?

- **Avoid GROUP BY restrictions**
- **Break complex problems** into steps
- **Safer** than one giant query

---

### Example — Record Company with Most Hits

#### Step 1 — Count per company

```sql
SELECT rec_co, COUNT(record_no) AS amount
FROM   records
GROUP BY rec_co;

-- Save As → 'mosthits'
```

#### Step 2 — Find max

```sql
SELECT rec_co, amount
FROM   mosthits
WHERE  amount = (SELECT MAX(amount) FROM mosthits);
```

---

## 1. Example

### a. Try the example

```sql
-- Step 1
SELECT rec_co, COUNT(record_no) AS amount
FROM   records
GROUP BY rec_co;
-- Save As → 'mosthits'

-- Step 2
SELECT rec_co, amount
FROM   mosthits
WHERE  amount = (SELECT MAX(amount) FROM mosthits);
```

---

### b. Include **record company name**

```sql
SELECT rec_comp.name, amount
FROM   mosthits, rec_comp
WHERE  mosthits.rec_co = rec_comp.rec_co
  AND  amount = (SELECT MAX(amount) FROM mosthits);
```

---

## Questions 3 — Most Successful Artists

Answer which artist(s) released most records.

> **Hint:** Same pattern as record companies

```sql
-- Step 1: Count records per artist
SELECT artist_no, COUNT(record_no) AS hits
FROM   records
GROUP BY artist_no;
-- Save As → 'artist_hits'

-- Step 2: Find max
SELECT artist_no, hits
FROM   artist_hits
WHERE  hits = (SELECT MAX(hits) FROM artist_hits);

-- Step 3: Include name
SELECT name, hits
FROM   artist_hits, artists
WHERE  artist_hits.artist_no = artists.artist_no
  AND  hits = (SELECT MAX(hits) FROM artist_hits);
```

---

## The Highest Debut Position

### a. List with **debut week**

```sql
SELECT record_no, MIN(week) AS debwk_no
FROM   charts
GROUP BY record_no;
```

---

### b. Exclude **week 1**

```sql
SELECT record_no, MIN(week) AS debwk_no
FROM   charts
WHERE  week > 1
GROUP BY record_no;
```

---

### c. Save as DEB WEEK

```sql
-- Save As → 'debweek' (fields: record_no, debwk_no)
```

---

### d. View file

```sql
SELECT * FROM debweek;
```

> **Meaning:**
> 
> - record_no → song ID
> - debwk_no → first week in charts

---

### e. Add **debut position**

```sql
SELECT 
  debweek.record_no, position AS debpos
FROM   
  debweek, charts
WHERE  
  debweek.record_no = charts.record_no
  AND  debweek.debwk_no = charts.week;
```

---

### f. Save as DEBPOSITION


```sql
-- Save As → 'debposition' (rec_no, debpos)
```

---

### g. Find **highest debut** (lowest position number!)


```sql
SELECT rec_no, debpos
FROM   debposition
WHERE  debpos = (SELECT MIN(debpos) FROM debposition);
```

---

### h. Get **song title**

```sql
SELECT title
FROM   records
WHERE  record_no IN (
    SELECT rec_no
    FROM   debposition
    WHERE  debpos = (SELECT MIN(debpos) FROM debposition)
);
```

---

## Questions 4 — Song of the Year 1964

Produce a hitparade of the 'Song of the Year 1964'

> **Scoring:** Position 10 → 1 point Position 9 → 2 points … Position 1 → 10 points

---

### Step 1 — Points per appearance


```sql
SELECT record_no, (11 - position) AS points
FROM   charts;
-- Save As → 'weekly_points'
```

---

### Step 2 — Total points per record

```sql
SELECT record_no, SUM(points) AS total_points
FROM   weekly_points
GROUP BY record_no;
-- Save As → 'year_totals'
```

---

### Step 3 — Final hitparade (descending)

```sql
SELECT 
  title, name, total_points
FROM   
  year_totals, records, artists
WHERE  
  year_totals.record_no = records.record_no
  AND records.artist_no = artists.artist_no
ORDER BY total_points DESC;
```

> **#1 = Song of the Year 1964**

---

## Summary

> **Aggregate Functions** → COUNT, SUM, AVG, MIN, MAX **GROUP BY** → one row per group **ORDER BY** → sort final result **Joins** → link tables with table.field = table.field **SAVE AS** → break complex queries into **safe, reusable steps**

> **Golden Rule:** _One small, correct query at a time → build up to the answer._