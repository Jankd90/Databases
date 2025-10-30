# Chapter 2: Database Design (Continued)

INTRODUCTION

In the previous chapter we considered the departments -and-employees databa se and used it to
introduce a number of important principles of database design. In particular, we showed how to deal
with one -to-many relationships. In this chapter we treat a more complicated kind of relationship,
namely, the many -to-many relationship. Again we approach the problem by way of a well -known but
useful example, this time the suppliers -and-parts example.

SUPPLIERS AND PARTS: A GOOD DESIGN

The suppliers -and-parts database is intended to model the following situation:

 A company uses a number of different kinds of parts and obtains them in the form of shipments
```
sql
from a number of dif ferent suppliers.
```

 Each supplier supplies many different kinds of parts; each kind of part is supplied by many different
suppliers. However, at any given time there will be at most one shipment out standing for a given kind
of part from a given supplier. Different shipments may involve different quantities of the part being
shipped.

 Each supplier has a supplier number (unique), a name, a status (i.e., a rating value), and a city
(supplier location).

 Each part (or, rather, each kind of part) has a part number (unique), a name, a color, a weight, and a
city (location at which parts of that kind are stored).

Figure 2.1 shows a design that is intuitively (and actually) a good one for this database.
Figure 2.2 shows some sample values to illustrate that design.

supplier
suppno sname Status city

part
partno pname Color weight city

shipment
suppno partno Quantity
figure 2.

Table supplier:

suppno sname status city
S1 Smith 20 London
S2 Jones 10 Paris
S3 Blake 30 Paris
S4 Clark 20 London
S5 Adams 30 Athens

Table Part:

partno pname color weight city
P1 Nut red 12 London
P2 Bolt green 17 Paris
P3 Screw blue 17 Rome
P4 Screw red 14 London
P5 Cam blue 12 Paris
P6 Cog red 19 London

Table Shipment:

suppno partno quantity
S1 P1 300
S1 P2 200
S1 P3 400
S1 P4 200
S1 P5 100
S1 P6 100
S2 P1 300
S2 P2 400
S3 P2 200
S4 P2 200
S4 P4 300
S4 P5 400

DISCUSSION

Note first of all that the suppliers -and-parts example does involve a ma ny-to-many relationship,
because (a) for each supplier there will typically be any number of outstanding shipments and hence
many corresponding parts, and (b) for each part, likewise, there will typically be many outstanding
shipments, from many distinct suppliers. More succinctly: For each supplier there are many parts; for
each part there are many suppliers. How did we arrive at our "good" database design? Well, note first
of all tha t tables SUP PLIER and PART are obtained by applicati on of the principles established in the
previous chapter:

 Table SUPPLIER consists of a primary key (SUPPNO) identifying some entity type (suppliers),
together with three additional fields (SNAME, STATUS, and CITY) representing properties of that entity
type.

 Table PART consists of a primary key (PARTNO) identifying some entity type (parts), together with
four additional fields (PNAME, COLOR, WEIGHT, and CITY) representing properties of that entity type.

Turning now to shipments, we observe first that we cannot put shipment information into the
SUPPLIER table. If we did, we would get a design of the form shown in Fig. 2.3, say. That design
obviously violates the principles already established in the pre vious chapter. We cannot put shipment
informa tion into the PART table either, for exactly the same reason. So we must introduce an other
table, the SHIPMENT table. Each record in that table repre sents a single shipment and specifies (a) the
supplier involv ed, (b) the part involved, and (c) the shipment quantity. Note the follow ing points:

 Supplier

Suppno
Sname
Status
City
Partno_1
Quantity_1
…….

....... partno_9 quantity_9

 Fields SHIPMENT.SUPPNO and SHIPMENT.PARTNO are foreign keys, matching primary keys
SUPPLIER.SUP PNO and PART.PARTNO, respectively. See Fig. 2.4.

 Field SHIPMENT.QUANTITY does not represent a property of a supplier, nor of a part, but of a
shipment. Shipments are en tities in their own right, just like suppliers and parts. As entities, they can
have properties of their own. (Note, however, that ship ments are not independent entities, in the same
way that suppliers and parts are independent entities; they depend on suppliers and parts, in the sense
that a given shipment can exist only if the corre sponding supplier and part both exist also.)

 As entities, shipments must have unique identifiers and hence primary keys. The primary key of the
SHIPMENT table is the combination (SHIPMENT.SUPPNO, SHIPMENT.PARTNO): It requires both a
supplier number and a part number together to identify a shipment u niquely, as the sample data
shown in Fig. 2.2 illustrates. (Recall from the definition in
