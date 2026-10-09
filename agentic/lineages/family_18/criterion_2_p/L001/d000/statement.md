# Problem B — Backbone Trenching for a Reporting Hierarchy

Time limit: 5 s   Memory limit: 256 MB

## Description
A monitoring installation places its units along a single straight line of mounting slots, one unit per slot, with as many slots as units — a one-to-one placement of units onto positions numbered along the line. The reporting relationships between units form a strict hierarchy: apart from a single top-level unit, every unit reports upward to exactly one parent unit, so the reporting links form a connected, loop-free structure spanning all units.

Each reporting link is carried by a cable whose length equals the number of slot positions between the two units it joins; connector details and reporting direction do not affect this length. The install has a single **total** cabling budget covering the sum of all link lengths — there is no per-link cap and no restriction on cables sharing the run.

Find a one-to-one placement of the units onto the line whose total link length is at most the budget, or report that the budget cannot be met. (Because the links form a hierarchy rather than an arbitrary web, the structure is more regular than a general network, but the total-length objective is still what must be respected.)

## Input
First line: three integers $n$, $m$, $B$. The integer $n$ is the headcount of units. The integer $m$ is the number of cables, which is exactly the headcount of units excluding the single top-level unit.
Each of the next $m$ lines: two integers $u$ $v$ (identifying units by positive integers up to the headcount) — a reporting link.

## Output
Print `YES` then a line with $n$ integers — assigning each unit $1, 2, \dots, n$ to a distinct slot position from $1$ up to the headcount — such that the total stretch is $\le B$. Otherwise print `NO`.

## Example

**Input:**
```
5 4 5
1 2
1 3
3 4
3 5
```

**Output:**
```
YES
2 1 4 3 5
```
