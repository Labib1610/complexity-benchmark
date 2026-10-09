# Inevitable Failure Certificate

Time limit: 2 s
Memory limit: 256 MB

## Description

A production facility is tasked with fulfilling **j** work orders. Each order must pass through exactly two sequential stages. Stage 1 is executed at Station 1, and upon its completion, Stage 2 is executed at Station 2. 

The facility operates under the following mechanics:
- Station 1 processes a single order's Stage 1 at any given moment.
- Station 2 processes a single order's Stage 2 at any given moment.
- An order's Stage 2 cannot commence until its Stage 1 has completely finished.

The facility has been given a strict time limit **T** by which all orders must be completely finished. However, it is fundamentally impossible to meet this time limit, regardless of how the orders are sequenced. Your task is not to attempt to sequence them, but to output a formal justification proving that the limit **T** cannot be met.

Exactly one of the following reasons will apply to the provided data. Output the one that holds:

- **Sequential Exceedance**: Because an order's Stage 2 must happen after its Stage 1, if a single order's Stage 1 duration and Stage 2 duration sum to a value strictly greater than **T**, that order alone cannot finish within the limit. Print `JOB i`, where **i** is the 1-based index of such an order.
- **Capacity Exceedance**: Because a station works sequentially, if a station's total assigned duration across all orders is strictly greater than **T**, that station cannot complete its work within the limit. Print `LOAD c`, where **c** is the station number (1 or 2) whose total required active time exceeds **T**.

## Input

The first line provides two integers **j** and **T** (1 ≤ **j** ≤ 200000, 1 ≤ **T** ≤ 1000000000).
The subsequent **j** lines each provide two integers **p1** and **p2** (1 ≤ **p1**, **p2** ≤ 1000000). These represent the duration required for Stage 1 and Stage 2 of the order, respectively.

## Output

Output a single line containing either `JOB i` (where order **i** requires a total sequential time greater than **T**) or `LOAD c` (where station **c** requires a total processing time greater than **T**).

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

In Example 1, order 1 requires 70 + 60 = 130 > 100 time units in sequence, so `JOB 1` proves the limit is impossible. In Example 2, no single order exceeds 150, but Station 1 must process 50 + 50 + 50 + 50 = 200 > 150 units of work in total, so `LOAD 1` is the justification.
