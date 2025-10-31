# Chapter 3 — Principle 3½

---

## Introduction

Database design generally proceeds from **information requirements**.  
From these requirements, we determine **characteristics (attributes)**, which lead to **entities** and **tables**.  

This chapter introduces **Principle 3½**, a rule that helps identify *many-to-many relationships* that also include their own attributes.

---

## Example — Departments and Employees (Revisited)

Assume the following situation:

> Employees can work in more than one department,  
> but have **voting rights** in only one department.

### Characteristics List

```
dep_name  
dep_no  
budget  
function  
salary  
emp_name  
emp_no  
voting_right
```

Applying **Principles 1–3**, we create two entity tables:

```sql
CREATE TABLE DEPARTMENT (
  DEP_NO CHAR(3) PRIMARY KEY,
  DEP_NAME VARCHAR(40),
  BUDGET DECIMAL(10,2)
);

CREATE TABLE EMPLOYEE (
  EMP_NO CHAR(5) PRIMARY KEY,
  EMP_NAME VARCHAR(50),
  FUNCTION VARCHAR(30),
  SALARY DECIMAL(10,2)
);
```

---

## Identifying Missing Characteristics

The attribute **voting_right** has not yet been placed in either table.  
It refers to *a specific employee in a specific department* —  
thus, it belongs to neither entity individually.

We must therefore design a **new table** for this attribute.

---

### Derived Relationship Table

The **voting_rights** table connects employees and departments:

```sql
CREATE TABLE VOTING_RIGHTS (
  EMP_NO CHAR(5) REFERENCES EMPLOYEE(EMP_NO),
  DEP_NO CHAR(3) REFERENCES DEPARTMENT(DEP_NO),
  VOTING_RIGHT CHAR(1),
  PRIMARY KEY (EMP_NO, DEP_NO)
);
```

This structure also captures the **many-to-many** relationship between employees and departments,  
as each employee may work in several departments.

---

## Principle 3½ — Formal Definition

> 🧩 **Principle 3½**  
> For every attribute not yet included in any table,  
> determine which entities it describes.  
> Create a new table containing:
> - The combination of the primary keys of those entities as its own **primary key**  
> - The attribute(s) describing that relationship

This principle ensures that all *relationship-specific* attributes are modeled properly.

---

## Relationship to Other Principles

- **Principle 3½** complements, not replaces, Principles 4 and 5.  
- It automatically identifies **many-to-many relationships** that carry additional attributes.  
- It applies only when the attribute has not yet been represented elsewhere.  

| Case | Principle Used | Description |
|------|----------------|--------------|
| One-to-many relationship | Principle 4 | Add foreign key to “many” table |
| Many-to-many relationship without attributes | Principle 5 | Create linking table |
| Many-to-many relationship with attributes | Principle 3½ | Create linking table with extra fields |

---

## Example — “Table in a Table” Problem

A poor design often contains an entire table embedded within another table.  
Sometimes this redundancy is subtle.

### Scenario

> “The salary of an employee depends on years of service.”

### Incorrect Design

| emp_no | emp_name | function | years_of_service | salary |
|--------|-----------|-----------|------------------|--------|
| 001 | J. de Boer | Porter | 6 | 1800 |
| 002 | J. de Vries | Admin Emp | 10 | 2000 |
| 003 | J. Deelder | Admin Emp | 6 | 1800 |
| 004 | J. den Dolder | Overseer | 6 | 1800 |

### Issue

The relationship between **years_of_service** and **salary** is duplicated multiple times.

### Correct Normalized Design

```sql
CREATE TABLE EMPLOYEE (
  EMP_NO CHAR(5) PRIMARY KEY,
  EMP_NAME VARCHAR(50),
  FUNCTION VARCHAR(30),
  YEARS_OF_SERVICE INT
);

CREATE TABLE SALARY_SCALE (
  YEARS_OF_SERVICE INT PRIMARY KEY,
  SALARY DECIMAL(10,2)
);
```

Here, `SALARY` depends directly on `YEARS_OF_SERVICE`, not on the employee.  
The relationship has been extracted into its own table — avoiding redundancy.

---

## Interpretation of Principle 3

> In any table for a particular entity,  
> include **only direct attributes**, not **derived or indirect** ones.

**Example:**  
Salary is *derived* from years of service → it belongs in a separate table.

---

## Notation of Relationships

Standard diagrammatic notation for relationships:

```
┌───────┐          ┌───────┐           ┌───────┐
└───┬───┘          └───┬───┘           └───┬───┘
    │ 1                │ 1                 │ n
    │ one              │ one               │ many
    │ to               │ to                │ to
    │ one              │ many              │ many
    │ 1                │ n                 │ n
┌───┴───┐          ┌───┴───┐           ┌───┴───┐
└───────┘          └───────┘           └───────┘
```

This notation clearly represents **one-to-one**, **one-to-many**, and **many-to-many** relationships.

---

## Summary

- **Principle 3½** identifies attributes describing relationships between entities.  
- It generates new tables linking multiple entities through their primary keys.  
- It aids normalization and prevents redundancy.  
- Each table must contain only **direct** attributes of its entity type.

> ✅ **Good Design Rule:**  
> “Include only direct facts about the key — not facts about facts.”

---
