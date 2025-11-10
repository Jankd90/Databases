# Chapter 12 — Files in the Database `TOP10USA`

---

## ARTISTS

| ARTIST_NO | NAME                     | COUNTRY |
|----------|--------------------------|---------|
| ...      | ...                      | ...     |
| 31       | The Dave Clark Five      | UK      |
| 32       | Betty Everett            | USA     |
| 33       | The Serendipity Singers  | USA     |
| 34       | Mary Wells               | UK      |
| 35       | The 4 Seasons            | USA     |
| 36       | Danny Williams           | USA     |
| 37       | Roy Orbison              | USA     |
| 38       | The Dixie Cups           | USA     |
| 39       | The Ray Charles Singers  | USA     |
| 40       | The Reflections          | USA     |
| **41**   | **Peter & Gordon**       | **UK**  |
| 42       | Billy J. Kramer          | UK      |
| 43       | Barbra Streisand         | USA     |
| 44       | Millie Small             | USA     |
| 45       | Gerry & The Pacemakers   | UK      |
| 46       | The Bachelors            | USA     |
| 47       | Johnny Rivers            | USA     |
| 48       | Stan Getz / Astrud Gilberto | USA  |
| 49       | Chuck Berry              | USA     |
| 50       | Roger Miller             | USA     |
| 51       | The Impressions          | USA     |
| 52       | Dusty Springfield        | UK      |
| 53       | Dean Martin              | USA     |
| 54       | The Supremes             | USA     |
| ...      | ...                      | ...     |

> **Total entries:** **77**

---

## RECORDS

| RECORD_NO | TITLE                             | ARTIST_NO | REC_CO |
|-----------|-----------------------------------|-----------|--------|
| ...       | ...                               | ...       | ...    |
| 39        | Do You Want to Know a Secret      | 15        | 24     |
| 40        | Dead Man's Curve                  | 14        | 14     |
| 41        | Bits and Pieces                   | 31        | 1      |
| 42        | My Guy                            | 34        | 31     |
| 43        | Ronnie                            | 35        | 3      |
| 44        | White on White                    | 36        | 28     |
| 45        | Love Me Do                        | 15        | 26     |
| 46        | It's Over                         | 37        | 32     |
| 47        | Chapel of Love                    | 38        | 33     |
| 48        | Love Me with All Your Heart       | 39        | 34     |
| 49        | (Just Like) Romeo & Juliet        | 40        | 35     |
| **50**    | **A World Without Love**          | **41**    | **19** |
| 51        | Little Children                   | 42        | 36     |
| 52        | Walk on By                        | 18        | 17     |
| 53        | P.S. I Love You                   | 15        | 26     |
| 54        | People                            | 43        | 12     |
| 55        | I Get Around                      | 26        | 19     |
| 56        | My Boy Lollipop                   | 44        | 37     |
| 57        | Don't Let the Sun Catch You Crying| 45        | 38     |
| 58        | Diane                             | 46        | 39     |
| ...       | ...                               | ...       | ...    |

> **Total entries:** **111**

---

## REC_COMP

| REC_CO | NAME             |
|--------|------------------|
| ...    | ...              |
| 15     | Okeh             |
| 16     | Mercury          |
| 17     | Scepter          |
| 18     | Decca            |
| **19** | **Capitol**      |
| 20     | Swan             |
| 21     | RCA              |
| 22     | ABC              |
| 23     | 20th Century     |
| 24     | Vee-Jay          |
| 25     | Montel           |
| 26     | Tollie           |
| 27     | Riviera          |
| 28     | United Artists   |
| ...    | ...              |

> **Total entries:** **55**

---

## CHARTS

| WEEK | RECORD_NO | POSITION |
|------|-----------|----------|
| ...  | ...       | ...      |
| 13   | 26        | 4        |
| 14   | 26        | 5        |
| 15   | 26        | 9        |
| 9    | 27        | 9        |
| 10   | 27        | 8        |
| 11   | 30        | 10       |
| 12   | 30        | 9        |
| 12   | 31        | 7        |
| 13   | 31        | 3        |
| ...  | ...       | ...      |

> **Total entries:** **520**  
> *(52 weeks × 10 positions = 520 records)*

---

## Database Summary — `TOP10USA`

| Table       | Rows | Purpose |
|-------------|------|-------|
| `ARTISTS`   | 77   | Artist info (name, country) |
| `RECORDS`   | 111  | Song titles + artist & label |
| `REC_COMP`  | 55   | Record company names |
| `CHARTS`    | 520  | Weekly Top 10 positions |

---

> **Key Relationships**  
> ```text
> artists.artist_no  → records.artist_no
> rec_comp.rec_co    → records.rec_co
> records.record_no  → charts.record_no
> ```

> **Rule of Thumb:**  
> *No data duplication — every fact stored **once**, linked by **keys**.*

---
```