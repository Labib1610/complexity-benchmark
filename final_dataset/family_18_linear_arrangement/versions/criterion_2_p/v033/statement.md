# Problem B — Backbone Trenching for a Reporting Hierarchy

Time limit: 5 s   Memory limit: 256 MB

## Description
A monitoring installation places its units along a single straight line of mounting slots, one unit per slot, with as many slots as units — a one-to-one placement of units onto positions numbered along the line. The reporting relationships between units are structured such that there is exactly one sequence of reporting links connecting any given pair of units.

Each reporting link is carried by a cable whose length equals the number of slot positions between the two units it joins; connector details and reporting direction do not affect this length. The installation has a single **total** cabling budget covering the sum of all link lengths — there is no per-link cap and no restriction on cables sharing the run.

Find a one-to-one placement of the units onto the line whose total link length is at most the budget, or report that the budget cannot be met. (Because the links are structured to connect all units with exactly $n-1$ cables rather than an arbitrary web, the structure is more regular than a general arrangement, but the total-length objective is still what must be respected.)

## Input
First line: three integers $n$, $m$, $B$. Each of the next $m$ lines contains two integers $u$ and $v$ — representing a reporting link between unit $u$ and unit $v$. (It is guaranteed that $m = n-1$ and that a sequence of links connects any two units.)

## Output
Print `YES` then a line with $n$ integers — the position (1..n, a permutation) of unit 1, 2, ..., n — such that the total link length is $\le B$. Otherwise print `NO`.

## Example

### Input
```text
4 3 4
1 2
1 3
1 4
```

### Output
```text
YES
2 1 3 4
```
