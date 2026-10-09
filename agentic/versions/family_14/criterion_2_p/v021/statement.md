# Problem B — Excavating the Archives

Time limit: 2 s   Memory limit: 256 MB

## Description

An ancient underground complex consists of **n** chambers, numbered 1 to **n**. There are **m** collapsed tunnels, each connecting a specific pair of chambers. Clearing a tunnel requires a certain number of labor hours. The architectural design of the complex guarantees that there are exactly **m = n - 1** tunnels, and that it is possible to navigate between any two chambers if all tunnels are cleared.

A team of archaeologists has identified **t** specific chambers that contain important murals. They wish to clear a subset of the tunnels such that all **t** mural chambers belong to a single connected network (i.e., it is possible to travel between any two mural chambers using only the cleared tunnels). Other chambers may also be part of this cleared network.

Determine the minimum total labor hours required to clear a set of tunnels that connects all **t** mural chambers.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the IDs of the chambers containing murals.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): indicating a collapsed tunnel between chamber **u** and chamber **v** that requires **w** labor hours to clear.

## Output

Print a single integer: the minimum total labor hours to connect all mural chambers.

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
