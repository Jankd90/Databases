# Chapter 9 — Principle 9

---

## Introduction

In this final principle of database design, we address **how to handle attributes that apply to only a subset of entities within a table**.  
**Principle 9** deals with **optional attributes** and **subtype (specialization) structures** — ensuring each attribute belongs only where it is logically relevant.

This prevents sparse tables, NULL proliferation, and semantic ambiguity in data models.

---

## The Problem — Irrelevant or Optional Attributes

Suppose a company stores both **employees** and **consultants** in a single `PERSONNEL` table.

```sql
CREATE TABLE PERSONNEL (
  ID CHAR(5) PRIMARY KEY,
  NAME VARCHAR(50),
  SALARY DECIMAL(10,2),
  CONTRACT_RATE DECIMAL(10,2)
);
```

Here:
- `SALARY` applies to employees.
- `CONTRACT_RATE` applies only to consultants.

Result:
- Many **NULL** values.
- Poor semantic clarity.
- Violates normalization principles.

---

## Principle 9 — Formal Definition

> 🧩 **Principle 9**  
> Attributes that apply only to *certain subtypes* of an entity must be placed in separate subtype tables.  
> Each subtype table references the common **supertype** entity via its key.

---

## Correct Design — Supertype / Subtype Model

We separate the entity into one **supertype** (`PERSONNEL`) and two **subtypes** (`EMPLOYEE`, `CONSULTANT`).

```sql
CREATE TABLE PERSONNEL (
  ID CHAR(5) PRIMARY KEY,
  NAME VARCHAR(50)
);

CREATE TABLE EMPLOYEE (
  ID CHAR(5) PRIMARY KEY REFERENCES PERSONNEL(ID),
  SALARY DECIMAL(10,2)
);

CREATE TABLE CONSULTANT (
  ID CHAR(5) PRIMARY KEY REFERENCES PERSONNEL(ID),
  CONTRACT_RATE DECIMAL(10,2)
);
```

This ensures:
- Each person’s general data is stored once.
- Specific data resides in the appropriate subtype.
- No unused or NULL attributes.

---

## Example Data

| PERSONNEL |        |        |
|------------|--------|--------|
| ID | NAME |
|----|------|
| 1001 | Smith |
| 1002 | Brown |
| 1003 | Jones |

| EMPLOYEE |        |        |
|-----------|--------|--------|
| ID | SALARY |
|----|--------|
| 1001 | 3000 |
| 1002 | 2800 |

| CONSULTANT |        |        |
|-------------|--------|--------|
| ID | CONTRACT_RATE |
|----|---------------|
| 1003 | 75.00 |

---

### Query — All Personnel with Their Compensation

```sql
SELECT P.ID, P.NAME,
       E.SALARY,
       C.CONTRACT_RATE
FROM PERSONNEL P
LEFT JOIN EMPLOYEE E ON P.ID = E.ID
LEFT JOIN CONSULTANT C ON P.ID = C.ID;
```

This provides a unified view of all personnel, with subtype-specific details filled in as applicable.

---

## Generalizing Principle 9

| Concept | Description |
|----------|-------------|
| **Supertype** | The general entity containing shared attributes (e.g., `PERSONNEL`). |
| **Subtype** | Specialized entities with additional attributes (e.g., `EMPLOYEE`, `CONSULTANT`). |
| **Key Inheritance** | Each subtype’s primary key is also a foreign key referencing the supertype. |
| **Constraint** | Every subtype record must correspond to exactly one supertype record. |

---

## Alternative Representation — Single Table with Type Indicator

When subtypes differ only slightly, one may use a **discriminator column**:

```sql
CREATE TABLE PERSONNEL (
  ID CHAR(5) PRIMARY KEY,
  NAME VARCHAR(50),
  TYPE CHAR(1),  -- 'E' for employee, 'C' for consultant
  SALARY DECIMAL(10,2),
  CONTRACT_RATE DECIMAL(10,2)
);
```

### Example Constraint (Check Clause)

```sql
ALTER TABLE PERSONNEL
ADD CONSTRAINT CHECK_TYPE
CHECK (
  (TYPE = 'E' AND CONTRACT_RATE IS NULL) OR
  (TYPE = 'C' AND SALARY IS NULL)
);
```

✅ Simple but **less normalized** — suitable for small systems.

---

## When to Use Subtypes

| Use Case | Recommended Structure |
|-----------|-----------------------|
| Many subtype-specific attributes | Separate subtype tables |
| Minor variations | Single table with type indicator |
| Polymorphic behavior (inheritance-like) | Supertype/subtype with key inheritance |
| Minimal design effort | Single table (denormalized) |

---

## Example — Vehicle Classification

**Supertype:** `VEHICLE`  
**Subtypes:** `CAR`, `TRUCK`

```sql
CREATE TABLE VEHICLE (
  VIN CHAR(10) PRIMARY KEY,
  MAKE VARCHAR(40),
  MODEL VARCHAR(40)
);

CREATE TABLE CAR (
  VIN CHAR(10) PRIMARY KEY REFERENCES VEHICLE(VIN),
  PASSENGER_CAPACITY INT
);

CREATE TABLE TRUCK (
  VIN CHAR(10) PRIMARY KEY REFERENCES VEHICLE(VIN),
  LOAD_CAPACITY DECIMAL(10,2)
);
```

Each subtype inherits `VIN` as its identifier.

---

## Benefits of Principle 9

| Benefit | Description |
|----------|-------------|
| **Semantic clarity** | Each table represents one concept. |
| **Normalization** | Eliminates NULLs and unused columns. |
| **Extensibility** | New subtypes can be added easily. |
| **Integrity** | Constraints maintain logical relationships. |

---

## Exercises

### Exercise 1 — Specialization

> Model a company’s product catalog where some products are *software* (with version and platform) and others are *hardware* (with weight and warranty).  
> Create normalized SQL tables.

### Exercise 2 — Type Discriminator

> Modify the design to use a single table with a type discriminator and appropriate check constraints.

---

## Summary

- **Principle 9** enforces separation of subtype-specific attributes.  
- Use **supertype/subtype structures** when attributes apply to only part of an entity set.  
- This eliminates redundant NULLs and improves clarity.  
- A **discriminator column** is a simplified alternative for minor variations.

> ✅ **Design Rule:**  
> Each attribute belongs only to the entity or subtype it describes.

---
