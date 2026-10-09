# Steam Pipe Diagnostics

Time limit: 2 s   Memory limit: 256 MB

## Description

A steam distribution network consists of **n** pressure valves, numbered 1 to **n**. The network is built with exactly **n − 1** pipes connecting them, forming a non-redundant layout where steam can travel between any two valves via exactly one unique sequence of pipes. Each pipe requires a specific amount of energy to pressurize.

A maintenance crew needs to run a diagnostic test on a target subset of **t** valves. To synchronize these valves, the crew must pressurize a set of pipes such that all **t** target valves can communicate pressure changes with each other, either directly or by routing through other valves. Non-target valves on the pressurized routes will simply pass the pressure along.

Determine the minimum total energy required to pressurize a set of pipes that connects all of the target valves.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers representing the identifiers of the target valves.
Each of the following **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating a pipe between valve **u** and valve **v** that requires **w** energy to pressurize.

## Output

Print a single integer representing the minimum total energy required to connect all target valves.

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
