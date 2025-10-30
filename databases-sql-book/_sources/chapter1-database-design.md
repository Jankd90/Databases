# Chapter 1: Database design

INTRODUCTION

Who does the database design in a single -user system, of course, that single user does? But in a shared
system no single end -user will have sufficient information to design the overalI database in its entirety;
instead, there will be some specially designated person --probably the database administrator (DBA) --
who has that responsibility. That person will have to work with users to under stand their individual
requirements and will have to merge all those require ments together to produce an appropriate
integrated design for the total database. Note, however, that individ ual users or user groups will be
respon sible for describing their own requirements to the DBA, and a good way of doing that is by
producing a preliminary design for their own piece of the d atabase. Thus even in a shared environment
it is a good idea for users to have at least a basic knowledge with some of the principles of good
design, even though they will probably not be responsible for the final overall design itself.
Database design is a big topic . Whole books have been writ ten about it. Traditionally, it has always
been regarded as a very difficult task, one involv ing highly specialized skills and consuming a great
deal of time and effort. Now it is true that the design of large shared databases can indeed be quite
difficult; but it is also true that the design of small and/or nonshared data bases can be fairly easy . The
design of large databases is not always difficult, either, especially in the newer systems. What is more,
the design principles that apply to small databases are still applicable when the database is large; it is
just that the design of large databases has to take into account a number of additional considerations
that are not rele vant to the small case. We content ourselves with identifying and illus trating some of
the basic principles that app ly to both cases.

As stated above, database design can be simple. Talking about it is frequently not! It is a fact that, in
simple cases at least, it is often easier just to do the design than it is to try and explain exactly what it
was you did. The reason for this state o f affairs is that in order to talk about design in the abstract, it is
necessary to introduce a certain amount of abstract terminol ogy; and it is that terminology that is at
the root of the problem. Papers on this topic typically involve a lot of abstract terms and tend therefore
to be very difficult to read. I will do my best in what follows to be as concrete as possible. (Of course,
I am saved from having to use a great deal of special terminology by the fact that I am not delving
very deeply into the su bject anyway. I am not denying the need for abstract terms in a more
far-reaching discussion.)

Our discussion is divided into two pieces (corresponding to the two chapters). In each, we consider a
simple example --one sufficiently simple that the "right" design is intuitively obvi ous--and then
examine the question of exactly why that design is right . From these considerations we will extract
some funda mental principles of good design, principles that (to repeat) apply to large databases as
well as small ones.

DEPARTMENTS AND EMPLOYEES: A GOOD DESIGN

As stated in the "Introduction" section, database design is the process of deciding what tables you
should have in the database and what fields those tables should contain. Our first example (a very bad
one, but none the worse for that) concerns depart ments and employees. To be more specific, we wish
to design a simple personnel database, in which we need to represent (or model) the following
situation:

 The company has some number of departments. As time progresses, new departments can be
created and existing ones eliminated.

 Each department has a department number (unique), a name, a manager, a budget, and a set
(possibly empty) of employees. No manager can manage more than one department at a time.

 Each employee has an employee number (unique), a name, a job, and a salary. Employees can leave
and join the company at any time. Every employee is in a department; no employee can be in more
than one department at a time. Managers are considered to be in the department that they manage.
(We are assuming a "flat" structure, for simplicity. That is, all departments are assumed to be at the
same level; there is no notion of one department containing other, lower -level departments, or of one
manager being se nior to another.)

 Department

Deptno
Name
Mgr_empno
budget

 Employee

Empno
Name
Job
Salary
deptno

DEPARTMENTS AND EMPLOYEES: A BAD DESIGN

Now, why exactly is the design shown above the right one? Let us consider some alterna tives. There
are basically two possible alternatives, both involving a single table instead of two tables . The first
involves moving employee information into the department table, yielding (say) a design of the form
shown in Fig. 1.1 (a table of 40 fields). The advantage of this design is that it is no longer necessary to
specify the department number for ea ch employee separately. But the disadvantages are obvious.
Among them are the following:

1. The table is very wide. It will not fit conveniently on the screen or (more important) on a printed
page. Reports from this database will be clumsy and difficult to read --a very practical considera tion!

2. We have had to set an upper limit (nine in the example) on the number of employees in a
department. The first department to acquire a tenth employee will cause major disruption to the data -
base and to programs that use the database.

 department
deptno name mgr_empno budget ......

 1st employee in this department
empno_1 name_1 job_1 salary_1 .......

 2nd employee in this department
empno_2 name_2 job_2 salary_2 ......

 last employee in this department
empno_9 name_9 job_9 salary_9 ......

3. Departments having fewer than nine employees will have records containing a lot of null values.
For example, the record for a department with only three employees will contain 24 'null' values (= no
values , 6 x 4 = 24 ), which is not very elegant and may waste storage space on the disk. (As a matter of
fact, each DEPT record in this design would probably include an additional field, NEMPS say, indicat ing
the number of employees it does have. That field could appear immedi ately following the BUDGET
field.)

4. It is likely that employee data for each department would be kept in some specific order within the
department record --for example, by alphabetical order of employee names, as in Fig. 1.2. (All fields
following SALARY_3 in that figure will be null, sinc e NEMPS is 3 for this department.) Now consider
the processing involved if a new employee (Clark) joins the depart ment, or if Adams leaves, or if the
instructor (Smith) gets married and changes her name to Anderson. Each of these changes will lead
to an a wkward shuffling of data within the record.

deptno name mgr_empno budgetno_emps nemps

M27 Education 42713 200K 3

 empno_1 name_1 job_1 salary_1
 61126 Adams Secretary 25K

 empno_2 name_2 job_2 salary_2
 42713 Cook Manager 50K

 empno_3 name_3 job_3 salary_3
 50708 Smith Instructor 30K

 empno_9 name_9 job_9 salary_9
 ? ? ? ?

5. Which department is employee 61126 in? In SQL ( Structural Query Language):

```
sql
SELECT DEPTNO
FROM EMP
WHERE EMPNO_1 = '61126'
```
OR EMPNO_2 = '61126'
OR EMPNO_3 = '61126'
OR EMPNO_4 = '61126'
OR EMPNO_5 = '61126'
OR EMPNO_6 = '61126'
OR EMPNO_7 = '61126'
OR EMPNO_8 = '61126'
OR EMPNO_9 = '61126'

6. Another example: "What is the average salary for department K82?" First, we need to find how many
employees there are in that department:

```
sql
SELECT NEMPS
FROM DEPT
WHERE DEPTNO = 'K82';
```

Suppose the result is 8. Then we compute the average salary as follows:

```
sql
SELECT (SALARY_1 + SALARY_2 + SALARY_3 + SALARY_4 + SALARY_5 + SALARY_6 + SALARY_7
```
+ SALARY_8) / 8
```
sql
FROM DEPT
WHERE DEPTNO = 'K82';
```

Now we consider briefly how the "right" design overcomes each of these problems:

1. Instead of having one very wide record for each department, the "right" design has (n + 1) records
for each department (one DEPT record and n EMP records, where n is the number of employees in the
department under consideration).

2. There is no upper limit on n.

3. A department with n employees will have exactly n EMP records. There is no question of an (n +
1)st record in which field values are null.

4. Ordering is not maintained within the database but is imposed on data as it is retrieved. For example:

```
sql
SELECT EMPNO, NAME, JOB, SALARY
FROM EMP
WHERE DEPNO = 'M27'
ORDER BY NAME;
```

Inserting, deleting, and updating records is straightforward and does not involve any awkward
shuffling of data:

```
sql
INSERT INTO EMP(.......,NAME,.........., DEPTNO)
```
VALUES (.......,'CLARK',......,'M27')

```
sql
DELETE FROM EMP
WHERE DEPTNO ='M27'
```
AND NAME = 'ADAMS';

```
sql
UPDATE EMP
```
SET NAME ='ANDERSON'
```
sql
WHERE DEPTNO = 'M27'
```
AND NAME = 'SMITH';

5. Which department is employee 61126 in?

```
sql
SELECT DEPTNO
FROM EMP
WHERE EMPNO = '61126';
```

6. What is the average salary in department K82?

```
sql
SELECT AVG(SALARY)
FROM EMP
WHERE DEPTNO = 'K82';
```

DEPARTMENTS AND EMPLOYEES: ANOTHER BAD DESIGN

The second alternative design for departments and employees is in effect, the converse of the previous
one. Instead of moving employee information into the department table, it moves department
information into the employee table, as follows:

empno ename job Salary deptno dname mgr_empno budget

Note that we have to distinguish between employee names and de partment names, so we have
renamed the fields concerned ENAME and DNAME, respectiveIy. Let us look at some sample data for
this design:

empno ename job salary deptno dname mgr_empno budget
------------------------------------------------------------------------------------------------------------------------
61126 Adams Secretary 25K M27 Education 42713 200K
42713 Cook Manager 50K M27 Education 42713 200K
50708 Smith Instructor 30K M27 Education 42713 200K
..... ..... ........ .... .... ......... ........ ......

The principal disadvantage is redun dancy, as the sample data above clearly illustrates. Some
consequences of that redundancy are as follows:

1. It is wasteful of storage space on the disk.

2. It is possible to update the database in such a way that it becomes incon sistent. For example, the
statement

```
sql
UPDATE EMP
```
SET MGR_EMPNO = '12345'
```
sql
WHERE EMPNO = '61126'
```

will leave the database in an inconsistent state (the manager for department M27 will be shown as
12345 in one record but as 42713 in others).

3. Suppose the department has just one employee in it. For example, suppose 61126 is the only
employee in department M27. If we delete that employee:

```
sql
DELETE
FROM EMP
WHERE EMPNO = '61126
```

then we lose all information about the department, too. (The department has become a department
with no employees in it, and the design is incapable of representing such a department.)

4. (This point is really the converse of the previous one.) Suppose a new department H45 (department
name Publishing, budget 400K, no manager yet assigned) has been established, but it contains no
employees as yet. Then we cannot conveniently insert that information into the database, because we
are not allowed to create a record such as

empno ename job salary deptno dname mgr_empno budget
-------------------------------------------------------------------------------------------------------------
? ? ? ? H45 Publishing ? 400K

The reason for this restriction is that EMPNO is the primary key of the EMP table, and primary keys are
usually not allowed to take on null values.

Once again let us consider briefly how the "right" design solves these prob lems.

 Department

Deptno
Name
Mgr_empno
budget

 Employee

Empno
Name
Job
Salary

1. There is no redundancy, so there is no waste of memory space.

2. There is no redundancy, so there cannot be any inconsistency. (Department M27's manager is given
in exactly one place --namely, in M27's DEPT record --so it cannot be shown as 12345 in one place and
42713 in another.)

3. If we delete the only employee (61126) in M27:

```
sql
DELETE
FROM EMP
WHERE EMPNO = '61126';
```

then no department information is lost. The record for M27 still exists in the DEPT table.

4. We can insert a department that has no employees:

```
sql
INSERT
```
INTO DEPT (DEPTNO, NAME, BUDGET)
VALUES ('H45', 'PUBLISHING', 400K)

DISCUSSION

Let us now try and analyze what is going on in this example and see if we can extract some broad and
useful principles from it. The situation to be modeled in the database involves two types of "entity"
(i.e., two basic kinds of object), namely, department s and employees, and in the "right" design each of
these entity types maps into a table of its own.
Hence we have the following:

 Principle 1:

Represent each entity type as a separate table.

Second, each individual entity (each individual department or employee in the real world) has its own
identifier unique with respect to all entities of the type in question, that is used to dis tinguish that
particular entity from all others of that type. The unique identifier for departments is of course
department number, that for employees is employee number. The se unique identifiers become
primary keys in the database design.

 Principle 2:

Decide the primary key for each table.

Values of the primary key of a table must be unique and must not be null. (We can now see the reason
for this "no nulls" restric tion, incidentally. A record with a null primary key value would have to
correspond to an entity with a null identifier; and an entity with a null identifier is an entity with no
identifier, which is a contradiction in terms. If there is no identifier, then there is no entity.)

Each entity has certain properties : Departments have names, budgets, and so on; employees have
jobs, salaries, and so on. These properties are represented by fields within the entity tables.

 Principle 3:

Assign each property of an entity type to a field within the table representing that entity type.

By following these three principles, we will always finish up with a design that conforms to the
following simple pattern:

Each table consists of:
1. a primary key, representing the unique identifier for some particular entity type;

together with
2. zero or more additional fields, representing properties of the entity type identified by the primary
key and not of some other entity type.

Both of the bad designs shown earlier fail to conform to this simple pattern. In the first case DEPT
records included fields (such as SALARY_1, SALARY_2, etc.) that represented properties of employees
rather than departments. In the second case EMP records included fields (such as BUDGET, DNAME,
etc.) that represented properties of departments rather than employees. As a result, the (single) table
in each case was overloaded with informa tion. The three prin ciples stated above, by contrast, will lead
to a clean design in which each table contains information about one entity type only. That clean
design will be easier to understand, easier to use, and (most important) easier to extend if new
informa tion is to be added to the database later on. In a nutshel l, the design will be stable and will be
a good foundation for future growth.

Another way of expressing the clean design objective is: One fact in one place. Each "fact" (e.g., the
fact that a given department has a given budget) appears at exactly one place in the design. Yet
another way of characterizing it (very informally) is: E ach field represents a fact about the key, the
whole key, and nothing but the key (where "key" is shorthand for "entity identified by the primary key
of the table that contains the field in question").

So far we have said nothing about the relationship that con nects the two entity types in the example
(i.e., the relationship between departments and employees). In fact, departments and employees
provide the standard example of a one -to-many rela tionship : For each department there are many
correspon ding employees (where "many" includes the possibilities of one and zero, of course). This
relationship must be understood to be directed (from depart ments to employees); the converse
relationship, from employ ees to depart ments, is many -to-one (many employees have the same
department). The example illus trates how such relationships are represented in the database: The
"many" table (EMP in the example) includes a foreign key (field EMP.DEPTNO), whose values ma tch
values of the primary key (field DEPT.DEPTNO) of the "one" table (table DEPT). Schematically , we have
the situation shown in Fig. 1.3.

As a matter of fact, there is another relationship that holds be tween DEPTs and EMPs: Each department
has a manager, and that manager is of course an employee. (That relationship is one -to-one: Each
department has exactly one manager. "One -to-one" is jus t a speciaI case of "one -to-many," however.)
So we have an other foreign -key primary -key match: Field DEPT.MGR_ EMPNO is a foreign key in the
DEPT table that matches the pri mary key (EMP.EMPNO) of the EMP table.
Figure 1.4 shows both matches:

DEPARTMENT
deptno name mgr_empno budget

 EMPLOYEE
empno name job salary deptno

primary key foreign key
stated that: department.deptno = employee.deptno

DEPARTMENT
deptno name mgr_empno budget
primary key foreign key

 EMPLOYEE
empno name job salary deptno
primary key foreign key

stated that: department.deptno = employee.deptno
or department.mgr_empno = employee.empno

figure figure 1.4

An alternative design would drop the foreign key MGR_EMPNO from the DEPT table and would add a
foreign key MGR_DEPTNO (say) to the EMP table, representing the depart ment managed by the
employee in question. See Fig. 1.5. How ever, this design is less satisfactory because it involves a lot
of null values (MGR_DEPTNO will be null for every employee who is not a manager). But it does
illustrate a point that we have not ex plicity mentioned before --namely, that the general rule for for eign
keys is not that each value of the foreign key must be equal to some existing primary key value, but
rather that each value of the foreign key either must be equal to some existing primary key value or
must be null. Sometimes, of course, null values will not be allowed; for example, the foreign key
EMP .DEPTNO is not allowed to take on null values, since every employee must be in a department.

Aside : To describe departments -to-managers as on e-to-one is in fact an over simplification. A more
accurate statement is as follows: For one department there is either one manager or none (allowing
for the case in which no manager is yet assigned); for one employee there is either one department or
none that is managed by that employee. The relationship is thus really "(zero -or-one)-to-(zero -or-one)."
But it is u sual to ignore such refinements in informal discussion.

DEPARTMENT
deptno name budget
primary key

EMPLOYEE
empno name job salary deptno mgr_deptno
primary key foreignkey foreign key

stated that: department.deptno = employee.deptno
or department.deptno = employee. mgr_deptno

To return to the main topic: Foreign -key/primary -key matches are the glue that holds the database
together. Identifying those matches is a crucial part of the database design process. So we have the
following:

 Principle 4:

Represent each one -to-many relationship between entity types by a foreign key in the "many" table
that matches the primary key of the "one" table.
