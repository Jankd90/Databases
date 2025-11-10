# Chapter 4 — Views

---

## INTRODUCTION

As **indexes** are tables that are **transparent** — which means they *do exist* but the user **cannot see their presence** — **views** are **visible to the user**, but actually **they do not exist**; they are **virtual tables**.

---

## EXAMPLES OF VIEWS

**Views** are very common when using a database. In fact, a **view** consists of a **selection of records or fields (or both)** from one or more **data tables**.

---

### 1. Record Subset from One Table

```text
┌───────────────────────────────────┐
│           ORIGINAL TABLE          │
├─────┬───────┬────────┬────────────┤
│ ID  │ TITLE │ TYPE   │ PRICE      │
├─────┼───────┼────────┼────────────┤
│ 101 │ News  │ Daily  │ 2.50       │
│ 102 │ Time  │ Weekly │ 4.00       │
│ 103 │ Life  │ Weekly │ 5.50       │
│ 104 │ Tech  │ Monthly│ 8.00       │
└─────┴───────┴────────┴────────────┘

          ▲
          │
          ▼

┌───────────────────────────────────┐
│               VIEW                │
├─────┬───────┬────────┬────────────┤
│ ID  │ TITLE │ TYPE   │ PRICE      │
├─────┼───────┼────────┼────────────┤
│ 102 │ Time  │ Weekly │ 4.00       │
│ 103 │ Life  │ Weekly │ 5.50       │
└─────┴───────┴────────┴────────────┘
````

In the above diagram, you can see a **view** that consists of a **selection of records** from a **single data table**. The view ensures that the user is only dealing with **records needed for a specific operation** — for example, **weekly magazines**.

---

### 2. Field Subset from Multiple Tables

text

```
┌─────────────────────┐     ┌─────────────────────┐
│     CUSTOMERS       │     │       ORDERS        │
├─────┬───────┬───────┤     ├─────┬───────┬───────┤
│ ID  │ NAME  │ CITY  │     │ ID  │ CUSTID│ AMOUNT│
├─────┼───────┼───────┤     ├─────┼───────┼───────┤
│ C1  │ Smith │ London│     │ O1  │ C1    │ 250   │
│ C2  │ Jones │ Paris │     │ O2  │ C1    │ 180   │
└─────┴───────┴───────┘     └─────┴───────┴───────┘

          ▲          ▲
          │          │
          ▼          ▼

┌───────────────────────────────┐
│               VIEW            │
├───────┬───────┬───────┬───────┤
│ NAME  │ CITY  │ ORDER │ AMOUNT│
├───────┼───────┼───────┼───────┤
│ Smith │ London│ O1    │ 250   │
│ Smith │ London│ O2    │ 180   │
└───────┴───────┴───────┴───────┘
```

In the next diagram, you can see a **view** consisting of a **selection of fields** from **two data tables**. This type of view is very useful when:

- A table has **many fields**
- You want to **combine information** from several tables
- The **database administrator** wants to **impose a view** to **hide confidential fields** from certain users

> **Security Benefit:** Some users see **one subset of fields**; others see **another**. **Sensitive data** is **hidden** from unauthorized users.

---

### 3. Combined Record + Field Subset

text

```
┌───────────────────────────────────┐
│           ORIGINAL TABLES         │
├─────┬───────┬────────┬────────────┤
│ ID  │ TITLE │ TYPE   │ PRICE      │
├─────┼───────┼────────┼────────────┤
│ 101 │ News  │ Daily  │ 2.50       │
│ 102 │ Time  │ Weekly │ 4.00       │
│ 103 │ Life  │ Weekly │ 5.50       │
└─────┴───────┴────────┴────────────┘

          ▲
          │
          ▼

┌─────────────────────────────┐
│            VIEW             │
├───────┬────────┬────────────┤
│ TITLE │ TYPE   │ PRICE      │
├───────┼────────┼────────────┤
│ Time  │ Weekly │ 4.00       │
│ Life  │ Weekly │ 5.50       │
└───────┴────────┴────────────┘
```

Combining **record subset** and **field subset** gives a **focused, application-specific view**.

---

## VIRTUAL FIELD

Another powerful feature of views is the ability to create a **virtual field** — a field that **appears** to be part of a data table, but **actually isn't**.

### Example: Currency Conversion

text

```
┌───────────────────────────────────┐
│           ORIGINAL TABLE          │
├─────┬───────┬────────┬────────────┤
│ ID  │ ITEM  │ CURRENCY │ PRICE    │
├─────┼───────┼──────────┼──────────┤
│ P1  │ Bolt  │ EUR      │ 15.50    │
│ P2  │ Nut   │ USD      │ 12.00    │
└─────┴───────┴──────────┴──────────┘

          ▲
          │
          ▼

┌───────────────────────────────────────────┐
│                 VIEW                      │
├─────┬───────┬──────────┬──────────────────┤
│ ID  │ ITEM  │ CURRENCY │ PRICE_IN_GUILDERS│
├─────┼───────┼──────────┼──────────────────┤
│ P1  │ Bolt  │ EUR      │ 34.16            │
│ P2  │ Nut   │ USD      │ 26.40            │
└─────┴───────┴──────────┴──────────────────┘
```

> **Note:** PRICE_IN_GUILDERS is **computed** using CURRENCY and PRICE — it **does not exist** in the base table.

sql

```
CREATE VIEW V_ITEMS_GUILDERS AS
SELECT 
  ID,
  ITEM,
  CURRENCY,
  CASE 
    WHEN CURRENCY = 'EUR' THEN PRICE * 2.20371
    WHEN CURRENCY = 'USD' THEN PRICE * 2.20
    ELSE PRICE
  END AS PRICE_IN_GUILDERS
FROM ITEMS;
```

---

## Summary

> ✅ **Views are virtual tables** that:
> 
> - **Filter records** (subset of rows)
> - **Select fields** (subset of columns)
> - **Join multiple tables**
> - **Compute virtual fields**
> - **Enforce security** by hiding sensitive data

> **Rule of Thumb:** _Use views to give users **exactly what they need** — and **nothing more**._