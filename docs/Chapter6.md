# Chapter 6 — Questions

---

## The Superclean Company

The **Superclean** cleaning company is a business with **20 branches** in the **Benelux** territory which cleans **office buildings**, **factories**, **sports halls**, and such-like.

For the **building (or buildings)** of each **customer**, it is known whether the cleaning must take place **before or just after office hours**. On the basis of the **number of square metres** and possible **special circumstances**, how many **man-hours** and what **materials** may be required each day for a particular customer is specified.

The cleaning is done as far as possible by a **fixed team** of cleaners, of which **one functions as overseer**. The **materials required** for the work are usually kept in the **building which is to be cleaned**. The overseer is responsible for **replenishing the stock** of cleaning materials and places an **order** for this to the **stores** at his/her **branch** of Superclean. In addition, the overseer **distributes the work** and the materials amongst the cleaners. He notifies the **absence of cleaners** to the **personnel department**.

The work carried out is checked by an **inspector** from Superclean, who is also responsible for dealing with the **customers** and their **wishes**. The inspector obtains from the company's **information system** a **monthly report** and a **summary of materials used** at the customer's premises and can in this way check whether the **consumption** for a particular customer remains within the **norms** which have been set.

For these matters, the inspector can contact the **overseer**. If necessary, the inspector gives relevant information to **financial administration**.

**Potential customers** can ask for a **tender**. The inspector for the relevant **district** goes to visit the potential customer at his premises. Then possibly a **contract** is concluded which is deposited with **financial administration**. Each branch has a **planning department** which assembles a **cleaning team** for each building, designates an **overseer**, and provides the persons and departments in question with relevant information.

Each branch also has a **personnel department** which recruits new cleaners and sorts out which present and new employees have the capabilities to function as an overseer.

At the **head office** of Superclean there is also a **personnel department**. This concerns itself with the **personnel management** at the head office but also with the **recruitment and appointment** of more highly trained staff for the branches, such as inspectors and managers of branches.

The **purchasing of cleaning materials** is controlled centrally from the head office of Superclean. To the companies which supply such materials, the **order** is given to deliver the quantities required **directly to the Superclean branches**.

**Questions 1 to 4** relate to the situation at the Superclean company.

---

## Question 1

Assume that the Superclean company in **Groningen** shall have the use of the following table of premises:

| building no. | address          | m2   | customer no. | name            | address                        |
| ------------ | ---------------- | ---- | ------------ | --------------- | ------------------------------ |
| 1054         | Landleven 10     | 1000 | 1052         | Hanzehogeschool | Landleven 10 9747 AD Groningen |
| 2034         | Penningsdijk 6   | 2000 | 1052         | Hanzehogeschool | Landleven 10 9747 AD Groningen |
| 1236         | Hoendiepskade 23 | 1700 | 1052         | Hanzehogeschool | Landleven 10 9747 AD Groningen |

What **objections** are to be raised against this database design?

---

## Question 2

Assume that the **Groningen branch** of Superclean has in use the following table of customers:

|custno|name|address|zip|city|bno1|bno2|bno3|bno4|bno5|
|---|---|---|---|---|---|---|---|---|---|
|1052|Hanze|Penningsdijk|9747 AR|Groningen|105|2034|1236|||
|1123|OVVM|Xxxxxxxxx 5|97xx XX|Groningen|1234|2345|1001|1991|1543|
|1423|AZG|Yyyyyyyyy 1|97yy YY|Groningen|1253|1111|1212|1330|1777|

a. What **objections** can be raised against this database design? b. Devise an **awkward question** to be put to this table and show why this is awkward.

---

## Question 3

Assume that the **salaries administration** of the Groningen branch will have the following table of employees in use. In this there is the **basic salary** (the amount which everyone shall earn for 38 hours in service) and the **gross salary** (the amount that everyone earns on the basis of the number of hours that he or she is actually in service):

|employee_no|name|functioncode|description|basic salary|no of hours|gross salary|
|---|---|---|---|---|---|---|
|086|J. de Boer|031|cleaner|1482|10|390|
|087|T. Pieterse|035|overseer|1710|12|540|
|088|A. Arendse|031|cleaner|1482|12|468|
|089|T. Dolstra|100|inspector|3980|38|3980|
|090|V.V. de Smet|031|cleaner|1482|10|390|

a. What **objections** are to be raised against this database design? b. An **improved design** is:

```
employees(emp_no, name, functioncode, no_of_hours)
functions(functioncode, description, basic_salary)
```

c. Fill in this table with all the values which are to be seen above. Give an accurate description of the way the **gross salary** of employee 088 can be found.

---

## Question 4

In the following there is always talk of **two entities**. Characterize the **relationship** between these entities according to the rules of notation on the previous page. (N.B. The descriptions below do not have to be entirely in agreement with the description of the Superclean company given earlier.)

a. A **customer** of Superclean can have several **buildings**. One building belongs to only one customer. b. Each **cleaner** is part of only one **team**. One team consists of several cleaners. c. Each **team** has only one **overseer**. An overseer can oversee several teams.

---

## Question 5

A situation description can look complicated to such a degree that one cannot see the wood for the trees. A simplification of the situation can help to enhance insight in the problem at hand. In this task such an approach is dealt with.

A **dentist** wants to automate his administration. For each **patient** he wants to establish a quantity of **personal data**. Furthermore, he wants to keep track of on what **date** patients had received what **treatments**.

There are a **hundred treatments**. Each of these possible treatments has its own **tariff** (which is fixed uniformly nationally). Patients can undergo **one or more** of these treatments per visit, for example twice for a dihedral amalgam restoration. Then it must be recorded whether a patient is **insured with a health insurance scheme** or is a **private patient**. In the first case bills are sent to that **insurance scheme**, in the second case to the patient himself.

With this situation description one should be able to meet the following task:

> _Design the database tables for this situation. Use the following list of field names (arranged alphabetically): address (= the address of a particular patient) date (= the date of a particular treatment for a particular patient) description (= the description of a particular treatment) hifaddress (= the address of a particular health insurance fund) hifname (= the name of a particular health insurance fund). name (= the name of a particular patient) number (= the number of treatments of a particular kind for a particular patient on a certain date) tariff (= the tariff for a particular treatment)_

In this list not necessarily all the field names of **primary keys** are included. For the rest this list is complete.

In that which follows you may first try for yourself to work out the statement. Then the situation is first simplified considerably and is then worked up step by step in accordance with the original situation description.

a. Carry out the task reproduced above in _italics_. (Do not devote more than 20 minutes to this; if you come to a full stop that is not a problem!)

Now follows the simplified rendering.

A dentist maintains a **patient administration system**, in which for each patient the necessary data is established. If a patient is insured with a **health insurance fund**, then the bill for a treatment is sent to the relevant health insurance fund. If a patient is insured privately, then the bill is sent to the patient himself. The dentist himself designs the following database table:

```
patients(patno, name, address, hifcode, hifname, hifaddress)
```

In it there are:

- patno = patient's number (unique)
- hifcode = a code which indicates whether someone is insured privately (P) or with a health insurance fund (I)
- hifname = the name of the health insurance fund
- hifaddress = the address of the health insurance fund.

b. Fill in **five records** of this table with values. c. On the basis of this filling in give **three objections** to this design. d. Make it clear that such objections are not to be brought against the following design:

```
patients(patno, name, address, hifcode)
health_insurance_funds(hifcode, hifname, hifaddress)
```

Here the hifcode is a **unique number** for each health insurance fund. The number **000**, however, represents no existing health insurance fund, but is used in order to indicate that a patient is insured privately.

e. Take the values which you have used for part b (except P and I) and fill in with these values the requisite records of the tables from the **improved design**. f. Which **two technical terms** are used for the field hifcode? g. What sort of **relationship** is spoken of between these two entities? h. Explain how the associated **rule for database design** is applied here and explain that this is applied in the correct manner.

Naturally the dentist also puts **monetary amounts** on the bills which he sends. At the same time he mentions in them the **date** on which the patient was under treatment. These matters must also be incorporated in the database design. The dentist therefore expands his table of patients as follows:

```
patients(patno, name, address, hifcode, date1, amount1, date2, amount2, ..., date10, amount10)
```

i. Give **three objections** to this approach. j. Formulate an **awkward question** for this table. k. Explain that such objections are not to be brought against the following design:

```
patients(patno, name, address, hifcode)
treatments_per_patient(patno, date, amount)
```

l. For illustration fill in the table **treatments_per_patient** with **four records**, of which **two relate to one and the same patient**. m. Using this filling in explain why in the table treatments_per_patient it cannot be sufficient with **patno as the sole key field**. n. Explain why it can indeed be sufficient with the **combination of patno and date**.

Patients and health insurance funds will also be keen to have a **description of the treatment** on the bill. Assume for convenience that there are **not more than 100 different treatments**, each of which has its own **tariff** (nationally uniform). For simplification in this stage, it may be assumed that a patient undergoes **only one** of the treatments per visit.

o. Give an **objection** against a table such as:

```
treatments_per_patient(patno, date, description, tariff)
```

The complete design for the dentist after these considerations gets the following appearance:

```
patients(patno, name, address, hifcode)
health_insurance_funds(hifcode, hifname, hifaddress)
treatments(upt_code, description, tariff)
treatments_per_patient(.....)
```

The table treatments_per_patient must now be filled in. The table treatments_per_patient is the right table for this. Someone proposes the following, but forgets to indicate the primary key:

```
treatments_per_patient(patno, date, upt_code, number)
```

q. Which fields must form the **primary key**?

The design is now complete and appears as follows:

```
patients(patno, name, address, hifcode)
health_insurance_funds(hifcode, hifname, hifaddress)
treatments(upt_code, description, tariff)
treatments_per_patient(patno, date, upt_code, number)
```

r. Now you know the answer, try to do the **complete design** again such as was asked in question 5a. s. In practice the dentist will certainly have printed on his bill **two other items**. Try to think what items these are and why these should be mentioned on the bill.

---


## Question 7

At the **SCG sports club** one can pursue various **sports**. Members must state which sports they wish to participate in. For each **member**, apart from a **membership number** and **personal data**, details of the **branches of sport** pursued are recorded. For each sport a certain **contribution** is laid down. It is also recorded whether members have **paid their contributions**. Possibly they have done this for one branch of sport and maybe not for another branch of sport.

a. Design the **tables** for the database of SCG. In doing so make use of the following list of field names. In this list not necessarily all field names of all **primary keys** appear. For the rest this list is complete.

```
sport_no, type of sport, contribution (=branch of sport)
date_of_birth (= the date of birth of a particular member)
memberno (= a unique membership number)
nat (= name, address and town of residence of a particular member)
paid (indicates whether a certain member has paid for a particular sport_amount (= the amount of the contribution for a particular branch of sport).
```

b. In your design indicate all **referencing keys**. c. Give the **pseudo commands** with which one can ascertain:

- which **sports** someone pursues
- and whether or not he has **paid** for them.

Once a year a **tournament** is organised, in which one can participate in various sports. Not every member needs to take part in the tournament. A member who participates does not need to participate in every branch of sport that he normally pursues. The data from the tournament are preserved. That means that a record is kept of who took part in what branches of sport in which **year**, and what his **placing** was for each branch of sport in which he participated.

d. Enlarge the **SCG database** so that these matters are also recorded in it. Extra fields which you can use are **yearnumber** and **placing**.

---

## Question 8

An **engineering office** carries out **projects** for clients. Such projects never last for longer than a **week**. For each project it is laid down for which **client** (unique client number, nat) it is carried out and which **basic price** is quoted to the client. In addition, it is recorded which **employees** (unique employee number, nat) take part in a project. An employee can participate in **various projects** at the same time. For the employees the **function** and the **number of hours** that he works per week on the various projects must be known. The **amount** that the client must pay is based on the number of hours that the various employees have put into the project. The **hourly rate** for each employee depends upon his function and on the **number of years’ experience** which he has. A database must be capable of, amongst other things, producing summaries of:

- all **employees** including their name, function, years of experience and hourly rate
- the names of all employees who have worked on a particular project, including for all employees the number of hours worked
- the numbers of projects which have been carried out, for which client, for which basic price as well as the total amount which is considered.

a. Design for this office the **required database tables**. Use the following field names:

```
basic_price
client_name
client_no
employee_name
employee_no
function
hourly_rate
no_of_hours (= number of hours worked by a particular employee on a particular project)
no_of_years (= number of years of experience for a particular employee)
projectcode
```

b. Give an accurate description of the manner in which a **summary** can be produced of the names of all the employees who have worked together on **project 3404**, including the **numbers of hours** worked by each of them.

---

## Question 9

In this question one is asked to design a database for the **Superclean company**. As is apparent from question 4, the original description still exhibits a lot of obscurities. For that there are the following additions to this description.

- A **customer** of Superclean can have several **buildings**. A building belongs to only one customer.
- A **building** is cleaned by only one **team**. Each team cleans only one building.
- An **employee** can form part of several different **teams**. A team consists of several employees.
- Each **team** has only one **overseer**. Someone who is allocated to several teams may be the overseer in one team but does not have to be that in another team.
- Each **customer** belongs to only one **district** and falls under the responsibility of the **inspector** for that district. In a district there are several customers.

Design the **database tables** for Superclean. Use the following list of field names. This list is complete:

```
building_address
building_hours (indicates when the building can be cleaned)
building_no
building_size
customer_name
customer_no
district_description
district_no
employee_name
employee_no
inspector_employee_no
overseer_employee_no
team_no
```

---

## Summary

> ✅ This chapter provides **practice questions** on database design principles, focusing on:
> 
> - Identifying **bad designs** and their problems
> - Improving schemas with **normalization**
> - Defining **relationships** (1:1, 1:n, n:n)
> - Building complete databases from **requirements**

> **Rule of Thumb:** _Start with **entities**, add **attributes**, resolve **relationships** with keys — and always check for **redundancy** and **consistency**._