# Problem A — Grid Integration

Time limit: 5 s   Memory limit: 256 MB

## Description

An offshore wind farm has **n** platforms (numbered 1..n). Certain pairs of platforms can be joined by a submarine cable at a given material cost. Among the platforms, **t** contain **primary turbines** and must all end up integrated into a single continuous grid through the cables you lay (directly or through intermediate platforms). The remaining platforms are structural supports: you may route cables through them if it minimizes total expenditure, or bypass them entirely.

Install a set of submarine cables of minimum total material cost so that all primary turbine platforms are integrated. Report that minimum total cost.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the primary turbine platforms.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a submarine cable option joining platforms u and v at cost w.
The available cable options are sufficient to integrate all primary turbine platforms.

## Output

Print a single integer: the minimum total material cost to integrate all primary turbine platforms.

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

In Example 1, routing cables through the structural support platform 4 (costs 1+1+1 = 3) is cheaper than joining the three primary turbine platforms directly (which would cost 4). In Example 3 there is only one primary turbine platform, so no cabling is needed.
