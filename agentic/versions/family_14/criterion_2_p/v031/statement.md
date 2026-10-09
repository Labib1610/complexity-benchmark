# Problem B — Activating the Critical Modules

Time limit: 2 s   Memory limit: 256 MB

## Description

A software architecture has **n** modules (numbered 1..n). Certain pairs of modules can be joined by an active data pipe at a given cost. Among the modules, **t** are **critical** and must all end up connected to each other through the pipes you activate (directly or through intermediate relay modules).

In this architecture the available data pipes form a strict layout: they connect all modules, there are exactly **n − 1** pipes, and between any two modules there is exactly one possible data route.

Activate a set of data pipes of minimum total cost so that all critical modules are connected. Report that minimum total cost.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the ids of the critical modules.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a data pipe joining modules u and v at cost w. The pipes form the layout described above.

## Output

Print a single integer: the minimum total cost to connect all critical modules.

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

In Example 1 the critical modules 1 and 4 are joined only through 2 and 3, so all three pipes (5+1+2 = 8) are needed. In Example 2 there is one critical module, so no pipes are needed.
