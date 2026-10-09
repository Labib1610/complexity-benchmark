# Problem B — Backbone Trenching for a Reporting System

Time limit: 5 s   Memory limit: 256 MB

## Description
A monitoring installation places its units along a single straight line of mounting slots, one unit per slot, with as many slots as units — a one-to-one placement of units onto positions numbered $1$ to $n$ along the line. The reporting relationships between units form a strict system: apart from a single primary unit, every unit reports to exactly one other unit, so the reporting links form a fully joined structure spanning all units without any circular sequences of links.

Each reporting link is carried by a cable whose length equals the number of slot positions between the two units it joins; connector details and reporting direction do not affect this length. The install has a single total cabling budget covering the sum of all link lengths — there is no per-link cap and no restriction on cables sharing the run.

Find a one-to-one placement of the units onto the line whose total link length is at most the budget, or report that the budget cannot be met.

## Input
First line: three integers $n$, $m$, $B$. Each of the next $m$ lines: two integers $u$ $v$ — a reporting link between unit $u$ and unit $v$.
(The links form the structure described above: $m = n-1$.)

## Output
Print `YES` then a line with $n$ integers — the position ($1 \dots n$, a permutation) of unit $1, 2, \dots, n$ — such that the total length of all cables is $\le B$. Otherwise print `NO`.

## Example

**Input**
```text
5 4 6
1 2
1 3
3 4
3 5
```

**Output**
```text
YES
3 2 4 5 1
```
