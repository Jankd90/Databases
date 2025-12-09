# Chapter 8 — Designing a Database

---

## AMERICAN TOP 10 — January 6, 1965

| TW  | LW  | TITLE                   | ARTISTS                          | RECORD COMPANY |
| --- | --- | ----------------------- | -------------------------------- | -------------- |
| 1   | 1   | I Feel Fine             | The Beatles                      | Capitol        |
| 2   | 2   | Come See About Me       | The Supremes                     | Motown         |
| 3   | 3   | Mr. Lonely              | Bobby Vinton                     | Epic           |
| 4   | 4   | She's a Woman           | The Beatles                      | Capitol        |
| 5   | -   | Love Potion Number Nine | The Searchers                    | Kapp           |
| 6   | 6   | Goin' Out of My Head    | Little Anthony and the Imperials | DCP            |
| 7   | 5   | She's Not There         | The Zombies                      | Parrot         |
| 8   | -   | Amen                    | The Impressions                  | ABC            |
| 9   | 9   | The Jerk                | The Larks                        | Money          |
| 10  | -   | The Wedding             | Julie Rogers                     | Mercury        |

> **TW:** This week's position  
> **LW:** Last week's position

In the above table, you can see the **American Top 10 Hitparade** of the **first week of January 1965**.  
Our workshops will deal with a **database** that contains **all data** on **every US Top 10 of 1964**.

---

## DATABASE STRUCTURE
```

DATABASE └── consists of DATAFILES └── consist of RECORDS └── consist of FIELDS

```
The **datafiles** usually have some **relationship** with each other — that is the reason why they are part of the **same database**.

---

## DESIGN PRINCIPLES

> 🧩 **Principle 1**  
> Create a **separate file** for each **entity type**

> 🧩 **Principle 2**  
> Decide the **primary key**

> 🧩 **Principle 3**  
> Assign each **property** of an entity type to a **field** within the table representing that entity type

---

### Entities

**Entities** are persons, objects, or things that have **properties**, **characteristics**, or **attributes**.

In our example, the entities are:

- **Artists**  
- **Records**  
- **Record Companies**

These are all entities with certain characteristics, like **name**, **title**, **country of origin**, and more.

---

## Applying the Principles

### Principle 1 — Separate Files per Entity

```text
ARTISTS
RECORDS
REC_COMP  (short for Record Companies)
````

### Principle 2 — Primary Keys

A **primary key** is a characteristic of an entity that **uniquely identifies** it — **no two entities** have the same primary key.

Examples from daily life:

- Bank account number
- Telephone number
- Customer number
- Social security number (SoFi number)
- Book’s **ISBN**

> **Not a primary key:** PIN code (only 10,000 combinations — reused across millions of accounts)

In our example: Each **song**, **artist**, and **record company** will be assigned a **unique number** within its file.

### Principle 3 — Properties in the Right Table

|Entity|Properties Stored|
|---|---|
|**Artists**|name, country|
|**Records**|title|
|**Rec. Co.**|name|

> In a real-life database, many more fields would be included (e.g., date of birth, address). For simplicity, we restrict ourselves to a few.

---

## Building the Schema

### Initial Tables

```
RECORDS     (record_no, title, ...)
ARTISTS     (artist_no, name, country, ...)
REC_COMP    (rec_co, name, ...)
```

## Relationships

### Records ↔ Artists

- A **record** is made by **one artist** (which may be a group)
- An **artist** makes **one or more records**

→ **One-to-many** relationship

**Solution:** Include the **artist’s primary key** in the RECORDS table:

```
RECORDS (record_no, title, artist_no, ...)
```

> Only the **key** is stored — not the full name or country. To get the artist name, **look up** artist_no in the ARTISTS table.

---

### Records ↔ Record Companies

- A **record** is released by **one record company**
- A **record company** releases **many records**

→ **One-to-many**

**Solution:** Include rec_co in RECORDS:

```
RECORDS (record_no, title, artist_no, rec_co)
```

---

## Chart Positions

To store **weekly positions**:

```
CHARTS (week, record_no, position)
```

- For **52 weeks** in 1964 → **520 entries** (10 per week)

---

## Final Database Structure


```
TOP10USA

├─ RECORDS     (record_no, title, artist_no, rec_co)
├─ ARTISTS     (artist_no, name, country)
├─ REC_COMP    (rec_co, name)
└─ CHARTS      (week, record_no, position)
```

---

## Key Design Benefits

> **No redundancy** — each fact stored **once**:

|Data|Stored In|Appears Only Once?|
|---|---|---|
|Artist name|ARTISTS|Yes|
|Artist country|ARTISTS|Yes|
|Record company|REC_COMP|Yes|

Even though **The Beatles** have **two songs** in the chart → their info is stored **only once**. Same for **Capitol Records**.

---

## Last Week’s Position?

> **Not stored separately** **Why?** It can be **retrieved** from existing data.

**Example:** Current week = **34** Want last week’s position of a record?

```sql
SELECT position
FROM CHARTS
WHERE week = 33
  AND record_no = ?
```

> **Rule of Thumb:** _Don’t store what you can **calculate** or **look up**._

---

## Summary

> ✅ **Good database design** follows three principles:
> 
> 1. **One table per entity**
> 2. **Unique primary key** per record
> 3. **Each fact in exactly one place**

> **Relationships** are represented using **foreign keys** — not duplicated data.

> **Result:**
> 
> - **No redundancy**
> - **Easy updates**
> - **Scalable and consistent**