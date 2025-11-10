# Chapter 9 — SQL

---

## Preparation

In order to **benefit as much as possible** from the limited time, be sure that you are **well prepared**.  
It can be believed that **proper preparation and attendance** are key.  
The **impact of a minor mistake** may be **disastrous**.  
We think that **a lot of practice** will help you **prevent mistakes**.

---

## Introduction to SQL

**SQL** was developed to have a **computer language** for **data retrieval** from large databases — much like **plain English**.  
The commands that make up the language are some sort of **structured English**.

> **Warning:**  
> Do **not underestimate** the impact of the commands.  
> They are **very powerful**, and mistakes may lead to a **wrong use of this power**, resulting in **minor or major disasters**.  
> These disasters **do not harm the computer** but will **annoy you** as they are **time-consuming**.

SQL can be used to **create databases** and **fill them with values**.  
We **won’t do this**.  
Our focus will be on **retrieving information**.  
The **key command** to do this is:

> ```sql
> SELECT
> ```

---

## Basic Structure of the `SELECT` Command

```sql
SELECT  <fields/expression>
FROM    <table(s)>
WHERE   <condition(s)>;
````

|Clause|Purpose|
|---|---|
|SELECT|List of **field names** (or one field) to display|
|FROM|**Table name(s)** involved|
|WHERE|**Condition(s)** — only matching rows are returned|

> **Note:** All SQL commands **end with a semicolon ;** If **no WHERE**, all records are selected A real-life table may have **thousands of records**

> **Rule of Thumb:** SELECT → **column selection** WHERE → **row selection**

---

## Examples

### Example 1 — Single Field, Single Row

sql

```
SELECT name
FROM   artists
WHERE  artist_no = 41;
```

### Sample ARTISTS Table

|ARTIST_NO|NAME|COUNTRY|
|---|---|---|
|1|Bobby Vinton|USA|
|2|The Kingsmen|USA|
|...|...|...|
|40|The Reflections|USA|
|**41**|**Peter & Gordon**|**UK**|
|42|Billy J. Kramer|UK|
|43|Barbra Streisand|USA|
|...|...|...|

**Result:**

text

```
NAME
Peter & Gordon
```

---

### Example 2 — All Fields (*)

sql

```
SELECT *
FROM   artists
WHERE  artist_no = 41;
```

**Result:**

|ARTIST_NO|NAME|COUNTRY|
|---|---|---|
|41|Peter & Gordon|UK|

---

### Example 3 — Multiple Rows

sql

```
SELECT name
FROM   artists
WHERE  country = 'UK';
```

**Result:** List of **all UK artists**

> **Note:** Alphanumeric values in **single quotes**: 'UK'

---

### Example 4 — No WHERE Clause

sql

```
SELECT country
FROM artists;
```

**Result:** Complete list of **all countries**

Try this in the seminar:

sql

```
SELECT DISTINCT country
FROM artists;
```

> **Spot the difference!** DISTINCT removes **duplicates**

---

## Finding Peter & Gordon’s Hits

We want the **title(s)** of **Peter & Gordon** in 1964.

### Step 1 — Find artist_no

sql

```
SELECT artist_no
FROM   artists
WHERE  name = 'Peter & Gordon';
```

**Result:** 41

---

### Sample RECORDS Table

|RECORD_NO|TITLE|ARTIST_NO|REC_CO|
|---|---|---|---|
|...|...|...|...|
|45|Love Me Do|15|26|
|50|**A World Without Love**|**41**|19|
|51|Little Children|42|36|
|...|...|...|...|

---

### Step 2 — Find Titles

sql

```
SELECT title
FROM   records
WHERE  artist_no = 41;
```

**Result:**

text

```
TITLE
A World Without Love
```

---

## Nested Commands (Subqueries)

Instead of manually copying 41, **nest** the query:

sql

```
SELECT title
FROM   records
WHERE  artist_no = (
    SELECT artist_no
    FROM   artists
    WHERE  name = 'Peter & Gordon'
);
```

> The inner query returns 41 → used in the outer query

---

## Using LIKE for Partial Matches

Not sure about spelling?

sql

```
SELECT artist_no
FROM   artists
WHERE  name LIKE '*gordon*';
```

> * = wildcard (any characters)

---

## When = Fails → Use IN

sql

```
SELECT title
FROM   records
WHERE  artist_no = (
    SELECT artist_no
    FROM   artists
    WHERE  name LIKE '*gordon*'
);
```

> **Problem:** Multiple artists may match → = fails

**Solution:** Use IN

sql

```
SELECT title
FROM   records
WHERE  artist_no IN (
    SELECT artist_no
    FROM   artists
    WHERE  name LIKE '*gordon*'
);
```

> IN works with **one or many** values **Always safe** when in doubt

---

## The CHARTS Table

|WEEK|RECORD_NO|POSITION|
|---|---|---|
|13|26|4|
|14|26|5|
|15|26|9|
|9|27|9|
|10|27|8|
|...|...|...|

- **520 records** total (52 weeks × 10)
- Record 27:
    - Week 9 → Position **9**
    - Week 10 → Position **8**

---

## Why No “Last Week’s Position” Field?

> **Not stored** — can be **calculated**!

**Example:** Current week = **10** Want **last week’s position** of record 27?

sql

```
SELECT position
FROM   charts
WHERE  week = 9
  AND  record_no = 27;
```

**Result:** 9

> **Rule of Thumb:** _Don’t store what you can **look up** or **compute**._

---

## Summary

> ✅ **SQL SELECT Structure**
> 
> sql
> 
> ```
> SELECT <columns>
> FROM   <tables>
> WHERE  <conditions>;
> ```

> ✅ **Key Techniques**
> 
> - * → all fields
> - DISTINCT → no duplicates
> - LIKE '*pattern*' → partial match
> - **Subqueries** with = or IN
> - **No redundancy** — compute derived data

> **Practice Tip:** _Write small queries first → combine with subqueries → avoid manual lookup._