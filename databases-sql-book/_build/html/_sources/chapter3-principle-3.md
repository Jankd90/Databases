# Chapter 3: Principle 3 ½

The normal course of affairs is that first the information requirements are determined and on the basis
of that a list of characteristics is produced. Using this list entities can be determined and the database
tables can be designed.
Assume that in the departments -employees database it is given that employees can work in more than
one department, but have a voting right in only one department. Op the basis of the information
requirements the following list of characteristics then can b e created:
dep_name
dep_no
budget
function
salary
emp_name
emp_no
voting_right

The database design according to the principles 1 - 3 results in the following tables:
departments (dep_no , dep_name, budget, ...)
employees( emp_no , emp_name, function, salary, ...)

The principles 4 and 5 govern how the relationship between these entities must be processed in the
design. However, one can also first examine which characteristics not yet have been included in any
of the present tables. In this example it is the characte ristic voting_right , which says something about
a particular employee in a particular department .
This formulation makes it clear that this characteristic can neither be taken up in departm ents nor in
employees. The consequence is that a separate table must be designed for it. The italics make it
immediately clear which key this new table must have, n amely the combina tion of emp_no and
dep_no :
voting_rightstable (emp_no , dep_no , voting_right)

The side effect of this treatment is that at the same time one can have processed the many -to-many
relationship which exists between employees and departments into the design. In this example the
application of the principles 4 and 5 is no longer necessary. This newly applied principle is not to be
found in the book of Date cited earlier and will in this text therefore be indicated as `principle 3½':

:::{important}
Principle 3½
:::

For every characteristic not yet included in a table determine the entities this charasteristic some thing
says about. Then create for this characteristic a new table in which the combina tion of primary keys
of the named entities appears as the primary key.

With rule 3½ one thus finds the many -to-many relationships that also have one or more characteristics
of their own. Principle 3½ does not render the principles 4 and 5 useless. Many -to-many relationships
which do not have any characteristic of thier own ar e naturally not found with rule 3½. In the case of
one-to-many relationships (principle 4) a characteristic already in use, namely as primary key in the
one-table, is once more included in another table. In the case of rule 3½ on the other hand, it concern s
characteristics which are not yet in use.

A TABLE IN A TABLE

The bad designs could also have been characterised by the remark `there is a complete table within
another table'.
In the case of the poor designs this is so striking that anyone will recognise this immediately. However
sometimes it is a good deal more subtle.
Assume that in the description of the departments -employees database the following sentence is
added:
`The salary of an employee depends on his years of service.'
The consequences of this sentence become clear using a suitable example table:

emp_no emp_name function years_of_service salary
-------------------------------------------------------------------------------------------
001 j. de boer porter 6 1800
002 j. de vries adm. emp 10 2000
003 j. deelder adm. emp 6 1800
004 j. den dolder overseer 6 1800

In this table redundancy can be recognised: the fact that 6 years of service corresponds to a salary of
1800 is stored several times. The solution is an extra table:
employees (emp_no , emp_name, function, years_of_service)
salaries (years_of_service , salary)

This correct solution makes it clear that in the example table there is also a table within a table.
The salary is a characteristic of the number of years of service and the years of service in its turn is a
characteristic of an employee. One might state that the salary is a derived or indirect character istic of
the employee entity. Principle 3 for the design should therefore be interpreted in such a way that in a
table for a particular object only direct characteristics may be included and no indirect or derived
charateristics.

NOTATION OF RELATIONS
Relations can be notated in the following manner:

┌───────┐ ┌───────┐ ┌───────┐
└───┬───┘ └───┬───┘ └───┬───┘
 │ 1 │ 1 │ n
 │ one │ one │ many
 │ to │ to │ to
 │ one │ many │ many
 │ 1 │ n │ n
┌───┴───┐ ┌───┴───┐ ┌───┴───┐
└───────┘ └───────┘ └───────┘
