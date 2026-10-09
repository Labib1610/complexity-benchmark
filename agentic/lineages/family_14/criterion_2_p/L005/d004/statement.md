# Thermal Stabilization Network

Time limit: 2 s   Memory limit: 256 MB

## Description

A modular orbital facility consists of **n** modules, indexed from 1 to **n**. Among these, a specific list of **t** modules are designated as critical and require synchronized thermal stabilization. The facility features **m** proposed thermal conduits, each connecting a pair of modules and requiring a specific amount of energy to activate.

The proposed conduits are arranged such that thermal exchange can be routed between any two modules via exactly one unique sequence of conduits.

Your task is to determine the minimum total energy required to activate a subset of conduits such that all critical modules are linked to one another, either directly or by relaying through other intermediate modules.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **n** ≤ 200000, **m** = **n** - 1, 1 ≤ **t** ≤ **n**).

The second line contains **t** distinct integers: the indices of the critical modules.

The following **m** lines each contain three integers **u**, **v**, and **w**. These specify a proposed conduit between module **u** and module **v** (where 1 ≤ **u**, **v** ≤ **n** and **u** ≠ **v**) having an activation energy of **w** (1 ≤ **w** ≤ 1000000).

## Output

Print a single integer representing the minimum total energy required to link all critical modules.

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

In Example 1 the critical modules 1 and 4 are linked only through 2 and 3, so all three conduits (5+1+2 = 8) are needed. In Example 2 there is one critical module, so no conduits are needed.