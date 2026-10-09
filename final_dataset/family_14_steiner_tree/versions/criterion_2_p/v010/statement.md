# Problem B — Priority Infrastructure

Time limit: 2 s
Memory limit: 256 MB

## Description

A university is upgrading its communication infrastructure across **n** buildings (numbered 1 to **n**). There are **m** proposed conduit links, each connecting a pair of buildings and requiring a certain budget to activate. The proposed links are laid out such that, if all were activated, every building would be able to communicate with every other building.

The university has identified **t** priority buildings. Your task is to select a subset of the proposed conduit links to activate so that all priority buildings can communicate with each other (either directly or by relaying through other buildings, which do not need to be priority buildings). You must find a valid selection that keeps the total activation budget as low as possible, and report this minimum total budget.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1).
The second line contains **t** distinct integers: the identifiers of the priority buildings.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), representing a proposed conduit link between buildings **u** and **v** that costs **w** to activate. It is guaranteed that the full set of **m** links connects all **n** buildings.

## Output

Print a single integer: the minimum total activation budget required to ensure all priority buildings are connected to one another.

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
