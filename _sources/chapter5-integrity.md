# Chapter 5: Integrity

INTRODUCTION
- Security involves ensuring that users are allowed to do the things they are trying to do
- Integrity involves ensuring that the things they are trying to do are correct

Or to put it otherwise: security means protecting the database against unau thorized users, integrity
means protecting it against authorized users.

SOME ASPECTS OF INTEGRITY
Every table should have a primary key : uniquely identifying each record. The DBMS should therefore
guarantee that no two records have the same primary key.
Some tables will include foreign keys . A foreign key must match some primary key. The DBMS should
check this. If for instance the matching record is deleted, the foreign key, first relating to that record,
now relates to a non -existing record. The DBMS should prevent this. A similar problem o ccurs when
for some reason the primary keys of a table are changed: foreign keys relating to it must be adapted
as well!
Using format constraints is a way to prevent (only) big mistakes. For instance, the values of some field
can be restricted to numbers only, or capitals only, or first four numbers and then two letters (like the
Dutch postcode ), et cetera. In Paradox for Windows, when defining a datatable structure, you have to
specify a field type : this is a format constraint as well. A field of type Date will accept strings that
represent a valid date only. In this way, blunt mistakes are prevented. Nonetheless, it remains very
well possible to make mistakes. It seems that no computer facility can ensure complete integrity.
