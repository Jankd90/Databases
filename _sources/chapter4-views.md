# Chapter 4: Views

INTRODUCTION
As indexes are tables that are transparant, which means that they do exist but the user cannot see
their presence, views are visible to the user, but actually they do not exist; they are virtual tables.

EXAMPLES OF VIEWS
Views are very common with using a database. In fact, a view consists of a selection of records or
fields (or both) of one or more data tables.

In the above picture you can see a view that consists of a selection of records from a single data table.
The view ensures that the user is only dealing with records that are needed for some specific operation.
For example, these may be the records of weekly magazines.

In the next picture, you can see a view consisting of a selection of fields from two data tables. This
type of view may be very useful if you have one table that has many fields, or if you want to combine
information from several data tables. In the view o nly those fields appear that matter for a particular
application. Furthermore, the database administrator has the possibility to impose a view on the
database, in such a way that confidential fields are hidden from particular users. Some users can use
one subset of fields, other user may be authorized to use another subset of fields. Sensitive data can
be hidden from users that aren't authorized to see or use it.

Combining these two types of views (record subset and fields subset) you get the next picture:

VIRTUAL FIELD
Another possibility with views is to create a virtual field, i.e. a field that seems to be part of a data
tables, but actually isn't. An example of this is in the next picture: the field price_in_guilders is
constructed with the fields currency and price of the original table:
