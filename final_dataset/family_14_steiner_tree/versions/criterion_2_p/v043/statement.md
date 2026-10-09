# Activating the Network

Time limit: 2 s   Memory limit: 256 MB

## Description

A large facility contains **n** workstations. You are provided with a list of **m** inactive data links, each capable of joining a specific pair of workstations for a given activation fee.

The blueprint for the facility has two specific properties regarding these **m** available links:
1. If all **m** links were activated, data could flow between any two workstations in the facility.
2. The layout contains no redundancy: if all **m** links were active, the failure of any single link would split the workstations into two disconnected groups that could no longer communicate with each other.

A specific group of **t** workstations are designated as *critical*. Your task is to activate a subset of the available links such that all critical workstations can exchange data with one another (this may involve routing data through non-critical workstations).

Determine the minimum total activation fee required to ensure all critical workstations are connected.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the identifiers of the critical workstations.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing an available link between workstation **u** and workstation **v** that has an activation fee of **w**.

## Output

Print a single integer: the minimum total activation fee required to connect all critical workstations.

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
