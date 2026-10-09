# Problem A — State Synchronization Modules

Time limit: 5 s   Memory limit: 256 MB

## Description

A large-scale control system maintains **n** state variables, numbered 1 through **n**. Among these, exactly **t** variables are designated as critical synchronization points.

You are tasked with ensuring that all critical synchronization points always hold the identical state. To achieve this, you can install bidirectional synchronization modules from a provided catalog. When a module is installed between two different variables, it enforces a strict equality between them. This equality is transitive: if variable A is synchronized with variable B, and variable B is synchronized with variable C, then variable A is guaranteed to be identical to variable C.

Your goal is to select a subset of the available modules such that all **t** critical synchronization points are forced to be identical, either directly or through a chain of intermediate variables. Variables that are not designated as critical are completely optional: they can be utilized as intermediate links if doing so reduces the overall expense, or they can be ignored entirely.

Calculate the minimum total expense required to procure a set of modules that fully synchronizes all critical points.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ t ≤ 10). The integer **t** is the number of critical synchronization points.
The second line provides **t** distinct integers representing the identifiers of these critical variables.
The subsequent **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), describing a module that enforces equality between variable **u** and variable **v** for an installation cost of **w**.
It is guaranteed that the available modules can successfully synchronize all critical points.

## Output

Print a single integer: the minimum total expense to synchronize all critical synchronization points.

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

In Example 1, utilizing the optional variable 4 as an intermediate (costing 1+1+1 = 3) is more economical than enforcing equality among the three critical points directly (which would cost 4). In Example 3, there is only a single critical point, so no synchronization modules are required.