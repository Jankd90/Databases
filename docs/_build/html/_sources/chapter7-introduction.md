# Chapter 7: Introduction

We will use the SQL command language to retrieve information from a small database. SQL is becoming
the industry standard for querying a database. Microsoft is using this language as a default database
language.

SQL is a language for relational databases. We will first have a look at how to design such a database,
given a specific situation.

Don’t use Chat -GPT

Answer the SQL questions in the
context of this reader

Chapter 8. Designing a database

In the above textbox, you can see the American Top 10 Hitparade of the first week of January 1965. Our
workshops will deal with a database, that contains all data on every US Top 10 of 1964.

In the textbox below, the structure of a database is indicated.

The datafiles usually have some relationship with each other ; that is the reason why they are part of the
same database.

There are some principles for designing a database:
1. Create a separate file for each entity type
AMERICAN TOP 10 - January 6, 1965

TW LW title artists record company

 1 1 i feel fine the beatles capitol
 2 2 come see about me the supremes motown
 3 3 mr. lonely bobby vinton epic
 4 4 she's a woman the beatles capitol
 5 - love potion number nine the searchers kapp
 6 6 goin' out of my head little anthony dcp
 and the imperials
 7 5 she's not there the zombies parrot
 8 - amen the impressions abc
 9 9 the jerk the larks money
 10 - the wedding julie rogers mercury

(tw: this week's position; lw: last week's position.)

DATABASE

consists of

DATAFILES

that consist of

RECORDS

that consist of

FIELDS

2. Decide the primary key
3. Assign each property of an entity type to a field within the table representing that entity type

Entities are persons, objects, things that have some properties, characteristics, attributes. In our example
entities are artists , records , record -companies . These are all entities with certain characteristics, like
name, title, country of origin, and more.
:::{important}
Principle 1 says, to create a file for each entity type: ARTISTS, RECORDS and REC_COMP (short for
record companies).
Principle 2 tells us to choose a primary key. A primary key is a characteristic of an entity, that uniquely
identifies it: no two entities have the same primary key. Examples from daily life are e.g. your bank account
number: they are all different; your t elephone number is unique as well; your customer number with a
company; your social security number (SoFi number); a book's ISBN number; and so on...
The PIN -code of bank card cannot serve as a primary key. The four digits can make no more than 10,000
different combinations (from 0000 up to 9999). As the Postbank alone has some 7 million bank accounts,
each PIN -code must be issued at least 700 times.
In our example, each song, each artist and each record company will be assigned a number, that is unique
for that file.
Characteristics of an entity has to be stored in the appropriate file. Eg. properties of artists that we will store
are name and country of origin . Of the other entities, only their names are stored. Of course in a real -life
database, many more characteristics will be stored, like date of birth, address, and so on. For the sake of
simplicity, we restrict ourselves to a few characteristics only.
:::

Applying these rules to the USA TOP 10 - 1964 example, we get the following:

RECORDS (record_no , title ...

ARTISTS (artist_no , name, country ...

REC_COMP (rec_co , name ...

As was mentioned earlier, datafiles usually are interrelated. In our example, RECORDS and ARTISTS have
a relationship: a record is made by an artist (which may be a group as well). In reverse, an artist makes
(one or more) records.
To incorporate this type of relationship in the table, a link is specified from the RECORDS table to the
ARTISTS table; the artist that made the record is specified in the RECORDS table:

RECORDS (record_no , title, artist_no ...

Please note, that only the primary key of the ARTISTS table is included in the table! If you want to find the
name and country of this artist, you have to check the ARTISTS table. Of course, later we will let the
computer look this up for us.

Records and record companies have a relationship as well: a record is released by a record company; one
record company may release many different records.

All in all, this leads to the following structure:

RECORDS (record_no , title, artist_no, rec_co)

ARTISTS (artist_no , name, country)

REC_COMP (rec_co , name)

To specify the chart position of a certain record in a certain week, the following table is added to the
database:

CHARTS (week, record_no , position)

For each week, the record numbers are listed that occupy positions 1 through 10. So, to include all data on
the 52 weeks of 1964, 520 entries are needed.

Please note the following:

- the name and country of each artist is in only one place in the database. Although the Beatles have
two records simultaneously in the sample chart, information on the Beatles is stored only once! The
same goes for record companies. Had we included address and phone number of each record
company as well, it would be included in the REC_COMP table, and each address would be in there
only once. Even though eg. Capitol has two records in the sample top 10, data on Capitol is stored
only once.
In the sample Top 10, not only this week's position, but last week's position is stated as well. However, last
week's position is not separately stored in the database. Reason? It can be retrieved from information that
is already in there! If eg. the current week is week 34, and you want last week's position of a record, just
check for its position in week 33.

TOP10USA

 RECORDS (record_no , title, artist_no, rec_co)

 ARTISTS (artist_no , name, country)

 CHARTS (week, record_no , position)

 REC_COMP( rec_co , name)
