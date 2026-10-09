# Infrastructure Project

Time limit: 2 s   Memory limit: 256 MB

## Description

A campus infrastructure project involves **n** buildings (numbered 1 to **n**). The administration has identified **m** potential fiber-optic trenches that can be dug between specific pairs of buildings. Each trench has an associated excavation cost. The layout of these potential trenches is strictly regulated such that, if all **m** trenches were excavated, there would be exactly one sequence of trenches connecting any given pair of buildings.

Among the **n** buildings, a specific group of **t** locations are designated as primary server hubs.

The project requires ensuring that every primary server hub is able to exchange data with every other primary server hub. Data can be routed through any number of intermediate buildings, provided the trenches between them have been excavated. Determine the lowest possible total excavation cost to connect all **t** primary server hubs.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the ids of the primary server hubs.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a potential trench between buildings u and v with an excavation cost of w. The layout of these trenches follows the strict regulation described above.

## Output

Print a single integer: the lowest possible total excavation cost to connect all primary server hubs.

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

In Example 1, the primary server hubs 1 and 4 are joined only through buildings 2 and 3, so all three trenches (5+1+2 = 8) must be excavated. In Example 2, there is only one primary server hub, so no excavation is needed.
