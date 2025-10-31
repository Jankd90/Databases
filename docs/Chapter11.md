# Chapter 11 — Principle 11

---

## Introduction

With the first ten principles establishing the logical foundations of relational design, **Principle 11** focuses on the **transition from logical to physical design**.  
It deals with the **implementation phase**, where the conceptual model is translated into a real, efficient database schema.

This principle emphasizes that **physical structures** (indexes, clusters, partitions) must serve the logical model — not distort it.

---

## Logical vs. Physical Design

| Aspect | Logical Design | Physical Design |
|---------|----------------|-----------------|
| **Focus** | What data means | How data is stored |
| **Concern** | Relationships, keys, normalization | Performance, access paths |
| **Representation** | Entities, attributes, relationships | Tables, indexes, files, partitions |
| **Objective** | Data integrity | Query efficiency |

Principle 11 ensures that logical soundness is preserved while optimizing for real-world performance.

---

## Principle 11 — Formal Definition

> 🧩 **Principle 11**  
> The physical design must **faithfully implement** the logical model without introducing new semantics or violating existing relationships.

---

## Example — Logical to Physical Mapping

### Logical Schema

```sql
CREATE TABLE CUSTOMER (
  CUST_ID CHAR(5) PRIMARY KEY,
  NAME VARCHAR(50),
  CITY VARCHAR(40)
);

CREATE TABLE ORDER_HEADER (
  ORDER_NO CHAR(6) PRIMARY KEY,
  ORDER_DATE DATE,
  CUST_ID CHAR(5) REFERENCES CUSTOMER(CUST_ID)
);
```

### Physical Design Decisions

| Design Element | Description |
|----------------|-------------|
| **Index on CUST_ID** | Speeds up joins and lookups in `ORDER_HEADER`. |
| **Partition by CITY** | Improves data locality and query performance. |
| **Materialized View** | May cache frequently queried results. |

Each decision enhances performance **without altering** logical dependencies.

---

## Common Implementation Issues

| Issue | Description | Example |
|--------|--------------|----------|
| **Denormalization** | Storing redundant data for speed | Copying `CUSTOMER.NAME` into `ORDER_HEADER` |
| **Derived Fields Stored** | Violates Principle 8 | Storing `TOTAL_AMOUNT` instead of computing |
| **Redundant Relationships** | Violates Principle 10 | Adding `CUSTOMER–PRODUCT` when derivable |
| **Physical-only keys** | Must still preserve logical uniqueness | Use of surrogate keys without justification |

> ⚠️ **Rule:** Never let physical optimization compromise logical consistency.

---

## Example — Controlled Denormalization

In rare cases, denormalization is used for **performance** but must be explicitly managed.

```sql
CREATE TABLE ORDER_HEADER (
  ORDER_NO CHAR(6) PRIMARY KEY,
  ORDER_DATE DATE,
  CUST_ID CHAR(5),
  CUSTOMER_NAME VARCHAR(50), -- denormalized
  FOREIGN KEY (CUST_ID) REFERENCES CUSTOMER(CUST_ID)
);
```

A **trigger** ensures synchronization:

```sql
CREATE TRIGGER sync_customer_name
AFTER UPDATE ON CUSTOMER
FOR EACH ROW
UPDATE ORDER_HEADER
SET CUSTOMER_NAME = NEW.NAME
WHERE CUST_ID = NEW.CUST_ID;
```

Logical accuracy is preserved, even with a performance-driven redundancy.

---

## Indexes and Access Paths

Indexes improve query speed but do not change logical meaning.

### Example

```sql
CREATE INDEX idx_order_customer ON ORDER_HEADER(CUST_ID);
```

This adds an access path but **does not alter** the table’s semantics.

> ✅ **Guideline:** Use indexes and clustering for performance — not as a substitute for logical relations.

---

## Physical Independence

A database must exhibit **physical data independence**, meaning:

> Changes to storage or indexing structures **do not affect** application logic or the logical schema.

### Example

Repartitioning a table:

```sql
ALTER TABLE ORDER_HEADER PARTITION BY RANGE (ORDER_DATE);
```

Applications and relationships remain unaffected.

---

## Physical Design Checklist

| Goal | Implementation |
|-------|----------------|
| Data integrity | Enforce primary and foreign keys |
| Performance | Use indexes, caching, partitioning |
| Maintainability | Preserve normalization, avoid redundancy |
| Scalability | Choose efficient storage organization |
| Logical fidelity | Ensure physical optimizations don’t change meaning |

---

## Example — Logical and Physical Views

A **view** allows a logical structure to persist even if physical storage changes.

```sql
CREATE VIEW CUSTOMER_ORDERS AS
SELECT C.NAME, O.ORDER_NO, O.ORDER_DATE
FROM CUSTOMER C
JOIN ORDER_HEADER O ON C.CUST_ID = O.CUST_ID;
```

If `ORDER_HEADER` is later partitioned, this view remains logically consistent.

---

## Exercises

### Exercise 1 — Logical Integrity

> Design physical indexes and partitions for the `STUDENT`, `COURSE`, and `ENROLLMENT` schema without altering logical structure.

### Exercise 2 — Controlled Denormalization

> Introduce a redundant attribute for performance.  
> Define triggers or constraints to preserve consistency.

---

## Summary

- **Principle 11** bridges logical and physical design.  
- The **logical model** defines meaning; the **physical design** optimizes performance.  
- Physical structures must never alter or contradict logical relationships.  
- Controlled denormalization and indexing are acceptable if logical integrity is maintained.

> ✅ **Design Rule:**  
> Optimize physically — but never compromise the logical model.

---
