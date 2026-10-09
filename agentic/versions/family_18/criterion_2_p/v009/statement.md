# Problem B — Backbone Trenching for a Reporting Hierarchy

Time limit: 5 s   Memory limit: 256 MB

## Description
The reporting relationships between units in a monitoring installation form a strict hierarchy: apart from a single top-level unit, every unit reports upward to exactly one parent unit, so the reporting links form a connected, loop-free structure spanning all units.

The installation is constrained by a single total cabling budget, which limits the sum of all link lengths. There is no per-link cap and no restriction on cables sharing a run.

To physically arrange the system, units are placed along a single straight line of mounting slots, one unit per slot, with as many slots as units — a one-to-one placement of units onto positions numbered along the line. Each reporting link is carried by a cable whose length equals the number of slot positions between the two units it joins; connector details and reporting direction do not affect this length.

Find a one-to-one placement of the units onto the line whose total link length is at most the budget, or report that the budget cannot be met. (Because the links form a hierarchy rather than an arbitrary web, the structure is more regular than a general network, but the total-length objective is still what must be respected.)

## Input
First line: three integers n, m, B. Each of the next m lines: two integers u v — an edge.
(The reporting relationships form a connected, loop-free structure: m = n-1.)

## Output
Print `YES` then a line with n integers — the position (1..n, a permutation) of node 1, 2, ..., n — such that the total stretch is <= B. Otherwise print `NO`.

## Example

### Input
```text
5 4 6
1 2
1 3
3 4
3 5
```

### Output
```text
YES
3 2 4 5 1
```
