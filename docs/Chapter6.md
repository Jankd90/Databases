# Chapter 6 — Principle 6

---

## Introduction

We have studied how to represent **entities** and **relationships** using the first five principles of database design.  
Now we introduce **Principle 6**, which deals with the **uniqueness of primary keys** and the **distinction between identifying and non-identifying relationships**.

This principle ensures every record in a database can be uniquely identified — a core foundation of relational integrity.

---

## Unique Identification

Every table must have a **primary key** — a set of one or more fields whose values uniquely identify each record.  
If no natural key exists, a **surrogate key** must be introduced.

### Example

```sql
CREATE TABLE STUDENT (
  STUDENT_ID CHAR(6) PRIMARY KEY,
  NAME VARCHAR(50),
  DATE_OF_BIRTH DATE,
  ADDRESS VARCHAR(100)
);
```

The field `STUDENT_ID` uniquely identifies each student, even if two students share the same name or date of birth.

---

## Composite Keys

In some cases, uniqueness is defined by a **combination** of fields rather than a single one.

### Example — Enrollment Table

A student can enroll in several courses, and each course has many students.  
The relationship is many-to-many and requires a **composite primary key**.

```sql
CREATE TABLE ENROLLMENT (
  STUDENT_ID CHAR(6) REFERENCES STUDENT(STUDENT_ID),
  COURSE_ID CHAR(6) REFERENCES COURSE(COURSE_ID),
  ENROLL_DATE DATE,
  PRIMARY KEY (STUDENT_ID, COURSE_ID)
);
```

The pair `(STUDENT_ID, COURSE_ID)` ensures that each enrollment record is unique.

---

## Identifying vs. Non-Identifying Relationships

### 1. Identifying Relationship

An **identifying relationship** occurs when the existence of a child record **depends** on its parent.

**Example:**

> Each *Order Line* belongs to a specific *Order* and cannot exist independently.

```sql
CREATE TABLE ORDER_HEADER (
  ORDER_NO CHAR(6) PRIMARY KEY,
  ORDER_DATE DATE
);

CREATE TABLE ORDER_LINE (
  ORDER_NO CHAR(6),
  LINE_NO INT,
  PRODUCT_ID CHAR(6),
  QUANTITY INT,
  PRIMARY KEY (ORDER_NO, LINE_NO),
  FOREIGN KEY (ORDER_NO) REFERENCES ORDER_HEADER(ORDER_NO)
);
```

Here, `ORDER_LINE` is **identified** by its parent `ORDER_HEADER`.

---

### 2. Non-Identifying Relationship

A **non-identifying relationship** occurs when the child table can exist independently of the parent.

**Example:**

> An employee belongs to a department but could exist even if the department is deleted.

```sql
CREATE TABLE DEPARTMENT (
  DEPTNO CHAR(3) PRIMARY KEY,
  NAME VARCHAR(50)
);

CREATE TABLE EMPLOYEE (
  EMPNO CHAR(5) PRIMARY KEY,
  NAME VARCHAR(50),
  JOB VARCHAR(30),
  DEPTNO CHAR(3),
  FOREIGN KEY (DEPTNO) REFERENCES DEPARTMENT(DEPTNO)
);
```

Here, `EMPLOYEE` has its own key (`EMPNO`), so the relationship is non-identifying.

---

## Surrogate Keys

When a natural key is either unavailable or inefficient, introduce a **surrogate key** (artificial identifier).

### Example

```sql
CREATE TABLE PROJECT (
  PROJECT_ID SERIAL PRIMARY KEY,
  DESCRIPTION VARCHAR(100),
  START_DATE DATE,
  END_DATE DATE
);
```

Surrogate keys simplify joins and ensure uniform key structures across tables.

> 💡 **Guideline:**  
> Use surrogate keys when natural keys are long, compound, or changeable.

---

## Principle 6 — Formal Definition

> 🧩 **Principle 6**  
> Every table must have a **primary key** that uniquely identifies each record.  
> For relationships:
> - Use **composite keys** for identifying relationships.  
> - Use **independent keys** for non-identifying relationships.

---

## Example — Department, Employee, and Dependents

### Situation

Each **employee** belongs to a department (non-identifying).  
Each **dependent** belongs to an employee (identifying).

```sql
CREATE TABLE DEPARTMENT (
  DEPTNO CHAR(3) PRIMARY KEY,
  NAME VARCHAR(40)
);

CREATE TABLE EMPLOYEE (
  EMPNO CHAR(5) PRIMARY KEY,
  NAME VARCHAR(50),
  DEPTNO CHAR(3),
  FOREIGN KEY (DEPTNO) REFERENCES DEPARTMENT(DEPTNO)
);

CREATE TABLE DEPENDENT (
  EMPNO CHAR(5),
  DEPENDENT_NO INT,
  NAME VARCHAR(50),
  RELATION VARCHAR(20),
  PRIMARY KEY (EMPNO, DEPENDENT_NO),
  FOREIGN KEY (EMPNO) REFERENCES EMPLOYEE(EMPNO)
);
```

- `EMPLOYEE` is linked non-identifyingly to `DEPARTMENT`.  
- `DEPENDENT` is identified by `(EMPNO, DEPENDENT_NO)` — an identifying relationship.

---

## Visual Representation

```
DEPARTMENT (1) ───< EMPLOYEE (N)
EMPLOYEE (1) ───< DEPENDENT (N)
```

- `EMPLOYEE` references `DEPARTMENT` independently.  
- `DEPENDENT` cannot exist without its parent `EMPLOYEE`.

---

## Advantages of Principle 6

| Advantage | Description |
|------------|-------------|
| Uniqueness | Each row is identifiable |
| Integrity | Prevents duplicate or orphan records |
| Clarity | Defines dependency structure between entities |
| Maintainability | Simplifies database evolution and indexing |

---

## Exercises

### Exercise 1 — Identifying vs. Non-Identifying

> Model a database for *Orders*, *Customers*, and *Payments*.  
> Indicate which relationships are identifying and which are not.

### Exercise 2 — Surrogate Keys

> Redesign a table using surrogate keys instead of composite keys.  
> Discuss advantages and disadvantages.

---

## Summary

- Each table must have a **primary key**.  
- Relationships are either **identifying** or **non-identifying**.  
- Composite keys apply to identifying relationships.  
- Surrogate keys simplify schema design when natural keys are complex.

> ✅ **Design Rule:**  
> Every table must contain a stable, unique, and minimal primary key.

---
