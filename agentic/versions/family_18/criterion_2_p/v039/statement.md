# Problem B — Power Collection Trenching on a Ridge

Time limit: 5 s   Memory limit: 256 MB

## Description
A wind farm deploys its turbines along a single straight access road, assigning one turbine per foundation slot, with exactly as many slots as turbines — a one-to-one placement of turbines onto positions numbered along the road. The power collection network between turbines forms a strict hierarchy: apart from a single substation turbine, every turbine feeds power to exactly one parent turbine, so the collection lines form a connected, loop-free structure spanning all turbines.

Each collection line requires a trench whose length equals the number of slot positions between the two turbines it joins; trenching depth and power flow direction do not affect this length. The project has a single total trenching budget covering the sum of all line lengths — there is no per-line cap and no restriction on lines sharing the same trench space.

Find a one-to-one placement of the turbines onto the access road whose total trench length is at most the budget, or report that the budget cannot be met. (Because the lines form a hierarchy rather than an arbitrary web, the structure is more regular than a general network, but the total-length objective is still what must be respected.)

## Input
The first line contains three integers $n$, $m$, and $B$ — the number of turbines, the number of collection lines, and the total trenching budget.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating a collection line between turbines $u$ and $v$.
(The network is a tree: $m = n - 1$.)

## Output
Print `YES` then a line with $n$ integers — the position (from $1$ to $n$, forming a permutation) of turbines $1, 2, \dots, n$ — such that the total trench length is $\le B$. Otherwise print `NO`.

## Example

**Input:**
```
5 4 6
1 2
1 3
3 4
3 5
```

**Output:**
```
YES
3 2 4 1 5
```
