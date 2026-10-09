# Priority Site Connectivity

Time limit: 2 s   Memory limit: 256 MB

## Description

A facility network has **n** stations (numbered 1..n). Certain pairs of stations can be joined by a conduit at a given cost. Among the stations, **t** are designated as **essential** and must all end up connected to each other through the conduits you establish (directly or through intermediate stations).

In this network, the available conduit options form a specific layout: they connect all stations, there are exactly **n − 1** options, and between any two stations there is exactly one possible route without revisiting any station. 

Because of this layout, connecting all essential stations is equivalent to ensuring that for every pair of essential stations, the single possible route between them is fully contained within your established set.

Establish a set of conduits of minimum total cost so that all essential stations are connected. Report that minimum total cost.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the ids of the essential stations.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a conduit joining stations u and v at cost w. The options form the layout described above.

## Output

Print a single integer: the minimum total cost to connect all essential stations.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```

## Note

In Example 1 the essential stations 1 and 4 are joined only through 2 and 3, so all three conduits (5+1+2 = 8) are needed. In Example 2 there is one essential station, so no conduits are needed.