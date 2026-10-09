# Problem A — Resonant Frequencies

Time limit: 5 s   Memory limit: 256 MB

## Description

A laboratory contains **n** tuning forks, numbered 1 to **n**. You have been tasked with harmonizing a specific subset of **t** primary tuning forks. To achieve this harmonization, the primary forks must be physically joined together.

You can join forks by applying silver solder between certain pairs. You are given a list of pairs of forks that can be soldered, along with the amount of silver required for each pair. You may also solder any of the remaining non-primary tuning forks; sometimes using these additional forks as junction points requires less total silver than soldering the primary forks directly to one another.

Determine the minimum total amount of silver needed to apply solder such that every primary tuning fork is connected to every other primary tuning fork, either directly or through a sequence of soldered forks.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the primary tuning forks.
Each of the following **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that tuning fork **u** and tuning fork **v** can be soldered together using **w** units of silver.
It is guaranteed that it is possible to connect all primary forks using the available soldering options.

## Output

Print a single integer: the minimum total units of silver required to connect all primary tuning forks.

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

In Example 1, soldering the three primary forks (1, 2, and 3) to the non-primary fork 4 requires 1+1+1 = 3 units of silver. This is more efficient than soldering the primary forks directly to each other (which would require at least 4 units). In Example 3, there is only one primary fork, so no soldering is necessary.
