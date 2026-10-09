# Problem B — Backbone Trenching for a Reporting Hierarchy

Time limit: 5 s   Memory limit: 256 MB

## Description
A monitoring installation places its units along a single straight line of mounting slots, one unit per slot, with as many slots as units — a one-to-one placement of units onto positions numbered along the line. The reporting relationships between units form a strict hierarchy: apart from a single top-level unit, every unit reports upward to exactly one parent unit, so the reporting links form a connected, loop-free structure spanning all units.

Each reporting link is carried by a cable whose length equals the number of slot positions between the two units it joins; connector details and reporting direction do not affect this length. The install has a single **total** cabling budget covering the sum of all link lengths — there is no per-link cap and no restriction on cables sharing the run.

Find a one-to-one placement of the units onto the line whose total link length is at most the budget, or report that the budget cannot be met. (Because the links form a hierarchy rather than an arbitrary web, the structure is more regular than a general network, but the total-length objective is still what must be respected.)

## Input
The first line contains three integers $n$, $m$, and $B$. The integer $m$ represents the exact number of cables required to form the connected, loop-free hierarchy among the $n$ units. 
Each of the next $m$ lines contains two integers $u$ and $v$ — a reporting link between unit $u$ and unit $v$.

## Output
Print `YES` then a line with $n$ integers — the position (from $1$ to $n$, forming a permutation) of units $1, 2, \dots, n$ — such that the total cable length is at most $B$. Otherwise, print `NO`.

## Example

### Input
```text
4 3 4
1 2
2 3
2 4
```

### Output
```text
YES
1 2 3 4
```
