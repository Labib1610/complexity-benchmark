# Problem B — Backbone Trenching for a Reporting Hierarchy

Time limit: 5 s   Memory limit: 256 MB

## Description
Deploying a monitoring installation is a multi-stage process. In the first stage, site surveyors have already identified the necessary reporting hierarchy and prepared a single straight line of mounting slots. There is exactly one unit per slot, with as many slots as units — requiring a one-to-one placement of units onto positions numbered along the line. The required reporting relationships between units form a strict hierarchy: apart from a single top-level unit, every unit reports upward to exactly one parent unit, so the reporting links form a connected, loop-free structure spanning all units.

Your task represents the second stage: layout optimization. Each reporting link is carried by a cable whose length equals the number of slot positions between the two units it joins; connector details and reporting direction do not affect this length. The install has a single **total** cabling budget covering the sum of all link lengths — there is no per-link cap and no restriction on cables sharing the run. You must find a one-to-one placement of the units onto the line whose total link length is at most the budget, or report that the budget cannot be met. (Because the links form a hierarchy rather than an arbitrary web, the structure is more regular than a general network, but the total-length objective is still what must be respected.)

Once your layout is complete, the final stage begins: procurement will order the exact cable lengths dictated by your placement, and technicians will install the physical wires.

## Input
First line: three integers n, m, B. Each of the next m lines: two integers u v — an edge.
(The graph is a tree: m = n-1.)

## Output
Print `YES` then a line with n integers — the position (1..n, a permutation) of node 1,2,...,n —
such that the total stretch is <= B. Otherwise print `NO`.

## Example

### Input
```
5 4 5
1 2
1 3
3 4
3 5
```

### Output
```
YES
4 5 2 1 3
```
