# Rail Network Maintenance

Time limit: 2 s   Memory limit: 256 MB

## Description

A regional transit authority manages **n** stations (numbered 1..n). Certain pairs of stations are linked by rail segments, each requiring a specific annual maintenance budget. Among the stations, **t** are designated as freight hubs and must all remain connected to each other via maintained rail segments (either directly or through intermediate stations).

The existing rail network was built without loops: it connects all stations, there are exactly **n − 1** segments, and between any two stations there is exactly one possible sequence of segments.

Select a set of rail segments to maintain at the minimum total budget so that all freight hubs are connected. Report that minimum total budget.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the ids of the freight hubs.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a rail segment joining stations u and v with an annual maintenance budget of w. The segments form the network described above.

## Output

Print a single integer: the minimum total budget to connect all freight hubs.

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

In Example 1 the freight hubs 1 and 4 are joined only through stations 2 and 3, so all three segments (5+1+2 = 8) must be maintained. In Example 2 there is one freight hub, so no segments need to be maintained.
