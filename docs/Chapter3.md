# Chapter 3 — Principle 3½

---

## INTRODUCTION

The normal course of affairs is that first the **information requirements** are determined and on the basis of that a list of **characteristics** is produced. Using this list, **entities** can be determined and the **database tables** can be designed.

Assume that in the **departments-employees** database it is given that **employees can work in more than one department**, but have a **voting right in only one department**. On the basis of the information requirements, the following list of characteristics can be created:
```

dep_name dep_no budget function salary emp_name emp_no voting_right

text

````
The database design according to **Principles 1–3** results in the following tables:

```text
departments(dep_no, dep_name, budget, ...)
employees(emp_no, emp_name, function, salary, ...)
````

**Principles 4 and 5** govern how the relationship between these entities must be processed in the design. However, one can also first examine which characteristics **have not yet been included** in any of the present tables.

In this example, it is the characteristic **voting_right**, which says something about a **particular employee in a particular department**.

This formulation makes it clear that this characteristic can **neither be taken up in departments nor in employees**. The consequence is that a **separate table must be designed** for it. The _italics_ make it immediately clear which key this new table must have — namely the **combination of emp_no and dep_no**:

text

```
voting_rightstable(emp_no, dep_no, voting_right)
```

> **Side Effect:** This treatment simultaneously processes the **many-to-many relationship** between employees and departments into the design. In this example, the application of **Principles 4 and 5** is **no longer necessary**.

This newly applied principle is **not found** in the book by C.J. Date and will therefore be indicated here as:

> 🧩 **Principle 3½** For every **characteristic not yet included** in a table, determine the **entities** this characteristic says something about. Then create a **new table** in which the **combination of primary keys** of the named entities appears as the **primary key**.

---

## How Principle 3½ Works

With **Principle 3½**, one thus finds **many-to-many relationships** that also have **one or more characteristics of their own**.

> **Note:** **Principle 3½ does _not_ render Principles 4 and 5 useless.** Many-to-many relationships **without** their own characteristics are **not found** with Principle 3½. In the case of **one-to-many relationships** (Principle 4), a characteristic already in use (as a primary key in the "one" table) is **included again** in another table. In the case of **Principle 3½**, however, it concerns **characteristics not yet in use**.

---

## A TABLE IN A TABLE

The **bad designs** from earlier chapters could also be characterized by the remark:

> _"There is a complete table within another table."_

In the poor designs, this is so striking that anyone will recognize it immediately. However, sometimes it is **much more subtle**.

Assume that in the description of the **departments-employees** database the following sentence is added:

> _"The salary of an employee depends on his years of service."_

The consequences become clear using a sample table:

|emp_no|emp_name|function|years_of_service|salary|
|---|---|---|---|---|
|001|J. de Boer|porter|6|1800|
|002|J. de Vries|adm. emp|10|2000|
|003|J. Deelder|adm. emp|6|1800|
|004|J. den Dolder|overseer|6|1800|

**Redundancy is present:** The fact that **6 years of service → salary 1800** is stored **multiple times**.

### Correct Solution

text

```
employees(emp_no, emp_name, function, years_of_service)
salaries(years_of_service, salary)
```

This reveals that in the original table, there was **a table within a table**.

- salary is a **characteristic of years_of_service**
- years_of_service is a **characteristic of employee** → salary is a **derived (indirect)** characteristic of the employee

> **Revised Interpretation of Principle 3:** In a table for a particular entity, **only direct characteristics** may be included — **no indirect or derived characteristics**.

---

## NOTATION OF RELATIONS

Relations can be notated in the following manner:

text

```
┌───────┐          ┌───────┐           ┌───────┐
└───┬───┘          └───┬───┘           └───┬───┘
    │ 1              │ 1                 │ n
    │  one           │  one              │  many
    │  to            │  to               │  to
    │  one           │  many             │  many
    │ 1              │ n                 │ n
┌───┴───┐          ┌───┴───┐           ┌───┴───┐
└───────┘          └───────┘           └───────┘
```

- **Left:**1:1 — One-to-One
- **Middle:**1:n — One-to-Many
- **Right:**n:n — Many-to-Many

---

## Summary

> ✅ **Principle 3½** is a **powerful discovery tool** for:
> 
> - **Many-to-many relationships with attributes**
> - **Hidden tables within tables**
> - **Indirect characteristics** violating clean entity design

It complements — but does **not replace** — Principles 4 and 5.

> **Rule of Thumb:** _Every piece of information belongs in **exactly one place** — and only in the table that **directly owns** it._