# Chapter 2 — Many-to-Many

---

## Introduction

In Chapter 1, we examined **departments and employees** to understand one-to-many relationships.  
We now consider a more complex case — the **many-to-many relationship** — using the classic *suppliers and parts* example.

---

## Suppliers and Parts — A Good Design

The **Suppliers-and-Parts** database models the following situation:

- A company uses many kinds of parts and obtains them from various suppliers.  
- Each **supplier** can supply many parts.  
- Each **part** can be supplied by many suppliers.  
- For each combination of supplier and part, there may be **one shipment** with a certain quantity.  

### Entities and Attributes

**SUPPLIER**
- SUPPNO — Supplier number (unique)  
- SNAME — Name  
- STATUS — Rating or status value  
- CITY — Supplier location  

**PART**
- PARTNO — Part number (unique)  
- PNAME — Name  
- COLOR — Color  
- WEIGHT — Weight  
- CITY — Storage location  

**SHIPMENT**
- SUPPNO — Supplier number (foreign key)  
- PARTNO — Part number (foreign key)  
- QUANTITY — Number of parts shipped  

---

### Relational Schema

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

---

### Example Data

| SUPPNO | SNAME | STATUS | CITY   |
|--------|--------|---------|--------|
| S1 | Smith | 20 | London |
| S2 | Jones | 10 | Paris  |
| S3 | Blake | 30 | Paris  |
| S4 | Clark | 20 | London |
| S5 | Adams | 30 | Athens |

| PARTNO | PNAME | COLOR | WEIGHT | CITY   |
|--------|--------|--------|--------|--------|
| P1 | Nut | Red | 12 | London |
| P2 | Bolt | Green | 17 | Paris |
| P3 | Screw | Blue | 17 | Rome |
| P4 | Screw | Red | 14 | London |
| P5 | Cam | Blue | 12 | Paris |
| P6 | Cog | Red | 19 | London |

| SUPPNO | PARTNO | QUANTITY |
|--------|---------|----------|
| S1 | P1 | 300 |
| S1 | P2 | 200 |
| S1 | P3 | 400 |
| S1 | P4 | 200 |
| S1 | P5 | 100 |
| S1 | P6 | 100 |
| S2 | P1 | 300 |
| S2 | P2 | 400 |
| S3 | P2 | 200 |
| S4 | P2 | 200 |
| S4 | P4 | 300 |
| S4 | P5 | 400 |

---

## Discussion

The suppliers-and-parts relationship is **many-to-many**:

- Each supplier → many parts  
- Each part → many suppliers  

The **SHIPMENT** table resolves this by linking both entities through foreign keys.

> 🧩 **Principle 5**  
> Represent each *many-to-many relationship* as a separate table.  
> Use foreign keys referencing the related entities, and use their combination as the primary key.

---

### Why the Design Works

1. **SUPPLIER** and **PART** follow the earlier rules:
   - Each represents one entity type.
   - Each has a primary key and entity attributes.

2. **SHIPMENT** captures the relationship itself:
   - Foreign keys: `SUPPNO`, `PARTNO`
   - Attribute of the relationship: `QUANTITY`
   - Composite primary key: `(SUPPNO, PARTNO)`

3. This avoids redundancy and preserves referential integrity.

---

### Incorrect Designs

#### ❌ Design 1 — Shipment fields in SUPPLIER

```text
SUPPLIER(SUPPNO, SNAME, STATUS, CITY, PARTNO_1, QUANTITY_1, ... PARTNO_9, QUANTITY_9)
```

This violates earlier principles:
- Stores part-related data in supplier table  
- Restricts number of shipments  
- Causes null values and maintenance issues  

#### ❌ Design 2 — Shipment fields in PART

Same issues apply if shipment data are embedded in the `PART` table.

---

### Many-to-Many-to-Many Example

Complex relationships exist, e.g., *suppliers, parts, and projects*:

**Example Design:**

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

Here the relationship involves three entities — a **many-to-many-to-many** relationship.  
The concept generalizes Principle 5.

> 💡 **Observation:**  
> A many-to-many relationship can always be seen as two one-to-many relationships combined.

---

### Other Inter-Table Relationships

Not all relationships are defined by keys.  
For example, `SUPPLIER.CITY` and `PART.CITY` may indicate **co-location** (same city).  
This relation is based on *matching values*, not keys.

If needed, a new **CITY** table could later formalize this relationship.

---

## Summary

> **Definition — Primary Key:**  
> A field (or combination) uniquely identifying each record in a table.  

> **Definition — Foreign Key:**  
> A field (or combination) in one table whose values reference a primary key in another table.

### Design Principles Recap

1. Represent each **entity type** as a separate table.  
2. Decide the **primary key** for each table.  
3. Assign each property of an entity to its own table.  
4. Represent each **one-to-many** relationship using a **foreign key** in the “many” table.  
5. Represent each **many-to-many** relationship as a separate table using a **composite primary key**.

> ✅ Good design avoids redundancy, ensures consistency, and supports future extension.

---

### 🧠 Exercise

Extend the supplier–part model to include projects.  
Design and populate a `SHIPMENT` table that links suppliers, parts, and projects.  
Define appropriate primary and foreign keys.

---
