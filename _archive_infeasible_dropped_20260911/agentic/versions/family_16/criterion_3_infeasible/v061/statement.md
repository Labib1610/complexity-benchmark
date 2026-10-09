# Problem C — Statutory Limit Violations

Time limit: 2 s   Memory limit: 256 MB

## Description

A regulatory agency handles **j** independent dossiers. The review process involves two distinct stages: Desk 1 and Desk 2. Every dossier must first be completely reviewed at Desk 1 before it can be transferred to Desk 2. You are given the number of microseconds each dossier needs exclusively at Desk 1 and Desk 2. A Desk can only handle a single dossier at any given moment.

A statutory limit of **T** microseconds is imposed on the entire batch. Every dossier must complete its journey through both Desks before this limit expires.

For all test cases provided, this statutory limit is mathematically impossible to satisfy, no matter what order the dossiers are processed in. Do not attempt to find a valid ordering. Instead, your task is to identify and output the specific rejection code that proves the limit is breached.

The input data is guaranteed to trigger exactly one of the following two rejection codes. Output the one that applies:

- **An individual dossier exceeds the limit.** If the sequential time required by a single dossier (its duration at Desk 1 plus its duration at Desk 2) is strictly greater than **T**, output `JOB i`, where **i** (1-based) is the index of that dossier.
- **A Desk's cumulative volume exceeds the limit.** Because a Desk cannot review dossiers simultaneously, its minimum active time is the sum of its requirements across all dossiers. If this sum for Desk **c** (where **c** is 1 or 2) is strictly greater than **T**, output `LOAD c`.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the microseconds a dossier requires at Desk 1 and Desk 2, respectively.

## Output

Print a single line containing the applicable rejection code: either `JOB i` or `LOAD c`.

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, dossier 1 requires 70 + 60 = 130 > 100 microseconds in sequence, so `JOB 1` proves the limit is breached. In Example 2, no single dossier exceeds 150, but Desk 1 must process 50+50+50+50 = 200 > 150 microseconds of volume in total, so `LOAD 1` is the correct rejection code.
