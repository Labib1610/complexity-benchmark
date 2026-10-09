# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A system handles **j** items using two distinct resource types, resource 1 and resource 2. For each item, you are given its required usage time on resource 1 and resource 2. The system operates strictly under the following mechanics:
- An item must fully complete its usage of resource 1 before it can begin using resource 2.
- A resource can only be utilized by a single item at any given moment.

There is a strict time limit **T**: every item must completely finish its usage of both resources by time **T**.

For every input in this problem, it is **guaranteed that the time limit cannot be satisfied**, regardless of the sequence in which items are handled. Your task is not to search for a valid sequence; it is to **prove** the limit is impossible with a short certificate that can be checked directly against the input.

Exactly one of the following reasons always applies. Print the one that holds:

- **An individual item requires too much sequential time.** By the first rule, an item's time on resource 1 and resource 2 cannot overlap. If an item's two usage times add up to more than **T**, that item alone cannot finish by **T**.
  Print: `JOB i` — where **i** (1-based) is such an item.

- **A resource is over-utilized.** By the second rule, a resource handles items serially, meaning it must be active for at least the sum of all its usage times. If the total time required on resource 1 (or resource 2) exceeds **T**, the limit is impossible.
  Print: `LOAD c` — where **c** is 1 or 2, and the total required time on resource **c** exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required usage times of an item on resource 1 and resource 2.

## Output

Print a single line: `JOB i` (an item whose p1 + p2 exceeds T) or `LOAD c` (a resource c whose total usage time exceeds T).

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

In Example 1, item 1 needs 70 + 60 = 130 > 100 time units in sequence, so `JOB 1` proves the limit is impossible. In Example 2 no single item exceeds 150, but resource 1 must be utilized for 50+50+50+50 = 200 > 150 units of work in total, so `LOAD 1` is the certificate.
