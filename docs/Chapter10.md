# Chapter 10 — Principle 10

---

## Introduction

In this final stage of relational database design, **Principle 10** addresses the treatment of **redundant relationships** and **derived connections**.  
It ensures that every relationship represented in the database is **logically necessary** and not derivable from existing ones.

This principle completes the normalization process by enforcing **semantic minimalism** — storing only essential relationships.

---

## Redundant Relationships

A *redundant relationship* occurs when a connection between two entities can be **derived** through other relationships.

### Example — Departments, Employees, and Projects

Assume:
- Each **Department** employs multiple **Employees**.
- Each **Employee** works on one or more **Projects**.
- Each **Project** is managed by one **Department**.

Diagrammatically:

```
DEPARTMENT ──< EMPLOYEE ──< WORKS_ON >── PROJECT
  │                                     ^
  └─────────────────────────────────────┘
```

The direct link between `DEPARTMENT` and `PROJECT` is **redundant**, since it can be derived through `EMPLOYEE`.

---

## Principle 10 — Formal Definition

> 🧩 **Principle 10**  
> Eliminate any relationship that can be **logically derived** from existing relationships between the same entities.

This principle avoids unnecessary duplication, circular dependencies, and inconsistent data paths.

---

## Example — Correct Design

We represent only the **essential** relationships.

```sql
CREATE TABLE DEPARTMENT (
  DEPTNO CHAR(3) PRIMARY KEY,
  NAME VARCHAR(40)
);

CREATE TABLE EMPLOYEE (
  EMPNO CHAR(5) PRIMARY KEY,
  NAME VARCHAR(50),
  DEPTNO CHAR(3) REFERENCES DEPARTMENT(DEPTNO)
);

CREATE TABLE PROJECT (
  PROJNO CHAR(4) PRIMARY KEY,
  DESCRIPTION VARCHAR(100)
);

CREATE TABLE WORKS_ON (
  EMPNO CHAR(5) REFERENCES EMPLOYEE(EMPNO),
  PROJNO CHAR(4) REFERENCES PROJECT(PROJNO),
  PRIMARY KEY (EMPNO, PROJNO)
);
```

No direct `DEPARTMENT–PROJECT` relationship is stored, since it can be derived through `EMPLOYEE`.

---

### Derivation Query Example

To find which departments manage which projects:

```sql
SELECT DISTINCT E.DEPTNO, W.PROJNO
FROM EMPLOYEE E
JOIN WORKS_ON W ON E.EMPNO = W.EMPNO;
```

This query derives the implicit relationship without duplicating data.

---

## Incorrect Design — Redundant Relationship

If we add a direct link between `DEPARTMENT` and `PROJECT`:

```sql
CREATE TABLE DEPT_PROJECT (
  DEPTNO CHAR(3) REFERENCES DEPARTMENT(DEPTNO),
  PROJNO CHAR(4) REFERENCES PROJECT(PROJNO),
  PRIMARY KEY (DEPTNO, PROJNO)
);
```

This relationship can already be deduced via `EMPLOYEE`.  
Its presence creates **redundancy** and risks **inconsistency** — if data changes in `WORKS_ON`, `DEPT_PROJECT` may no longer match.

---

### Example of Inconsistency

| EMPLOYEE |        |        |
|-----------|--------|--------|
| EMPNO | NAME | DEPTNO |
|--------|------|--------|
| 1001 | Adams | D1 |
| 1002 | Brown | D1 |

| WORKS_ON |        |        |
|-----------|--------|--------|
| EMPNO | PROJNO |
|--------|--------|
| 1001 | P1 |
| 1002 | P2 |

| DEPT_PROJECT |        |        |
|---------------|--------|--------|
| DEPTNO | PROJNO |
|--------|--------|
| D1 | P1 |

Here, Project P2 belongs to Department D1 via `WORKS_ON`, but `DEPT_PROJECT` fails to record it — resulting in inconsistency.

---

## Logical vs. Physical Redundancy

| Type | Description | Example |
|------|--------------|----------|
| **Logical redundancy** | Relationship can be inferred via joins | DEPARTMENT–PROJECT via EMPLOYEE |
| **Physical redundancy** | Duplicate data stored in multiple tables | Repeated department name in employee records |

Principle 10 eliminates **logical redundancy**, complementing earlier principles that remove **physical redundancy**.

---

## Relationship Dependency Rules

To determine redundancy:
1. Identify all relationships among entities.
2. Check whether one relationship can be inferred via others.
3. Remove any that can be derived through joins or transitive dependencies.

---

## Practical Example — Students, Courses, Instructors

### Scenario

> Each course is taught by one instructor.  
> Each student enrolls in many courses.  
> Which instructor teaches which student?

Derived relationship: `STUDENT` → `COURSE` → `INSTRUCTOR`.

### Correct Schema

```sql
CREATE TABLE STUDENT (
  STU_ID CHAR(5) PRIMARY KEY,
  NAME VARCHAR(50)
);

CREATE TABLE COURSE (
  COURSE_ID CHAR(5) PRIMARY KEY,
  TITLE VARCHAR(50),
  INSTRUCTOR_ID CHAR(5)
);

CREATE TABLE ENROLLMENT (
  STU_ID CHAR(5) REFERENCES STUDENT(STU_ID),
  COURSE_ID CHAR(5) REFERENCES COURSE(COURSE_ID),
  PRIMARY KEY (STU_ID, COURSE_ID)
);
```

We avoid a direct `STUDENT–INSTRUCTOR` table — it is derivable via `ENROLLMENT` and `COURSE`.

---

### Derived Query

```sql
SELECT S.STU_ID, S.NAME, I.INSTRUCTOR_ID
FROM STUDENT S
JOIN ENROLLMENT E ON S.STU_ID = E.STU_ID
JOIN COURSE I ON E.COURSE_ID = I.COURSE_ID;
```

This query produces the implicit `STUDENT–INSTRUCTOR` relationship.

---

## Principle Interaction

| Principle | Focus | Relation to Principle 10 |
|------------|--------|--------------------------|
| 4 | One-to-many | Introduces directional relationships |
| 5 | Many-to-many | Defines link tables |
| 7 | Direction of relationships | Ensures logical clarity |
| 10 | Redundant relationships | Removes unnecessary ones |

Principle 10 thus acts as the **final refinement**, ensuring the model is semantically minimal.

---

## Exercises

### Exercise 1 — Redundant Relationships

> Given the entities `Supplier`, `Part`, and `Shipment`, determine if a direct `Supplier–Warehouse` table is necessary when shipments already record warehouse data.

### Exercise 2 — Derivation Validation

> Design SQL queries to verify whether a relationship between `Course` and `Department` can be derived via `Instructor`.

---

## Summary

- **Principle 10** eliminates redundant or derivable relationships.  
- Ensures all relationships in the model are **semantically necessary**.  
- Prevents **inconsistency** and **circular dependencies**.  
- Completes the normalization framework introduced by earlier principles.

> ✅ **Design Rule:**  
> Store only relationships that cannot be derived logically from others.

---
