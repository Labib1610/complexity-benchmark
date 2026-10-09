# Problem A — Data Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

A complex system consists of **n** modules (numbered 1 through **n**). A specific subset of **t** critical modules must be able to share data with each other. 

You can establish two-way data links between certain pairs of modules. Each potential link requires a specific amount of power to maintain. 

Data sharing operates across established links: data can flow directly between two modules if a link is established between them. Furthermore, this flow is transitive: if data can flow between module A and module B, and between module B and module C, then data can flow between module A and module C.

Your goal is to select a set of links to establish such that data can flow between any two critical modules. You may establish links involving non-critical modules if using them as relays reduces the overall power required.

Find the minimum total power required to establish a valid set of links.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the critical modules.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing a potential two-way data link between module **u** and module **v** that requires **w** units of power to maintain.
It is guaranteed that there exists at least one set of links that allows all critical modules to share data.

## Output

Print a single integer: the minimum total power required to establish links such that all critical modules can share data with each other.

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

In Example 1, establishing links through the non-critical module 4 (requiring 1+1+1 = 3 power) is more efficient than linking the three critical modules directly (which would require 2+2 = 4 power). In Example 3, there is only one critical module, so no links need to be established (0 power).
