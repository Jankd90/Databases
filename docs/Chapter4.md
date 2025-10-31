# Chapter 4 — Principle 4

---

## Introduction

In the previous chapters, we developed database design principles for entities and relationships.  
This chapter introduces **Principle 4**, which deals with representing **one-to-many relationships** between entities.

---

## Example — Departments and Employees

We revisit the familiar scenario:

> A company has several departments, each employing multiple employees.  
> Each employee works in exactly one department.

From this, we identify a **one-to-many relationship**:
- **One department** → many employees  
- **Each employee** → one department

---

### Step 1 — Entities and Attributes

**DEPARTMENT**
- DEPTNO — Department number (unique)  
- NAME — Department name  
- MGR_EMPNO — Manager’s employee number  
- BUDGET — Department budget  

**EMPLOYEE**
- EMPNO — Employee number (unique)  
- NAME — Employee name  
- JOB — Job title  
- SALARY — Monthly salary  

---

### Step 2 — Relational Schema

To represent the one-to-many relationship, add a **foreign key** to the “many” side — the `EMPLOYEE` table.

```sql
CREATE TABLE DEPARTMENT (
  DEPTNO CHAR(3) PRIMARY KEY,
  NAME VARCHAR(40),
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

### Step 3 — Data Example

| DEPTNO | NAME | MGR_EMPNO | BUDGET |
|--------|------|------------|---------|
| M27 | Education | 42713 | 200000 |
| K82 | IT | 53321 | 300000 |

| EMPNO | NAME | JOB | SALARY | DEPTNO |
|-------|------|-----|---------|--------|
| 61126 | Adams | Secretary | 25000 | M27 |
| 42713 | Cook | Manager | 50000 | M27 |
| 53321 | Smith | Analyst | 42000 | K82 |
| 55902 | Lee | Developer | 39000 | K82 |

---

### Step 4 — Example Queries

Retrieve all employees from a specific department:

```sql
SELECT EMPNO, NAME, JOB, SALARY
FROM EMPLOYEE
WHERE DEPTNO = 'M27'
ORDER BY NAME;
```

Calculate the average salary per department:

```sql
SELECT DEPTNO, AVG(SALARY)
FROM EMPLOYEE
GROUP BY DEPTNO;
```

Retrieve departments with budgets over 250,000:

```sql
SELECT NAME, BUDGET
FROM DEPARTMENT
WHERE BUDGET > 250000;
```

---

## Principle 4 — Formal Definition

> 🧩 **Principle 4**  
> Represent each *one-to-many* relationship by including the **primary key** of the “one” table as a **foreign key** in the “many” table.

This ensures referential integrity and allows efficient retrieval of related data.

---

## Example — Projects and Tasks

Consider another case:

> Each project consists of multiple tasks.  
> Each task belongs to one project.

### Schema

```sql
CREATE TABLE PROJECT (
  PROJNO CHAR(4) PRIMARY KEY,
  DESCRIPTION VARCHAR(80)
);

CREATE TABLE TASK (
  TASKNO CHAR(5) PRIMARY KEY,
  DESCRIPTION VARCHAR(80),
  HOURS INT,
  PROJNO CHAR(4) REFERENCES PROJECT(PROJNO)
);
```

Here, `PROJNO` in `TASK` represents the one-to-many relationship between projects and tasks.

---

## Visual Representation

```
DEPARTMENT (1) ──────────< EMPLOYEE (N)
     │                        │
     │                        │
  Primary Key             Foreign Key (DEPTNO)
```

The arrow indicates that many employees belong to one department.

---

## Referential Integrity

The **foreign key constraint** guarantees that:

- Every `EMPLOYEE.DEPTNO` exists in `DEPARTMENT.DEPTNO`.  
- No employee can reference a non-existent department.

### Example of Violation

```sql
INSERT INTO EMPLOYEE (EMPNO, NAME, JOB, SALARY, DEPTNO)
VALUES ('88888', 'Clark', 'Trainer', 28000, 'Z99');
```

If department `Z99` doesn’t exist, the system rejects the insertion.

---

## Deletion and Update Rules

Foreign key constraints can specify **referential actions**.

```sql
ALTER TABLE EMPLOYEE
ADD CONSTRAINT FK_DEPT
FOREIGN KEY (DEPTNO)
REFERENCES DEPARTMENT(DEPTNO)
ON DELETE CASCADE
ON UPDATE CASCADE;
```

- **ON DELETE CASCADE:** Deleting a department automatically deletes all employees in it.  
- **ON UPDATE CASCADE:** Changing a department number updates all references.

Use cascading actions cautiously to prevent accidental mass deletions.

---

## Comparison with Other Relationships

| Relationship Type | Implementation |
|--------------------|----------------|
| One-to-One | Either table may contain foreign key |
| One-to-Many | “Many” table includes foreign key |
| Many-to-Many | Create separate linking table |

---

## Exercises

### Exercise 1 — Courses and Students

> Each course may have several students.  
> Each student takes exactly one course.

Design the tables `COURSE` and `STUDENT`, showing the foreign key relationship.

---

### Exercise 2 — Referential Integrity Test

Add a record to the “many” table referencing a non-existent record in the “one” table.  
Observe the system’s response.

---

## Summary

- Principle 4 handles **one-to-many** relationships.  
- Implemented by placing a **foreign key** in the “many” table.  
- Ensures **referential integrity**.  
- Cascading options control how deletions and updates propagate.

> ✅ **Design Rule:**  
> Every foreign key enforces a valid, consistent relationship between entities.

---
