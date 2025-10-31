# Chapter 8 — Principle 8

---

## Introduction

In previous chapters, we have examined how to represent entities, relationships, and referential integrity within databases.  
**Principle 8** addresses the correct **placement of derived or computed data** — ensuring that only *elementary facts* are stored in the database, while derived information is computed when needed.

This principle ensures **data consistency**, **accuracy**, and **eliminates redundancy**.

---

## Derived Data

A *derived attribute* is one that can be calculated from other stored data.  
Examples:
- Total order value = SUM of line-item amounts  
- Employee age = CURRENT_DATE – birth date  
- Average salary per department = aggregate function of `SALARY`

> 🧩 **Key Rule:**  
> Derived data should **not** be stored directly in tables — it should be computed dynamically using queries or views.

---

## Example — Orders and Order Lines

### Entities and Relationships

Each order consists of several order lines.  
Each order line contains quantity and price.

**Tables:**

```sql
CREATE TABLE ORDER_HEADER (
  ORDER_NO CHAR(6) PRIMARY KEY,
  ORDER_DATE DATE
);

CREATE TABLE ORDER_LINE (
  ORDER_NO CHAR(6) REFERENCES ORDER_HEADER(ORDER_NO),
  LINE_NO INT,
  PRODUCT_ID CHAR(5),
  QUANTITY INT,
  PRICE DECIMAL(10,2),
  PRIMARY KEY (ORDER_NO, LINE_NO)
);
```

---

### Incorrect Design

If the total order value is added as a stored column:

```sql
ALTER TABLE ORDER_HEADER ADD TOTAL_VALUE DECIMAL(12,2);
```

This design introduces **redundancy** — the total can be calculated from `ORDER_LINE`.

---

### Correct Design

Instead, calculate the total dynamically:

```sql
SELECT ORDER_NO, SUM(QUANTITY * PRICE) AS TOTAL_VALUE
FROM ORDER_LINE
GROUP BY ORDER_NO;
```

Or create a **view** for convenient retrieval:

```sql
CREATE VIEW ORDER_TOTAL AS
SELECT ORDER_NO, SUM(QUANTITY * PRICE) AS TOTAL_VALUE
FROM ORDER_LINE
GROUP BY ORDER_NO;
```

This keeps data consistent while allowing easy computation of totals.

---

## Principle 8 — Formal Definition

> 🧩 **Principle 8**  
> Only *elementary facts* should be stored in the database.  
> Facts that can be **derived** from others should **not** be physically stored but computed when required.

---

## Why Derived Data Should Not Be Stored

| Reason | Description |
|---------|--------------|
| **Redundancy** | Duplicate information increases storage and inconsistency risk. |
| **Update anomalies** | Updates in one table may require recalculating stored derived fields. |
| **Integrity issues** | Inconsistencies arise if derived and base data are unsynchronized. |
| **Efficiency** | Derived values can be computed via optimized queries or views. |

---

## When Storing Derived Data May Be Justified

In some exceptional cases, storing derived data can improve **performance**, especially for large datasets with complex calculations.

**Example — Materialized Totals**

```sql
CREATE TABLE SALES_SUMMARY (
  SALES_DATE DATE PRIMARY KEY,
  TOTAL_SALES DECIMAL(12,2)
);
```

This is acceptable only if:
- The derived data is **periodically recalculated** (e.g., nightly batch process).
- **Triggers** or **procedures** ensure synchronization.

---

### Example — Using Triggers to Maintain Derived Data

```sql
CREATE TRIGGER update_sales_summary
AFTER INSERT OR UPDATE ON SALES
FOR EACH ROW
BEGIN
  UPDATE SALES_SUMMARY
  SET TOTAL_SALES = (
    SELECT SUM(AMOUNT)
    FROM SALES
    WHERE SALES_DATE = NEW.SALES_DATE
  )
  WHERE SALES_DATE = NEW.SALES_DATE;
END;
```

This ensures that the summary table remains consistent with the detailed data.

---

## Derived vs. Stored Attributes — Comparison

| Type | Example | Stored? | Notes |
|------|----------|----------|-------|
| Base attribute | `EMPLOYEE.SALARY` | Yes | Elementary fact |
| Derived attribute | `AGE = CURRENT_DATE - BIRTH_DATE` | No | Calculated |
| Aggregate value | `AVG(SALARY)` | No | Computed using query |
| Materialized summary | `TOTAL_SALES` | Conditional | Stored only for optimization |

---

## Example — Employee Age

Instead of storing age directly:

```sql
CREATE TABLE EMPLOYEE (
  EMPNO CHAR(5) PRIMARY KEY,
  NAME VARCHAR(50),
  BIRTH_DATE DATE
);
```

Calculate on demand:

```sql
SELECT NAME, FLOOR(DATEDIFF(CURDATE(), BIRTH_DATE) / 365) AS AGE
FROM EMPLOYEE;
```

---

## Data Normalization Context

Principle 8 reinforces the **Third Normal Form (3NF)**:

> “Every non-key attribute must depend directly on the key — and nothing else.”

Derived data violates this rule because it depends on other attributes, not the key itself.

---

## Exercises

### Exercise 1 — Identify Derived Data

> Examine the following attributes and identify which should be stored and which should be derived:
> - `TOTAL_SALARY`
> - `AGE`
> - `EMPLOYEE_NAME`
> - `HOURS_WORKED`
> - `TOTAL_HOURS`

### Exercise 2 — Create a View

> Write a SQL view that shows each department’s total salary cost using the `EMPLOYEE` table.

---

## Summary

- **Principle 8** ensures only *base facts* are stored in databases.  
- Derived or computed values should be **calculated dynamically**.  
- Avoid storing redundant information to maintain integrity.  
- Exceptions exist for performance — use **materialized summaries** with **controlled synchronization**.

> ✅ **Design Rule:**  
> Store only fundamental data. Compute derived values through queries or views.

---
