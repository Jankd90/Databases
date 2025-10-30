# Chapter 9: SQL

Preparation

In order to benefit as much as possible from the limited time, be sure that you are well prepared. It can be
believed that proper preparation and attendance . The impact of a minor mistake may be disastrous. We
think that a lot of practice will help you preventing mistakes.

Introduction to SQL

SQL was developed to have a computer language for data retrieval from large databases much like plain
English. The commands that make up the language are some sort of structured English. However, do not
underestimate the impact of the commands. They are ve ry powerful, and mistakes may lead to a wrong
use of this power, resulting in minor or major disasters. These disasters however do not harm the computer
but will annoy you as they are time -consuming.

SQL can be used to create databases and fill them with values. We won't do this. Our focus will be on
retrieving information . The key command to do this is select .

The basic structure of the command is:

```
sql
select <fields/expression>
```

```
sql
from <table(s)>
```

```
sql
where <condition(s)> ;
```

After select , a list of fieldnames follow (or just one fieldname). In our example, fieldnames are viz. title,
record_no or country .
After from , specify the tablenames (=filenames) of the tables (=files) that are involved. Our database
consists of four tables. Some select -commands may involve all four of them, usually one or two tables are
involved.
After where , one (or more) conditions may follow. If no condition is specified, you need not specify where ;
in that case, all entries from the database will be selected and printed. However, usually you do want to
```
sql
select . Please understand, that a real -life datafile may contain thousands of records. Only those entries
```
that satisfy the condition(s) will be selected and printed.
You could say, that select makes a column selection, and where selects rows.
Please note, that all SQL commands end with a semicolon ;.

Examples

We will now have a look at some sample SQL commands.
The first one has a very elementary structure:

```
sql
select name
from artists
where artist_no= 41;
```

In the above textbox, you can see part of the ARTISTS table. To execute the command, the computer
will look in this table, because it is specified after from , and will select only those records that satisfy
the condition that the value of their field artist_no equals 41. Of course, this is only one record. From
this record, the value of the field name is printed. On the screen you will read the result:

NAME
peter & Gordon

To print all of the fields, specify * after select:

```
sql
select *
from artists
where artist_no=41 ;
```

Result:
ARTIST_NO NAME COUNTRY
41 peter & gordon uk

ARTISTS

ARTIST_NO NAME COUNTRY

 1 bobby vinton usa
 2 the kingsmen usa
 .. ............. ...
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
 .. ............. ...

A select command may of course yield more than one matching record.

```
sql
select name
from artists
where country='uk';
```

This will give a list of all artist names of artists from the UK. Please note, that the value of an alphanumerical
field is enclosed in single quotes.

Remember, you don't always need the where clause:

```
sql
select country
from artists;
```

will give a complete list of all countries the artists come from. When you try this command in the seminar,
please try the following as well, and 'spot the difference...' :

```
sql
select distinct country
from artists;
```

Perhaps you are interested in the hit(s) of Peter & Gordon in 1964. The title(s) are in the table RECORDS.
Part of this file is listed in the textbox below.

```
sql
From one of the previous commands, we know that Peter & Gordon have artist_no 41. Now, check for this
```
column, and select all records in which artist_no=41 . Printing the title will give you the desired information.
```
sql
From the part of the RECORDS table that is listed in the textbox, you can find only one entry: 'A World
```
Without Love'.
RECORDS

RECORD_NO TITLE ARTIST_NO REC_CO
 .. ......... .. ..
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
 .. ........ .. ..

But maybe there are more: let the computer find them.

```
sql
select title
from records
where artist_no=41;
```

Had we been looking for the songs from a different artist or group, we hadn't known their artist_no. So, our
complete sequence of commands should have been:

```
sql
select artist_no
from artists
where name='peter & gordon';
```

```
sql
select title
from records
where artist_no=41;
```

Nested commands
SQL allows us, to construct one command from the above two. In fact, the result from the first command is
used in the second one: we read the result 41 from the screen and use this in the second command. You
could say, that

```
sql
select artist_no
from artists
where name='peter & gordon';
```

is a different way of writing

41.

So, replace 41 in

```
sql
Select title
from records
where artist_no=41;
```

to get one nested command:

```
sql
select title
from records
where artist_no= (select artist_no
from artists
where name='peter & gordon');
```

Remark:
Sometimes one isn't quite sure about the spelling of a name. In that case, you may prefer the option like.
```
sql
select artist_no
```

```
sql
from artists
where name like '*gordon*';
```

will select all records from the file that include the string gordon in the name -field.

Warning:
Note, that there may be several entries that satisfy this condition! So, the result could be several artist
numbers.
Consequently, the = -sign in

```
sql
select title
from records
where artist_no= (select artist_no
from artists
where name like '*gordon*');
```

doesn't make sense anymore. In that case, use in. Because the answer is a set of answers.

```
sql
select title
from records
where artist_no in (select artist_no
from artists
where name like '*gordon*');
```

In will work as well, when only one value is selected. So, in any case of doubt, use the in-construction.

The
CHARTS table

The fields in the CHARTS table are week , record_no , and position .
In the textbox a small part of the file is listed. Because information of 52 top 10s is listed, the table has 520
records in total.
```
sql
From the part of the table that is shown in the box, one can draw the conclusion, that record number 27
```
occupied position 9 in week 9; in week 10 it occupied position 8. Of course, in the RECORDS table, one
can find the title of this song.
Remember that we decided not to include last week's position as a separate field in the table when we
designed the database; from this example it should be clear why. In week 10, last week's position of record
number 27 is position 9 which is its position in week 9.

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
 .. .. ..
