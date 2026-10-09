# Problem B — Backbone Trenching for a Reporting Hierarchy

Time limit: 5 s   Memory limit: 256 MB

## Description
A monitoring installation must assign its $n$ units to a single straight line of mounting slots. There are $n!$ possible one-to-one placements of the units onto the positions numbered $1$ to $n$ along the line, creating a massive configuration space to evaluate. 

The units are connected by a network of $m$ reporting links. These relationships form a strict hierarchy: apart from a single top-level unit, every unit reports upward to exactly one parent unit, so the reporting links form a connected, loop-free structure spanning all units.

Each reporting link is carried by a cable whose length equals the number of slot positions between the two units it joins; connector details and reporting direction do not affect this length. The install has a single **total** cabling budget covering the sum of all link lengths for the entire network — there is no per-link cap and no restriction on cables sharing the run.

You must search the space of permutations to find a one-to-one placement of the units onto the line whose total link length is at most the budget, or report that the budget cannot be met by any possible arrangement.

## Input
First line: three integers $n$, $m$, $B$. 
Each of the next $m$ lines: two integers $u$ and $v$ representing a reporting link.
($m = n-1$.)

## Output
Print `YES` then a line with $n$ integers — the position ($1..n$, a permutation) of node $1, 2, \dots, n$ — such that the total stretch is $\le B$. Otherwise print `NO`.

## Example
**Input**
```
3 2 2
1 2
1 3
```

**Output**
```
YES
2 1 3
```
