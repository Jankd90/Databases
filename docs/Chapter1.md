# Chapter 1 — Database Design

---

## Introduction

Database design defines the structure of data storage.

In a **single-user system**, the user usually designs the database.  
In a **shared system**, a **Database Administrator (DBA)** integrates requirements from multiple users and designs the total database.

Database design may be simple or complex, depending on scope.  
The same fundamental principles apply to both small and large systems.

> **Definition:**  
> *Database design* is the process of deciding what tables should exist and which fields they contain.

---

## Departments and Employees — A Good Design

A company has multiple departments.  

**Each Department:**
- Has a unique department number  
- Has a name, manager, and budget  
- Can employ zero or more employees  
- A manager manages one department only  

**Each Employee:**
- Has a unique employee number  
- Has a name, job title, and salary  
- Works in one department only  

**Relational Schema:**

```sql
CREATE TABLE DEPARTMENT (
  DEPTNO CHAR(3) PRIMARY KEY,
  NAME VARCHAR(50),
  MGR_EMPNO CHAR(5),
  BUDGET DECIMAL(10,2)
);

CREATE TABLE EMPLOYEE (
  EMPNO CHAR(5) PRIMARY KEY,
  NAME VARCHAR(50),
  JOB VARCHAR(30),
  SALARY DECIMAL(10,2),
  DEPTNO CHAR(3) REFERENCES DEPARTMENT(DEPTNO)
);
```

---

## ⚠️ Bad Design Example 1 — One Big Table

If employee data is merged into the department table, the result is a wide, redundant structure:

```
DEPTNO | NAME | MGR_EMPNO | BUDGET | EMPNO_1 | NAME_1 | JOB_1 | SALARY_1 | ... | EMPNO_9 | NAME_9 | JOB_9 | SALARY_9
```

### Problems

1. **Too wide** — Difficult to display or print.  
2. **Fixed limit** — Only a set number of employees can exist.  
3. **Null values** — Departments with fewer employees waste storage.  
4. **Maintenance complexity** — Adding or deleting an employee causes field shuffling.  
5. **Complex queries:**

```sql
SELECT DEPTNO
FROM EMP
WHERE EMPNO_1 = '61126'
   OR EMPNO_2 = '61126'
   OR EMPNO_3 = '61126';
```

6. **Inefficient aggregate operations:**

```sql
SELECT (SALARY_1 + SALARY_2 + SALARY_3 + SALARY_4
      + SALARY_5 + SALARY_6 + SALARY_7 + SALARY_8) / 8
FROM DEPT
WHERE DEPTNO = 'K82';
```

---

## ✅ Correct Design and Queries

The normalized design uses two tables — **DEPARTMENT** and **EMPLOYEE**.

Retrieve all employees in department `M27`:

```sql
SELECT EMPNO, NAME, JOB, SALARY
FROM EMPLOYEE
WHERE DEPTNO = 'M27'
ORDER BY NAME;
```

Insert, delete, or update data easily:

```sql
INSERT INTO EMPLOYEE (EMPNO, NAME, JOB, SALARY, DEPTNO)
VALUES ('50901', 'CLARK', 'INSTRUCTOR', 32000, 'M27');

DELETE FROM EMPLOYEE
WHERE DEPTNO = 'M27'
  AND NAME = 'ADAMS';

UPDATE EMPLOYEE
SET NAME = 'ANDERSON'
WHERE DEPTNO = 'M27'
  AND NAME = 'SMITH';
```

Average salary per department:

```sql
SELECT AVG(SALARY)
FROM EMPLOYEE
WHERE DEPTNO = 'K82';
```

---

## ⚠️ Bad Design Example 2 — Department Data in Employee Table

If department details are stored with every employee record:

| EMPNO | ENAME | JOB | SALARY | DEPTNO | DNAME | MGR_EMPNO | BUDGET |
|-------|--------|-----|--------|--------|--------|------------|--------|
| 61126 | Adams | Secretary | 25K | M27 | Education | 42713 | 200K |
| 42713 | Cook | Manager | 50K | M27 | Education | 42713 | 200K |

### Problems

- **Redundant data** (repeated department info)  
- **Wasted storage space**  
- **Risk of inconsistency**  
- **Loss of department info when deleting last employee**  
- **Cannot represent empty departments**

### Example of inconsistency

```sql
UPDATE EMP
SET MGR_EMPNO = '12345'
WHERE EMPNO = '61126';
```

This would make the department manager inconsistent across rows.

---

## Discussion

From this example, several **design principles** arise.

> 🧩 **Principle 1**  
> Represent each **entity type** as a separate table.

> 🧩 **Principle 2**  
> Decide the **primary key** for each table.

> 🧩 **Principle 3**  
> Assign each property of an entity type to a field in that entity’s table.

**Summary of structure:**

Each table consists of:
1. A primary key (unique identifier)  
2. Zero or more attributes describing only that entity type  

Bad designs violate this rule by including fields that describe other entities.

> **Rule of Thumb:**  
> Each field represents *a fact about the key, the whole key, and nothing but the key.*

---

## Relationships

Departments and employees have a **one-to-many** relationship:
- Each department has many employees.
- Each employee belongs to one department.

Representation:

```
DEPARTMENT (DEPTNO, NAME, MGR_EMPNO, BUDGET)
EMPLOYEE (EMPNO, NAME, JOB, SALARY, DEPTNO)
```

**Foreign key relationships:**
- `EMPLOYEE.DEPTNO → DEPARTMENT.DEPTNO`
- `DEPARTMENT.MGR_EMPNO → EMPLOYEE.EMPNO`

```sql
ALTER TABLE EMPLOYEE
  ADD FOREIGN KEY (DEPTNO)
  REFERENCES DEPARTMENT(DEPTNO);

ALTER TABLE DEPARTMENT
  ADD FOREIGN KEY (MGR_EMPNO)
  REFERENCES EMPLOYEE(EMPNO);
```

> 🧩 **Principle 4**  
> Represent each *one-to-many relationship* by a foreign key in the "many" table referencing the "one" table.

---

## Summary

- **Entities → Tables**  
- **Attributes → Fields**  
- **Relationships → Foreign Keys**  
- **Primary Keys → Uniquely identify each record**

> ✅ **Good database design** ensures stability, extensibility, and consistency.  
> Each fact is stored *once*, in *one place*.

---

> 💡 **Definition: Entity**
> A distinguishable object about which data is stored.  
> Examples: Department, Employee.

> 💡 **Definition: Attribute**
> A property describing an entity.  
> Examples: Name, Salary, Budget.

---
