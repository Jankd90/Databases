# Chapter 1 — Database Design

---

## INTRODUCTION

Who does the database design in a **single-user system**? Of course, that single user does. But in a **shared system** no single end-user will have sufficient information to design the overall database in its entirety; instead, there will be some specially designated person—probably the **database administrator (DBA)**—who has that responsibility. That person will have to work with users to understand their individual requirements and will have to merge all those requirements together to produce an appropriate integrated design for the total database. Note, however, that individual users or user groups will be responsible for describing their own requirements to the DBA, and a good way of doing that is by producing a preliminary design for their own piece of the database. Thus even in a shared environment it is a good idea for users to have at least a basic knowledge of some of the principles of good design, even though they will probably not be responsible for the final overall design itself.

Database design is a big topic. Whole books have been written about it. Traditionally, it has always been regarded as a very difficult task, one involving highly specialized skills and consuming a great deal of time and effort. Now it is true that the design of large shared databases can indeed be quite difficult; but it is also true that the design of small and/or nonshared databases can be fairly easy. The design of large databases is not always difficult, either, especially in the newer systems. What is more, the design principles that apply to small databases are still applicable when the database is large; it is just that the design of large databases has to take into account a number of additional considerations that are not relevant to the small case. We content ourselves with identifying and illustrating some of the basic principles that apply to both cases.

As stated above, database design can be simple. Talking about it is frequently not! It is a fact that, in simple cases at least, it is often easier just to do the design than it is to try and explain exactly what it was you did. The reason for this state of affairs is that in order to talk about design in the abstract, it is necessary to introduce a certain amount of abstract terminology; and it is that terminology that is at the root of the problem. Papers on this topic typically involve a lot of abstract terms and tend therefore to be very difficult to read. I will do my best in what follows to be as concrete as possible. (Of course, I am saved from having to use a great deal of special terminology by the fact that I am not delving very deeply into the subject anyway. I am not denying the need for abstract terms in a more far-reaching discussion.)

Our discussion is divided into two pieces (corresponding to the two chapters). In each, we consider a simple example—one sufficiently simple that the "right" design is intuitively obvious—and then examine the question of exactly why that design is right. From these considerations we will extract some fundamental principles of good design, principles that (to repeat) apply to large databases as well as small ones.

> **Definition:**  
> *Database design* is the process of deciding what tables should exist and which fields they contain.

---

## DEPARTMENTS AND EMPLOYEES — A GOOD DESIGN

As stated in the "Introduction" section, database design is the process of deciding what tables you should have in the database and what fields those tables should contain. Our first example concerns **departments and employees**. To be more specific, we wish to design a simple personnel database, in which we need to represent (or model) the following situation:

- The company has some number of departments. As time progresses, new departments can be created and existing ones eliminated.  
- **Each Department:**  
  - Has a unique department number  
  - Has a name, manager, and budget  
  - Can employ zero or more employees  
  - A manager manages one department only  
- **Each Employee:**  
  - Has a unique employee number  
  - Has a name, job title, and salary  
  - Works in one department only  
  - Managers are considered to be in the department that they manage  

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
````

---

## ⚠️ Bad Design Example 1 — One Big Table

Now, why exactly is the design shown above the right one? Let us consider some alternatives. There are basically two possible alternatives, both involving a single table instead of two tables. The first involves moving employee information into the department table, yielding a wide, redundant structure:

text

```
deptno | name | mgr_empno | budget | empno_1 | name_1 | job_1 | salary_1 | ... | empno_9 | name_9 | job_9 | salary_9
```

### Problems

1. **Too wide**- The table is very wide. It will not fit conveniently on the screen or (more important) on a printed page. Reports from this database will be clumsy and difficult to read—a very practical consideration!
2. **Fixed limit** - We have had to set an upper limit (nine in the example) on the number of employees in a department. The first department to acquire a tenth employee will cause major disruption to the database and to programs that use the database.
3. **Null values** - Departments having fewer than nine employees will have records containing a lot of null values. For example, the record for a department with only three employees will contain many 'null' values, which is not very elegant and may waste storage space on the disk.
4. **Maintenance complexity** - It is likely that employee data for each department would be kept in some specific order within the department record—for example, by alphabetical order of employee names. Now consider the processing involved if a new employee joins the department, or if an employee leaves, or if an employee changes their name. Each of these changes will lead to an awkward shuffling of data within the record.
5. **Complex queries** - Which department is employee 61126 in?

sql

```
SELECT DEPTNO
FROM EMP
WHERE EMPNO_1 = '61126'
   OR EMPNO_2 = '61126'
   OR EMPNO_3 = '61126'
   OR EMPNO_4 = '61126'
   OR EMPNO_5 = '61126'
   OR EMPNO_6 = '61126'
   OR EMPNO_7 = '61126'
   OR EMPNO_8 = '61126'
   OR EMPNO_9 = '61126';
```

6. **Inefficient aggregate operations** - What is the average salary for department K82? First, find how many employees there are:

sql

```
SELECT NEMPS
FROM DEPT
WHERE DEPTNO = 'K82';
```

Suppose the result is 8. Then compute the average:

sql

```
SELECT (SALARY_1 + SALARY_2 + SALARY_3 + SALARY_4
      + SALARY_5 + SALARY_6 + SALARY_7 + SALARY_8) / 8
FROM DEPT
WHERE DEPTNO = 'K82';
```

---

## ✅ Correct Design and Queries

The normalized design uses two tables — **DEPARTMENT** and **EMPLOYEE**.

Instead of having one very wide record for each department, the correct design has (n + 1) records for each department (one DEPT record and n EMP records, where n is the number of employees).

Retrieve all employees in department M27:

sql

```
SELECT EMPNO, NAME, JOB, SALARY
FROM EMPLOYEE
WHERE DEPTNO = 'M27'
ORDER BY NAME;
```

Insert, delete, or update data easily:

sql

```
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

Which department is employee 61126 in?

sql

```
SELECT DEPTNO
FROM EMPLOYEE
WHERE EMPNO = '61126';
```

Average salary per department:

sql

```
SELECT AVG(SALARY)
FROM EMPLOYEE
WHERE DEPTNO = 'K82';
```

---

## ⚠️ Bad Design Example 2 — Department Data in Employee Table

The second alternative design is in effect the converse of the previous one. Instead of moving employee information into the department table, it moves department information into the employee table:

|empno|ename|job|Salary|deptno|dname|mgr_empno|budget|
|---|---|---|---|---|---|---|---|

Sample data:

|empno|ename|job|salary|deptno|dname|mgr_empno|budget|
|---|---|---|---|---|---|---|---|
|61126|Adams|Secretary|25K|M27|Education|42713|200K|
|42713|Cook|Manager|50K|M27|Education|42713|200K|
|50708|Smith|Instructor|30K|M27|Education|42713|200K|

### Problems

- **Redundant data** (repeated department info)
- **Wasted storage space**
- **Risk of inconsistency** - Example:

sql

```
UPDATE EMP
SET MGR_EMPNO = '12345'
WHERE EMPNO = '61126';
```

This leaves the database inconsistent (manager shown as 12345 in one row, 42713 in others).

- **Loss of department info when deleting last employee**
- **Cannot represent empty departments** - Cannot insert a new department with no employees due to primary key constraints.

---

## ✅ Correct Design Solutions

1. No redundancy → no waste of space.
2. No redundancy → no inconsistency. Department manager stored in exactly one place.
3. Deleting the only employee does not delete department:

sql

```
DELETE FROM EMPLOYEE
WHERE EMPNO = '61126';
```

Department record remains. 4. Insert empty department:

sql

```
INSERT INTO DEPARTMENT (DEPTNO, NAME, BUDGET)
VALUES ('H45', 'PUBLISHING', 400000);
```

---

## Discussion

From this example, several **design principles** arise.

> 🧩 **Principle 1** Represent each **entity type** as a separate table.

> 🧩 **Principle 2** Decide the **primary key** for each table. Values must be unique and not null.

> 🧩 **Principle 3** Assign each property of an entity type to a field in that entity’s table.

**Summary of structure:**

Each table consists of:

1. A primary key (unique identifier)
2. Zero or more attributes describing only that entity type

Bad designs violate this by including fields that describe other entities.

> **Rule of Thumb:** Each field represents _a fact about the key, the whole key, and nothing but the key._

---

## Relationships

Departments and employees have a **one-to-many** relationship:

- Each department has many employees
- Each employee belongs to one department

Representation:

text

```
DEPARTMENT (DEPTNO, NAME, MGR_EMPNO, BUDGET)
EMPLOYEE (EMPNO, NAME, JOB, SALARY, DEPTNO)
```

**Foreign key relationships:**

- EMPLOYEE.DEPTNO → DEPARTMENT.DEPTNO
- DEPARTMENT.MGR_EMPNO → EMPLOYEE.EMPNO

sql

```
ALTER TABLE EMPLOYEE
  ADD FOREIGN KEY (DEPTNO)
  REFERENCES DEPARTMENT(DEPTNO);

ALTER TABLE DEPARTMENT
  ADD FOREIGN KEY (MGR_EMPNO)
  REFERENCES EMPLOYEE(EMPNO);
```

> 🧩 **Principle 4** Represent each _one-to-many relationship_ by a foreign key in the "many" table referencing the "one" table.

---

## Summary

- **Entities → Tables**
- **Attributes → Fields**
- **Relationships → Foreign Keys**
- **Primary Keys → Uniquely identify each record**

> ✅ **Good database design** ensures stability, extensibility, and consistency. Each fact is stored _once_, in _one place_.

> 💡 **Definition: Entity** A distinguishable object about which data is stored. Examples: Department, Employee.

> 💡 **Definition: Attribute** A property describing an entity. Examples: Name, Salary, Budget.