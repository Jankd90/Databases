# Chapter 7 — Principle 7

---

## Introduction

Up to this point, database design has focused on ensuring data integrity and proper representation of entities and relationships.  
In this chapter, we introduce **Principle 7**, which concerns the **direction of relationships** and how to correctly assign foreign keys when multiple valid alternatives exist.

This principle helps eliminate **redundant paths** and **circular references** in database design.

---

## Direction of Relationships

When two entities are related, the relationship can be represented by a **foreign key** in either table.  
However, to maintain logical consistency and simplicity, the direction must be chosen carefully.

> 💡 **Example:**  
> A *department* has a *manager*, and an *employee* manages a *department*.  
> Should the foreign key appear in `EMPLOYEE` or `DEPARTMENT`?

---

## Example — Departments and Managers

### 1. Entities

**DEPARTMENT**
- DEPTNO — Department number (unique)  
- DNAME — Department name  
- MGR_EMPNO — Manager’s employee number  

**EMPLOYEE**
- EMPNO — Employee number (unique)  
- ENAME — Name  
- JOB — Job title  
- SALARY — Salary  

---

### 2. Relationship Analysis

Each department has **one manager**, and an employee can manage **at most one department**.

This is a **one-to-one relationship**.

Two possible representations exist:

**Option A:**  
Foreign key `MGR_EMPNO` in `DEPARTMENT` → points to `EMPLOYEE`.

```sql
CREATE TABLE DEPARTMENT (
  DEPTNO CHAR(3) PRIMARY KEY,
  DNAME VARCHAR(40),
  MGR_EMPNO CHAR(5),
  FOREIGN KEY (MGR_EMPNO) REFERENCES EMPLOYEE(EMPNO)
);
```

**Option B:**  
Foreign key `DEPTNO` in `EMPLOYEE` → points to `DEPARTMENT`.

```sql
CREATE TABLE EMPLOYEE (
  EMPNO CHAR(5) PRIMARY KEY,
  ENAME VARCHAR(40),
  JOB VARCHAR(30),
  SALARY DECIMAL(10,2),
  DEPTNO CHAR(3),
  FOREIGN KEY (DEPTNO) REFERENCES DEPARTMENT(DEPTNO)
);
```

---

### 3. Choosing the Correct Direction

Although both designs are logically possible, **Option A** is preferred.

| Criteria | Reason |
|-----------|--------|
| Clarity | The department “has” a manager — relationship direction reflects this. |
| Simplicity | Each department references one manager (a clear one-to-one mapping). |
| Avoids Redundancy | The employee table already identifies employees; adding a department reference may duplicate information. |

Thus, the **foreign key should reside in the DEPARTMENT table**, referencing the employee who manages it.

---

## Principle 7 — Formal Definition

> 🧩 **Principle 7**  
> When several equivalent relationship representations are possible,  
> **choose the one that minimizes redundancy** and **most clearly expresses the semantic meaning** of the relationship.

---

## Example — Supervisor Relationships

Consider the **employee-supervisor** relationship:

> Each employee has one supervisor, who is also an employee.

Both entities are of the same type (recursive relationship).

### Schema

```sql
CREATE TABLE EMPLOYEE (
  EMPNO CHAR(5) PRIMARY KEY,
  ENAME VARCHAR(40),
  JOB VARCHAR(30),
  SALARY DECIMAL(10,2),
  SUPERVISOR CHAR(5),
  FOREIGN KEY (SUPERVISOR) REFERENCES EMPLOYEE(EMPNO)
);
```

Here, `SUPERVISOR` is a **self-referencing foreign key** in the same table.

---

### Example Query — Recursive Relationship

Retrieve all employees with their supervisors:

```sql
SELECT E.ENAME AS EMPLOYEE, S.ENAME AS SUPERVISOR
FROM EMPLOYEE E
LEFT JOIN EMPLOYEE S ON E.SUPERVISOR = S.EMPNO;
```

This illustrates the **hierarchical structure** within a single entity type.

---

## Avoiding Redundant Paths

Incorrect placement of foreign keys can lead to **circular references**, where two tables reference each other.

### Example — Bad Design

```sql
CREATE TABLE DEPARTMENT (
  DEPTNO CHAR(3) PRIMARY KEY,
  MGR_EMPNO CHAR(5),
  FOREIGN KEY (MGR_EMPNO) REFERENCES EMPLOYEE(EMPNO)
);

CREATE TABLE EMPLOYEE (
  EMPNO CHAR(5) PRIMARY KEY,
  DEPTNO CHAR(3),
  FOREIGN KEY (DEPTNO) REFERENCES DEPARTMENT(DEPTNO)
);
```

This design causes ambiguity and mutual dependency during insertion and deletion.

**Solution:**  
Keep only one directional link — either `DEPTNO` in `EMPLOYEE` **or** `MGR_EMPNO` in `DEPARTMENT`, not both.

---

## Example — Projects and Managers

> Each project has one manager, who is also an employee.

Correct representation:

```sql
CREATE TABLE PROJECT (
  PROJNO CHAR(4) PRIMARY KEY,
  DESCRIPTION VARCHAR(100),
  MGR_EMPNO CHAR(5),
  FOREIGN KEY (MGR_EMPNO) REFERENCES EMPLOYEE(EMPNO)
);
```

This maintains direction from “project → manager,” reflecting real-world meaning.

---

## One-to-One Relationship Guidelines

| Scenario | Recommended Design |
|-----------|--------------------|
| Each entity in Table A corresponds to exactly one in Table B | Choose one side to hold the foreign key (not both). |
| The relationship represents *ownership* | The owner table should contain the foreign key. |
| Either table may exist without the other | Avoid mandatory foreign key dependencies. |

---

## Exercises

### Exercise 1 — Choosing Direction

> Model the relationship between *Vehicle* and *Driver* where each driver can have one assigned vehicle, and each vehicle has exactly one driver.  
> Decide where the foreign key should go and justify your choice.

### Exercise 2 — Self-Referencing Key

> Create a recursive relationship in which each employee reports to another employee.  
> Write SQL queries to display each employee’s supervisor.

---

## Summary

- Relationships can often be represented in multiple ways.  
- **Principle 7** ensures the chosen direction avoids redundancy and reflects real-world semantics.  
- Circular foreign key dependencies must be avoided.  
- For one-to-one or self-referencing relationships, choose the **simplest, most expressive direction**.

> ✅ **Design Rule:**  
> Prefer the foreign key placement that minimizes redundancy and mirrors logical ownership.

---
