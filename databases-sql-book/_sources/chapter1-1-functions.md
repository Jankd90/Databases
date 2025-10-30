# Chapter 1: 1 Functions

Aggregate functions

SQL provides with some so -called aggregate functions. Aggregation means to summarize values into one.
The functions are:
count( )
sum( )
avg( )
min( )
max( )

The use of these aggregate functions is similar, and depends on whether they are used alone, or in
conjunction with a field.
In between the parentheses, the name of the field is specified. The function count() returns the number of
entries that were selected; the other functions compute and print the sum, average, lowest or highest value
of the selected entries with respect to the specified field.

Aggregate function on its own
In this case, the function just follows the ' select' -clause and returns the computed value of the function will
be computed.

Examples:

```
sql
select min(week)
from charts
where record_no=50;
```

The computer will select all weeks from the CHARTS file of record number 50 but will print only the lowest
value of them.
In fact, the value that is returned is the so -called debut week of this record: the week in which it entered the
Top 10.

```
sql
select count(record_no)
from records
where artist_no=15;
```

Returns the number of entries in the table RECORDS that satisfy the condition. (Artist number 15 are The
Beatles). The value is interpreted as the number of records the Beatles had in the charts.

Aggregate functions in conjunction with a field
Usually, the outcome of an aggregate function says something about a field, and you want this field to be
printed as well.

Example
Suppose you want a list of all different countries, together with the number of artists from that country.

For one country at a time, it would look like this:

```
sql
select count(artist_no)
from artists
where country='usa';
```

or
```
sql
select count(artist_no)
from artists
where country='uk';
```

or

```
sql
select count(artist_no)
from artists
where country='f';
```

and so on.

In fact, you would first have to know all the possible country -values.
What we would like, is a list of all countries, followed by a number, indicating the number of artists.

This is the command:
```
sql
select country, count(artist_no)
from artists
group by country;
```

The official SQL rule is:
The GROUP BY clause combines rows from a SELECT statement into groups in which the specified
column has the same value.
Each group is reduced to a single row (which includes this value). After the word SELECT only the
field that specifies the group may be named, together with aggregate functions (sum, min, max, avg,
count) only.

In our case, for each different value of country (because group by is followed by this field) one line is printed,
which may contain the value of an aggregate function as well.

Another example
The number of artists per record company.
For one record company it would be like this:

```
sql
select count(record_no)
from records
where rec_co=19; (record company 19 is Capitol)
```

To have list that includes all record companies with the value of the aggregate functions we need group by :

```
sql
select rec_co, count(record_no)
from records
group by rec_co;
```

Sorting

The clause order by results in the final list to appear in sorted order, by default in ascending order. Order
by appears at the very end of a select statement, and you have to specify the field that defines the sorting.
After this fieldname, you could specify desc to obtain descending order.

:::{note}
**Example:** 
:::

```
sql
select week, position
from charts
where record_no = 50
order by position;
```

will return a list of chart positions of this record ('A World Without Love') is chronological order.
Please note, that a table in a relational database need not be sorted!
Remark: week doesn't necessarily have to be part of the select clause, although it defines the sorting order.

Linking files

In our database, the entities, and thus the files, are related. SQL should be told about these relationship.
Then SQL is able to connect values from one table to another.
Linking two files is done by specifying the fields that should match in the where -claus.

:::{note}
**Example:** 
The artist_no in RECORDS relates to the artist_no in ARTISTS. In fact, they are the same.
Suppose we want all record titles of songs released by Capitol Records (rec_co=19).
First try:
```
sql
select title
from records
where rec_co=19;
```
:::

If we want to include artist names as well, we have to get these names from the ARTISTS table. The files
are linked by the relationship

 records.artist_no = artists.artist_no
Please note, that the fields are prefixed by the filename that they belong to.

The command is:

```
sql
select title, name
from records, artists
where records.artist_no=artists.artist_no
```
and rec_co=19;

Remarks:
- After from, all files must be named that are involved in the selection.
- When fieldnames are ambiguous, filenames have to be stated in front of the fieldnames, in order to
enable SQL to identify exactly which fields are meant.
- Leaving out the link would result in a disaster: in that case all artist names would be printed in
conjunction with each record title (satisfying the condition): an enormous list, all garbage!

In our running example only three links can be made (see box).

Of course you can imagine real -life databases to have hundreds of links. Handling that need not be more
difficult than handling three: it's just more of the same.

Questions 2

a. Create a list of record numbers of records that were in the charts in week 20.
b. Include positions in this list.
c. Order the list by position.
 What you have now, is the basis of the week 20 hitparade. Of course, a real hitparade includes
 titles.
d. Make a link with one of the other files, to include these record titles in this list.
e. Make another link, to include artist names as well.
 What you should have by now, is a list that very much resembles a true hitparade. You might
 want to include the names of record companies as well.
f. Make a list of record numbers, together with their first week in the charts (the so -called debut week ).
Use of course one of the aggregate functions.
g. List the no.1 hits of the Beatles (artist_no=15).
Hint: first produce a list of all their hits, then select only those that reached the no.1 position.
h. Make a list of record companies, that released records from the Beatles.
i. Include the songtitles in this list.

LINKS IN THE DATABASE TOP10USA

artists.artist_no=records.artist_no

records.rec_co=rec_comp.rec_co

charts.record_no=records.record_no

Chapte r 11 Files

Creating 'files'

When you end a query with save as… command then a file will be created with the name that you specified
and fieldnames you specified: just as many fieldnames as you specified in the select -clause.

Eg.
```
sql
select artists.name, records.title
from artists, records
where artists.artist_no=records.artist_no
```

File|Save as… 'songs' {overwrite the previous name}

The table SONGS can now be treated as an ordinary table.

Remarks:
- Before you actually create the file, first check the output on the screen. When everything is found to
be O kay, select the SQL -button and then goto File| save as… .
- The use of files is extremely important when you use aggregate functions. When you use aggregate
functions, group by must be specified. When you save the results to a file, you don't have to specify
```
sql
group by again, and consequently you are no longer restricted to the rules of group by .
```

Using files can make your SQL life a lot easier. It can be used to break down a complicated question into
smaller ones, and consequently breaks up a complicated SQL query (with possibly disastrous
consequences when containing an error) into a few less complicated ones.

Example
You may want to be interested in which record company has released most records. That might be an
interesting indication for the market position of record companies.
The problem is to come up with the name of that record company.
Think of the following: how would you solve this problem without SQL, from paper? Probably, you would
first want to count the number of records per record company (and put these numbers on a piece of paper),
and then have a look at that list and select the highest value.
Files play the role of the piece of paper. Make a list of two columns, one for the record companies, and the
second column containing the number of records released by that company.

First try:

```
sql
select rec_co, count(record_no)
from records
group by rec_co;
```

This will produce a list as follows:

1 7
2 1
3 7
4 1
5 1
... ...

in which the first column is the record company number, and the second one the amount of records released
by that company.
This list should be on the piece of paper , and then the highest value should be selected.
In SQL, the piece of paper is replaced by the notion of file:

Second try:

```
sql
select rec_co, count(record_no) AS amount
from records
group by rec_co
```

save as... 'mosthits'

The extra statements 'AS amount' is added to (re)name fieldname count(reocrd_no). The fieldname is now
'amount' instate of 'exp1001'. In general with the 'AS' statement you can rename every fieldname.

Now the file MOSTHITS has been created, with two fields rec_co and amount , of course indicating the
record company code and their respective amount of hits.

Would you type

```
sql
select *
from mosthits;
```

the complete list would be printed on the screen.
Now it is not too difficult to find the record company/ies with the highest number of hits:

```
sql
select rec_co, amount
from mosthits
where amount = (select max(amount)
from mosthits) ;
```

Note that more than one record company code could be listed.

1. Example
a. Try the example from the text above.

b. If you did a good job, you should be able to include the name(s) of the record company/ies in the
final SQL clause. The output should include not only rec_co but name (of the record company) as
well.

Questions 3

Most Successful Artists

If you fully understand the previous example, you should be able to follow the same pattern to answer the
question:
which artist(s) released most records

(Hint: how would you proceed without SQL, so with pen and paper only?)

The Highest Debut Position
In the world of hit parades , many records can be set longest on the charts, most weeks on no.1 position,
and so on. The record that we now will look at, is the highest debut position . Some records enter the
charts at position 10, some at 9, et cetera. When a record enters the charts at a high position (4, or 3,
maybe even higher) it is considered a sensational hit. In the next questions, we will find out which record
was the biggest sensation (as to its debut position) in 1964.

a. Produce a list of record numbers with their debut week numbers.

b. Exclude from this list the records from week 1: they shouldn't count, as they are all new entries. (Just
add one extra line in the where part)

c. Save this list to file; call this file DEBWEEK , with fields recond_no and debwk_no , (use here the 'AS'
statement two times).

d. Have a look at this file, by issueing the command
```
sql
select *
from debweek;
```
Do you exactly understand what the two columns stand for? (Be honest if you don't!)

e. Use this just created file DEBWEEK, to make a list including record numbers and the chart position
of each record in their debut week.
This list will then contain record numbers and debut positions.
In other words, your output should look as follows:

... ...
32 7
33 4
34 9
... ...

in which the first column is the record number, and the second one is the position in the debut week.

(Hint: positions can of course be found in the CHARTS table. One record occupies several positions
in different weeks; you are only interested in one particular week: the debut week. In other words:
week from the CHARTS table should be equal to debwk_no in the DEBWEEK table. You will of
course have to link these files. Through which fields?)

f. Save as… debposition with fieldnames rec_no, debpos. Then, after issueing the command, another
file will have been created: DEBPOSITION.
Have a look at this file, by typing
```
sql
select *
from debposition;
```
Again, be honest if don't fully understand the meaning of the columns.

g. Use this file DEBPOSITION to find the record(s) with the highest debut position.

h. Check the appropriate table to find the song title(s)

Questions 4

Song of the Year 1964
Produce a hitparade of the 'Song of the Year 1964'.
(Including record title, artist name and total number of points).
A record that was at position 10 in a certain week will get 1 point, at position 9 will get 2 points, and so on,
and a song at the top position gets 10 points.
The song that has most points in total will end up as the no.1 song of the year 1964, so at the first position
of the list that you are asked to produce. Second most points will be the runner up, and so on.

Hints:
Use files, for the following purposes:
First make a file, with the points for each record in a certain week.
The number of points is computed by 11-position . (Here the rule is used that a computation may follow
```
sql
select).
```
Your first command will be:

```
sql
select record_no, 11 -position AS points
from ...
```

Then sum all these points per record (use SUM and GROUP BY ) and save this to another file.
This file contains record numbers, together with the points total of that record.
Then sort, and so on.

Chapter12 Files in the database
top10usa

 ARTISTS

ARTIST_NO NAME COUNTRY

 .. .... ..
 31 the dave clark five uk
 32 betty everett usa
 33 the serendipity singers usa
 34 mary wells uk
 35 the 4 seasons usa
 36 danny williams usa
 37 roy orbison usa
 38 the dixie cups usa
 39 the ray charles singers usa
 40 the reflections usa
 41 peter & gordon uk
 42 billy j. kramer uk
 43 barbra streisand usa
 44 millie small usa
 45 gerry & the pacemakers uk
 46 the bachelors usa
 47 johnny rivers usa
 48 stan getz/astrud gilberto usa
 49 chuck berry usa
 50 roger miller usa
 51 the impressions usa
 52 dusty springfield uk
 53 dean martin usa
 54 the supremes usa
 .. .... ...

In total there are 77 entries in this table.

RECORDS

RECORD_NO TITLE ARTIST_NO REC_CO

 .. .... .. ..
 39 do you want to know a secret 15 24
 40 dead man's curve 14 14
 41 bits and pieces 31 1
 42 my guy 34 31
 43 ronnie 35 3
 44 white on white 36 28
 45 love me do 15 26
 46 it's over 37 32
 47 chapel of love 38 33
 48 love me with all your heart 39 34
 49 (just like) romeo & juliet 40 35
 50 a world without love 41 19
 51 little children 42 36
 52 walk on by 18 17
 53 p.s. i love you 15 26
 54 people 43 12
 55 I get around 26 19
 56 my boy lollipop 44 37
 57 don't let the sun catch you 45 38
 crying
 58 diane 46 39
 .. ... .. ..

In total there are 111 entries in this file.

REC_COMP

REC_CO NAME

 .. ...
 15 okeh
 16 mercury
 17 scepter
 18 decca
 19 capitol
 20 swan
 21 rca
 22 abc
 23 20th century
 24 vee-jay
 25 montel
 26 tollie
 27 riviera
 28 united artists
 .. ...

In total there are 55 entries in this file.

CHARTS

WEEK RECORD_NO POSITION

 .. .. ..
 13 26 4
 14 26 5
 15 26 9
 9 27 9
 10 27 8
 11 30 10
 12 30 9
 12 31 7
 13 31 3
 .. .. ..

In total there are 520 entries in this file.
