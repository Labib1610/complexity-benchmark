# Problem B — Backbone Trenching for a Reporting Installation

Time limit: 5 s   Memory limit: 256 MB

## Description
A monitoring installation places its units along a single straight line of mounting slots, one unit per slot, with as many slots as units — a one-to-one placement of units onto positions numbered along the line. 

The reporting relationships between units are formed as follows: starting with one initial unit, every subsequent unit is integrated by creating exactly one direct reporting link between it and a previously integrated unit. This ensures that signals can pass between any two units through a unique sequence of links.

Each reporting link is carried by a cable whose length equals the number of slot positions between the two units it joins; connector details and reporting direction do not affect this length. The install has a single **total** cabling budget covering the sum of all link lengths — there is no per-link cap and no restriction on cables sharing the run.

Find a one-to-one placement of the units onto the line whose total link length is at most the budget, or report that the budget cannot be met. (Because the links are formed in this specific sequence rather than an arbitrary web, the structure is more regular than a general network, but the total-length objective is still what must be respected.)

## Input
First line: three integers n, m, B. Each of the next m lines: two integers u v — a link.
(The links are formed as described: m = n-1.)

## Output
Print `YES` then a line with n integers — the position (1..n, a permutation) of unit 1,2,...,n — such that the total stretch is <= B. Otherwise print `NO`.

## Example

### Input
```
3 2 2
1 2
1 3
```

### Output
```
YES
2 1 3
```
