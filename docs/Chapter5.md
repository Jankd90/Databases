# Chapter 5 — Principle 5

---

## Introduction

So far, we have learned to represent:
- **Entities** (Principles 1–3)  
- **One-to-many relationships** (Principle 4)  

In this chapter, we study **many-to-many relationships** and introduce **Principle 5**, which explains how to represent them using a separate linking table.

---

## Example — Suppliers and Parts

A company uses many parts supplied by multiple suppliers.  
Each **supplier** can supply many **parts**, and each **part** can be supplied by many **suppliers**.

This is a **many-to-many** relationship.

---

### Step 1 — Entities and Attributes

**SUPPLIER**
- SUPPNO — Supplier number (unique)  
- SNAME — Supplier name  
- STATUS — Supplier rating  
- CITY — Supplier location  

**PART**
- PARTNO — Part number (unique)  
- PNAME — Part name  
- COLOR — Color  
- WEIGHT — Weight  
- CITY — Manufacturing location  

The relationship “supplies” connects **SUPPLIER** and **PART**, and includes an attribute **QUANTITY**.

---

### Step 2 — Relational Schema

We must create a separate table to represent the relationship.

```sql
CREATE TABLE SUPPLIER (
  SUPPNO CHAR(3) PRIMARY KEY,
  SNAME VARCHAR(40),
  STATUS INT,
  CITY VARCHAR(40)
);

CREATE TABLE PART (
  PARTNO CHAR(3) PRIMARY KEY,
  PNAME VARCHAR(40),
  COLOR VARCHAR(20),
  WEIGHT DECIMAL(5,2),
  CITY VARCHAR(40)
);

CREATE TABLE SHIPMENT (
  SUPPNO CHAR(3) REFERENCES SUPPLIER(SUPPNO),
  PARTNO CHAR(3) REFERENCES PART(PARTNO),
  QUANTITY INT,
  PRIMARY KEY (SUPPNO, PARTNO)
);
```

The **SHIPMENT** table resolves the many-to-many relationship between suppliers and parts.

---

### Step 3 — Example Data

| SUPPNO | SNAME | STATUS | CITY   |
|--------|--------|---------|--------|
| S1 | Smith | 20 | London |
| S2 | Jones | 10 | Paris  |
| S3 | Blake | 30 | Paris  |
| S4 | Clark | 20 | London |

| PARTNO | PNAME | COLOR | WEIGHT | CITY |
|--------|--------|--------|--------|------|
| P1 | Nut | Red | 12 | London |
| P2 | Bolt | Green | 17 | Paris |
| P3 | Screw | Blue | 17 | Rome |
| P4 | Cog | Red | 19 | London |

| SUPPNO | PARTNO | QUANTITY |
|--------|---------|----------|
| S1 | P1 | 300 |
| S1 | P2 | 200 |
| S2 | P2 | 400 |
| S3 | P1 | 300 |
| S4 | P4 | 250 |

---

### Step 4 — Example Queries

List all parts supplied by supplier `S1`:

```sql
SELECT P.PARTNO, P.PNAME, P.COLOR
FROM PART P
JOIN SHIPMENT SH ON P.PARTNO = SH.PARTNO
WHERE SH.SUPPNO = 'S1';
```

Find suppliers who supply the part `P2`:

```sql
SELECT S.SUPPNO, S.SNAME, S.CITY
FROM SUPPLIER S
JOIN SHIPMENT SH ON S.SUPPNO = SH.SUPPNO
WHERE SH.PARTNO = 'P2';
```

Compute total parts shipped per supplier:

```sql
SELECT SUPPNO, SUM(QUANTITY) AS TOTAL_QUANTITY
FROM SHIPMENT
GROUP BY SUPPNO;
```

---

## Principle 5 — Formal Definition

> 🧩 **Principle 5**  
> Represent every *many-to-many* relationship by creating a separate table.  
> The **primary key** of this table is the **combination** of the primary keys of the related entity tables.

### Explanation

This rule:
1. Eliminates redundancy.  
2. Ensures referential integrity.  
3. Allows attributes (like `QUANTITY`) to describe the relationship itself.  

---

## Step 5 — Complex Relationships

Sometimes, a relationship may involve more than two entities — for example:

> “Each supplier supplies parts to specific projects.”

This becomes a **many-to-many-to-many** relationship.

```sql
CREATE TABLE PROJECT (
  PROJNO CHAR(3) PRIMARY KEY,
  DESCRIPTION VARCHAR(80)
);

CREATE TABLE SHIPMENT (
  SUPPNO CHAR(3) REFERENCES SUPPLIER(SUPPNO),
  PARTNO CHAR(3) REFERENCES PART(PARTNO),
  PROJNO CHAR(3) REFERENCES PROJECT(PROJNO),
  QUANTITY INT,
  PRIMARY KEY (SUPPNO, PARTNO, PROJNO)
);
```

Here the composite key `(SUPPNO, PARTNO, PROJNO)` uniquely identifies each shipment.

---

## Visual Representation

```
SUPPLIER (1) ───< SHIPMENT >───(1) PART
     |                         |
     |                         |
Primary Key            Primary Key
```

The relationship table sits between the two entities, connecting them through foreign keys.

---

## Referential Integrity

The **SHIPMENT** table maintains valid relationships between suppliers and parts.

- Every `SUPPNO` must exist in `SUPPLIER`.  
- Every `PARTNO` must exist in `PART`.  
- Deleting a supplier or part may cascade to delete related shipment records.

Example with cascading constraints:

```sql
ALTER TABLE SHIPMENT
ADD CONSTRAINT FK_SUPPLIER
FOREIGN KEY (SUPPNO)
REFERENCES SUPPLIER(SUPPNO)
ON DELETE CASCADE;

ALTER TABLE SHIPMENT
ADD CONSTRAINT FK_PART
FOREIGN KEY (PARTNO)
REFERENCES PART(PARTNO)
ON DELETE CASCADE;
```

---

## Advantages of Principle 5

| Advantage | Description |
|------------|-------------|
| Normalization | Avoids duplication of part or supplier data |
| Flexibility | Allows adding/removing relationships easily |
| Integrity | Maintains consistency across tables |
| Extensibility | Enables extra attributes for relationships (e.g., quantity, date, cost) |

---

## Exercises

### Exercise 1 — Books and Authors

> Each book may have multiple authors.  
> Each author may write multiple books.  

Design the tables `BOOK`, `AUTHOR`, and `AUTHORSHIP`.

### Exercise 2 — Enrollment

> Students enroll in many courses, and each course has many students.  

Design a relational schema implementing this scenario with foreign keys and composite primary keys.

---

## Summary

- **Principle 5** handles *many-to-many* relationships.  
- Represent such relationships using a separate **linking table**.  
- The linking table’s primary key combines the keys of both entities.  
- Relationship-specific attributes belong in the linking table.  

> ✅ **Design Rule:**  
> Every many-to-many relationship must be explicitly represented by its own table.

---
