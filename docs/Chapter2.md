# Chapter 2 — Database Design (Continued)

---

## INTRODUCTION

In the previous chapter we considered the **departments-and-employees** database and used it to introduce a number of important principles of database design. In particular, we showed how to deal with **one-to-many relationships**. In this chapter we treat a more complicated kind of relationship, namely, the **many-to-many relationship**. Again we approach the problem by way of a well-known but useful example, this time the **suppliers-and-parts** example.

---

## SUPPLIERS AND PARTS — A GOOD DESIGN

The **suppliers-and-parts** database is intended to model the following situation:

- A company uses a number of different kinds of **parts** and obtains them in the form of **shipments** from a number of different **suppliers**.  
- **Each supplier** supplies many different kinds of parts; **each kind of part** is supplied by many different suppliers.  
- At any given time, there will be **at most one shipment outstanding** for a given kind of part from a given supplier.  
- Different shipments may involve different **quantities** of the part being shipped.  

**Each Supplier:**
- Has a **supplier number** (unique)  
- Has a **name**, **status** (rating value), and **city** (location)  

**Each Part:**
- Has a **part number** (unique)  
- Has a **name**, **color**, **weight**, and **city** (storage location)  

**Each Shipment:**
- Identifies a **supplier**, a **part**, and a **quantity**  

**Relational Schema:**

```sql
CREATE TABLE SUPPLIER (
  SUPPNO CHAR(2) PRIMARY KEY,
  SNAME VARCHAR(50),
  STATUS INTEGER,
  CITY VARCHAR(50)
);

CREATE TABLE PART (
  PARTNO CHAR(2) PRIMARY KEY,
  PNAME VARCHAR(50),
  COLOR VARCHAR(20),
  WEIGHT DECIMAL(5,1),
  CITY VARCHAR(50)
);

CREATE TABLE SHIPMENT (
  SUPPNO CHAR(2) REFERENCES SUPPLIER(SUPPNO),
  PARTNO CHAR(2) REFERENCES PART(PARTNO),
  QUANTITY INTEGER,
  PRIMARY KEY (SUPPNO, PARTNO)
);
````

### Sample Data

**Table SUPPLIER:**

|SUPPNO|SNAME|STATUS|CITY|
|---|---|---|---|
|S1|Smith|20|London|
|S2|Jones|10|Paris|
|S3|Blake|30|Paris|
|S4|Clark|20|London|
|S5|Adams|30|Athens|

**Table PART:**

|PARTNO|PNAME|COLOR|WEIGHT|CITY|
|---|---|---|---|---|
|P1|Nut|red|12.0|London|
|P2|Bolt|green|17.0|Paris|
|P3|Screw|blue|17.0|Rome|
|P4|Screw|red|14.0|London|
|P5|Cam|blue|12.0|Paris|
|P6|Cog|red|19.0|London|

**Table SHIPMENT:**

|SUPPNO|PARTNO|QUANTITY|
|---|---|---|
|S1|P1|300|
|S1|P2|200|
|S1|P3|400|
|S1|P4|200|
|S1|P5|100|
|S1|P6|100|
|S2|P1|300|
|S2|P2|400|
|S3|P2|200|
|S4|P2|200|
|S4|P4|300|
|S4|P5|400|

---

## ⚠️ Bad Design Example — Embedding Shipments in SUPPLIER

We **cannot** put shipment information into the SUPPLIER table. Doing so would violate principles from Chapter 1:

text

```
SUPPNO | SNAME | STATUS | CITY | PARTNO_1 | QUANTITY_1 | ... | PARTNO_9 | QUANTITY_9
```

This leads to the same problems as before:

- Fixed limit on shipments per supplier
- Nulls for unused slots
- Complex queries and updates
- Violates **Principle 1** and **Principle 3**

---

## ✅ Correct Design — SHIPMENT as a Separate Table

The correct approach introduces a **separate SHIPMENT table**:

- SHIPMENT.SUPPNO → foreign key to SUPPLIER.SUPPNO
- SHIPMENT.PARTNO → foreign key to PART.PARTNO
- QUANTITY → property of the **shipment**, not supplier or part
- **Primary key** = (SUPPNO, PARTNO) combination (uniquely identifies each shipment)

> **Key Insight:** **Shipments are entities in their own right**, dependent on suppliers and parts, but with their own properties and identity.

---

## Discussion

The **suppliers-and-parts** example involves a **many-to-many relationship**:

- For each **supplier**, there are **many parts**
- For each **part**, there are **many suppliers**

We resolve this by:

> 🧩 **Principle 5** Represent each **many-to-many relationship** between entity types as a **separate table**.
> 
> - Use **foreign keys** to identify the related entities.
> - Use the **combination of foreign keys** as the **primary key**.
> - Represent **properties of the relationship** (e.g., QUANTITY) in this table.

---

## FURTHER REMARKS

### Many-to-Many-to-Many (and Beyond)

Many-to-many relationships are not the most complex. Consider an extension involving **projects**:

> Each **shipment** is of a **part** from a **supplier** to a **project**.

**Extended Schema:**

sql

```
CREATE TABLE PROJECT (
  PROJNO CHAR(3) PRIMARY KEY,
  PNAME VARCHAR(50),
  BUDGET DECIMAL(10,2)
);

CREATE TABLE SHIPMENT (
  SUPPNO CHAR(2) REFERENCES SUPPLIER(SUPPNO),
  PARTNO CHAR(2) REFERENCES PART(PARTNO),
  PROJNO CHAR(3) REFERENCES PROJECT(PROJNO),
  QUANTITY INTEGER,
  PRIMARY KEY (SUPPNO, PARTNO, PROJNO)
);
```

This handles **many-to-many-to-many** relationships using the **same technique** — just more foreign keys.

> **Exercise:** Invent sample data for this extended design.

---

### Many-to-Many = Two One-to-Many

A many-to-many relationship can always be seen as **two one-to-many relationships**:

- **One supplier → many shipments**
- **One part → many shipments**

**Principle 4** applies to each separately.

---

### Non-Key Relationships

Not all relationships are captured by foreign keys.

Example: SUPPLIER.CITY and PART.CITY → Suppliers in **London** are _colocated_ with parts stored in **London** → This is a **relationship**, but **not enforced by keys** → Could become a foreign key if a CITY table were added

---

## Summary

We have now concluded our discussion of database design. We have covered enough to approach design problems with confidence, especially in small or single-user environments.

### Key Definitions

> 💡 **Primary Key** A field (or combination of fields) that **uniquely identifies** each record in a table.

> 💡 **Foreign Key** A field (or combination) in one table whose values **must match** the primary key of another table.

---

### Design Principles (Recap)

> 🧩 **Principle 1** Represent each **entity type** as a **separate table**.

> 🧩 **Principle 2** Decide the **primary key** for each table.

> 🧩 **Principle 3** Assign each **property** of an entity type to a **field** in its table.

> 🧩 **Principle 4** Represent each **one-to-many relationship** with a **foreign key** in the "many" table.

> 🧩 **Principle 5** Represent each **many-to-many relationship** as a **separate table**, using **foreign key combinations** as the **primary key** and storing **relationship properties** within.

---

> ✅ **Good database design** is built on **clarity**, **consistency**, and **scalability**. Each entity, attribute, and relationship has **one correct place** — and only one.