# Chapter 10 Getting Familiar — SQL

---

## Instructions

> **Type your selection of commands** that we discussed above, to see how things work.  
> If you **mistype** a command, SQL will give a **warning** in a message box.  
> Select the **SQL icon** on the speed bar if you want to make **changes** to the command.

---

## Questions 1 — Find Answers Using SQL Only!

> **Let the computer do the entire job!**  
> **No cheating** — no manual lookup!

---

### a. What hits did **The Beatles** have?

```{toggle}
:label: Show details

blabla
```

```{toggle}
:label: Outer

Outer content.

```{}
:label: Inner
Inner content.

#### Step 1 — Find `artist_no`

```sql
SELECT artist_no
FROM   artists
WHERE  name = 'The Beatles';
````

> **Result:** (Assume 15)

---

#### Step 2 — Find song titles

```{toggle}
:label: Show SQL

    ```sql
    SELECT title
    FROM   records
    WHERE  artist_no = 15;
    ```
```

```sql
SELECT title
FROM   records
WHERE  artist_no = 15;
```

---

#### One Single Command (Nested)

```sql
SELECT title
FROM   records
WHERE  artist_no = (
    SELECT artist_no
    FROM   artists
    WHERE  name = 'The Beatles'
);
```

---

#### Modified for **The Beach Boys**

```sql
SELECT title
FROM   records
WHERE  artist_no = (
    SELECT artist_no
    FROM   artists
    WHERE  name = 'The Beach Boys'
);
```

---

### b. Which record titles have the word **'love'** in it?

```sql
SELECT title
FROM   records
WHERE  title LIKE '%love%';
```

> **Note:**
> 
> - % = wildcard (any characters)
> - Case-insensitive in most systems
> - Returns: _A World Without Love_, _Love Me Do_, etc.

---

### c. What is the **record number** of the song **'She Loves You'**?

```sql
SELECT record_no
FROM   records
WHERE  title = 'She Loves You';
```

> **Result:** (Assume 53)

---

### d. What **positions** did **'She Loves You'** occupy?

```sql
SELECT position
FROM   charts
WHERE  record_no = (
    SELECT record_no
    FROM   records
    WHERE  title = 'She Loves You'
)
ORDER BY week;
```

---

### e. Change to include **week numbers** as well

```sql
SELECT week, position
FROM   charts
WHERE  record_no = (
    SELECT record_no
    FROM   records
    WHERE  title = 'She Loves You'
)
ORDER BY week;
```

**Sample Output:**

|WEEK|POSITION|
|---|---|
|35|1|
|36|1|
|37|2|
|...|...|

---

### f. Which **artist(s)** perform **'She Loves You'**?

> _(Let the computer find it!)_


```sql
SELECT name
FROM   artists
WHERE  artist_no = (
    SELECT artist_no
    FROM   records
    WHERE  title = 'She Loves You'
);
```

**Result:**

```
NAME
The Beatles
```

---

## Final Summary — All Commands

```sql
-- a. Beatles hits (single command)
SELECT title
FROM   records
WHERE  artist_no = (SELECT artist_no FROM artists WHERE name = 'The Beatles');

-- a. Beach Boys hits
SELECT title
FROM   records
WHERE  artist_no = (SELECT artist_no FROM artists WHERE name = 'The Beach Boys');

-- b. Titles with 'love'
SELECT title
FROM   records
WHERE  title LIKE '%love%';

-- c. Record number of 'She Loves You'
SELECT record_no
FROM   records
WHERE  title = 'She Loves You';

-- d. Positions of 'She Loves You'
SELECT position
FROM   charts
WHERE  record_no = (SELECT record_no FROM records WHERE title = 'She Loves You')
ORDER BY week;

-- e. Weeks + positions
SELECT week, position
FROM   charts
WHERE  record_no = (SELECT record_no FROM records WHERE title = 'She Loves You')
ORDER BY week;

-- f. Artist of 'She Loves You'
SELECT name
FROM   artists
WHERE  artist_no = (SELECT artist_no FROM records WHERE title = 'She Loves You');
```

---

> **Pro Tip:** Use **subqueries** to avoid manual steps Use LIKE '%...%' for partial text search Use ORDER BY to sort results logically