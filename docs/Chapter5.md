# Chapter 5 — Integrity

---

## INTRODUCTION

- **Security** involves ensuring that users are **allowed** to do the things they are trying to do.  
- **Integrity** involves ensuring that the things they are trying to do are **correct**.

Or to put it otherwise:  
> **Security** means protecting the database against **unauthorized users**;  
> **Integrity** means protecting it against **authorized users**.

---

## SOME ASPECTS OF INTEGRITY

### 1. Primary Key Uniqueness

Every table **must have a primary key** — uniquely identifying each record.  
The **DBMS must guarantee** that **no two records** have the same primary key.

```sql
CREATE TABLE EMPLOYEE (
  EMPNO CHAR(5) PRIMARY KEY,  -- Enforced uniqueness
  NAME VARCHAR(50)
);
````

---

### 2. Foreign Key Referential Integrity

Some tables include **foreign keys**. A **foreign key must match** an existing **primary key** in another table.

The **DBMS must enforce** this rule:

|Situation|Problem|DBMS Action|
|---|---|---|
|Delete referenced record|Foreign key points to **nothing**|**Prevent deletion** or **cascade**|
|Update primary key|Foreign keys become **invalid**|**Update all related foreign keys**|
|Insert invalid foreign key|Refers to **non-existent record**|**Reject insert**|


```sql
ALTER TABLE EMPLOYEE
  ADD FOREIGN KEY (DEPTNO)
  REFERENCES DEPARTMENT(DEPTNO)
  ON DELETE RESTRICT
  ON UPDATE CASCADE;
```

---

### 3. Format Constraints (Domain Integrity)

**Format constraints** help prevent **obvious mistakes**:

|Field Type|Allowed Values|Example|
|---|---|---|
|Number|Digits only|SALARY DECIMAL(10,2)|
|Text|Capitals only|STATUS CHAR(1) CHECK (STATUS IN ('A','I'))|
|Postcode|4 digits + 2 letters|POSTCODE CHAR(6) CHECK (POSTCODE REGEXP '^[0-9]{4}[A-Z]{2}$')|
|Date|Valid dates only|BIRTHDATE DATE|

> In **Paradox for Windows**, defining a **field type** is itself a **format constraint**. A Date field accepts **only valid dates** → prevents _blunt mistakes_.


```sql
CREATE TABLE PERSON (
  ID CHAR(8) PRIMARY KEY,
  BIRTHDATE DATE CHECK (BIRTHDATE >= '1900-01-01')
);
```

---

## Limitations of Integrity Enforcement

> **No computer system can ensure _complete_ integrity.**

Even with:

- Primary key enforcement
- Foreign key checks
- Format constraints

**Subtle errors** can still occur:

|Example|Why It Passes Checks|
|---|---|
|Salary = 5000 for a janitor|Within numeric range|
|Birthdate = 2025-01-01 for a 50-year-old|Valid date format|
|Two employees with same phone number|No uniqueness rule|

---

## Summary

> ✅ **Integrity** is about **correctness**, not just **access**. The DBMS helps with:
> 
> - **Uniqueness** (Primary Keys)
> - **Referential accuracy** (Foreign Keys)
> - **Format validity** (Domain Constraints)

> **Rule of Thumb:** _The system prevents **silly mistakes** — but **smart mistakes** require **application logic** and **human judgment**._