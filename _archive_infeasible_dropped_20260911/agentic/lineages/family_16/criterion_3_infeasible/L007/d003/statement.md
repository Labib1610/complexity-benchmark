# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A manufacturing facility processes **j** distinct items. The production of each item involves exactly two sequential stages: it must first undergo preparation at stage 1, and upon completion, undergo finishing at stage 2. You are provided the duration required for each stage per item. Equipment at any stage can handle at most one item at any given moment.

The facility operates for a single shift of duration **T**. All items must be completely processed before the shift ends.

You are tasked with auditing production logs from failed facilities. For each log, the required production cannot possibly be completed within the shift, regardless of how the items are scheduled. Your objective is to generate a concise certificate that definitively proves the impossibility of the schedule. 

Exactly one of the following reasons always applies. Print the one that holds:

- `JOB i` — The **i**-th item (1-indexed), if its stage 1 preparation were to begin at time 0 and its stage 2 finishing were to follow immediately, would complete stage 2 strictly after time **T**.
- `LOAD c` — The equipment at stage **c** (where **c** $\in \{1, 2\}$), if it were to process its required tasks for all **j** items continuously starting from time 0 with zero idle time, would complete its final task strictly after time **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the duration required for the item at stage 1 and stage 2, respectively.

## Output

Print a single line containing the applicable certificate: either `JOB i` or `LOAD c`.

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