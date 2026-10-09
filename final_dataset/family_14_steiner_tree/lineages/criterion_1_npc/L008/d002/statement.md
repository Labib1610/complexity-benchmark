# Problem A — Grid Integration

Time limit: 5 s   Memory limit: 256 MB

## Description

An offshore wind farm has **n** platforms (numbered 1..n). Certain pairs of platforms can be joined by a submarine cable at a given material cost.

Among the platforms, **t** contain **primary turbines**. 

Initially, each platform operates as its own independent energy grid. Building a submarine cable between platform *u* and platform *v* merges the energy grid containing *u* and the energy grid containing *v* into a single unified energy grid.

You must select a subset of cables to build such that, after all selected cables are built and the corresponding grids are merged, all **t** primary turbines end up in the exact same unified energy grid. (Platforms without primary turbines may also be part of this grid).

Determine the minimum total material cost of a set of cables that satisfies this requirement.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the platforms that contain primary turbines.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a submarine cable option joining platforms u and v at cost w.
The available cable options are sufficient to allow all primary turbines to end up in the same energy grid.

## Output

Print a single integer: the minimum total material cost of the built cables.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, building the cables between platform 4 and platforms 1, 2, and 3 (total cost 1+1+1 = 3) merges their grids such that the three primary turbine platforms end up in the same energy grid. This is cheaper than building cables strictly between the primary turbine platforms themselves (which would cost 4). In Example 3 there is only one primary turbine platform, so it is already in its own energy grid and no cabling is needed.