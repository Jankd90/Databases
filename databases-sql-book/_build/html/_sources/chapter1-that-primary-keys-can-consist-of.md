# Chapter 1: that primary keys can consist of

combinations of fields as well as of single fields. )

SUPPLIER
suppn
o sname status city
primary key

SHIPMENT
 foreign key
suppn
o partno quantity
foreign key

PART
partno pname color weight city
primary key

stated that: supplier.suppno = shipment.suppno
and shipment.partno = part.partno

Abstracting the foregoing discussion, we are led to the following:

 Principle 5

Represent each many -to-many relationship between entity types as a separate table. Use foreign keys
within that table to identify the entity types involved in the relationship. Use the combina tion of those
foreign keys as the primary key for the table. Represent properties of the relations hip by fields in the
relationship table.

FURTHER REMARKS

 The suppliers -and-parts example gives rise to a number of further observati ons.

 It is common to talk of many -to-many relationships as if they were the most complicated kind of
relationship to arise in practice. But many -to-many-to-many (etc.) relationships are by no means
unknown. By way of illustrati on, we might extend the supplie rs-and-parts example to involve projects
also: Each shipment is a shipment of a certain part by a certain supplier to a certain project. A suitable
design for this case would be as shown in Fig. 2.5. The SHIPMENT table now represents a
many -to-many -to-many rela tionship and involves three foreign keys and a primary key with three
components. Thus the technique for dealing with many -tomany -to-many (etc.) relationships is no
more than a generalization of that for dealing with many -to-many relationships (Pr inciple 5), and does
not really require any special considerati on.

:::{admonition} Exercise
:::

 supplier
Suppno sname etc.

 part
partno pname etc.

 project
projno etc.

 shipment
suppno partno Projno quantity

stated that:
supplier.suppno = shipment.suppno
and part.partno = shipment.partno
and project.projno = shipment.projno
 Returning now to the simple suppliers -and-parts example (i.e., forgetting projects): Note that the
relationship of suppliers to ship ments is one -to-many, and the relationship of parts to shipments is
also one -to-many. Principle 4 (for dealing with one -to-many rela tionships) should therefore apply; and
so indeed it does, if we look at suppliers -to-shipments and parts -to-shipments separately. The fact is,
a many -to-many relationship can always be regarded as a combina tion of two one -to-many
relationship s. (Similarly, a many -to-many -to-many relationship can always be regarded as a
combination of three one -to-many relationships, etc.)

 We said earlier that foreign -key-primary -key matches are the glue that holds the database (better
yet: the tables) together. Broadly speaking, this state ment is true. However, there may be other
intertable relationships that are not represented by keys at all. An example is provided in the
suppliers -and-parts database by the fields SUPPLIER.CITY and PART.CITY. Suppli ers located in
London, for example, do have some kInd of relationship with parts that are stored in London, namely,
"colocation"; but that re lationship is represented by matching values in two fields that are not primary
or foreign keys. (Those fields could become foreign keys if a "city" table were to be added to the
database later on.)

SUMMARY

We have now come to the end of our discussion of database design. As indicated in the introduction
to the previous chapter, it is possi ble to go very much further with this topic than we have done in
these two chapters. However, we have covered enough to enable you to approach database design
problems with some confidence, particularly in a small or single -user environ ment. By way of con -
clusion, we repeat the definitions of primary and foreign key (since those concepts are so crucial to
the design pro cess), and we then repeat the five design principles identified in this chapter and its
predecessor.

 Definition: The primary key of a table is a field of that table, or perhaps a combination of several
fields of that table, that can be used as a unique identifier for the records in that table.

 Definition: A foreign key is a field or field combination in one table whose values are required to
match those of the primary key in some other table.

 Design principle 1: Represent each entity type as a separate table.

 Design principle 2: Decide the primary key for each table.

 Design principle 3: Assign each property of an entity type to a field within the table representing that
entity type.

 Design principle 4: Represent each one -to-many relationship between entity types by a foreign key
in the "many" table that matches the primary key of the "one" table.

 Design principle 5: Represent each many -to-many relationship between entity types as a separate
table. Use foreign keys within that table to identify the entity types involved in the re lationship. Use
the combination of those foreign keys as the primary key for the table. Represent properties of the
relation ship by fields in the relationship table.
