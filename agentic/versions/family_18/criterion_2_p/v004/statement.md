# Problem B — Backbone Trenching for a Reporting Hierarchy

Time limit: 5 s   Memory limit: 256 MB

## Description
A monitoring installation places $n$ units along a single straight line of mounting slots, one unit per slot, with as many slots as units — a one-to-one placement of units onto positions numbered $1$ to $n$ along the line. This requires selecting one specific arrangement from the $n!$ possible permutations.

The units are connected according to a given set of reporting links. Each reporting link is carried by a cable whose length equals the number of slot positions between the two units it joins; connector details and reporting direction do not affect this length. The install has a single total cabling budget covering the sum of all link lengths — there is no per-link cap and no restriction on cables sharing the run. The reporting relationships between units form a strict hierarchy: apart from a single top-level unit, every unit reports upward to exactly one parent unit, so the reporting links form a connected, loop-free structure spanning all units.

Find a one-to-one placement of the units onto the line whose total link length is at most the budget, or report that the budget cannot be met. (Because there are $n!$ possible permutations, the space of arrangements is large, but the total-length objective is what must be respected.)

## Input
First line: three integers $n$, $m$, $B$. 
Each of the next $m$ lines: two integers $u$ $v$ — a reporting link. 
(The links form a strict hierarchy: $m = n-1$.)

## Output
Print `YES` then a line with $n$ integers — the position (1..$n$, a permutation) of unit 1, 2, ..., $n$ — such that the total stretch is $\le B$. Otherwise, print `NO`.

## Example

### Input
```text
5 4 5
1 2
1 3
3 4
3 5
```

### Output
```text
YES
4 5 3 1 2
```
