# Synchronized Zone Activation

Time limit: 2 s
Memory limit: 256 MB

## Description

You are configuring a distributed network of $n$ computational nodes, indexed $1$ through $n$.

You are provided with a catalog of $m$ optional bidirectional synchronization modules. Each module links two specific nodes $u$ and $v$ (without affecting any other nodes) and has an activation cost $w$.

The catalog of available modules provides minimal and complete connectivity: there are exactly $m = n - 1$ modules available, and if all were activated, there would be exactly one valid communication route between any two nodes in the network.

Your objective is to activate a subset of these modules to establish a synchronized zone. You must ensure that a specific list of $t$ critical nodes can all communicate with each other using only the activated modules. (That is, for any two critical nodes $a$ and $b$, data must be able to travel between them via a sequence of activated modules). The communication capabilities of the remaining non-critical nodes do not matter.

What is the minimum total activation cost of the modules you must select to satisfy this communication condition?

## Input

The first line contains three integers **n**, **m**, and **t**. The number of computational nodes is **n** (1 ≤ **n** ≤ 200000). The number of available modules **m** is always exactly **n** − 1. The number of critical nodes is **t** (1 ≤ **t** ≤ **n**).
The second line contains **t** distinct integers: the identifiers of the critical nodes.
Each of the next **m** lines contains three integers **u**, **v**, and **w**. These denote an optional module linking nodes **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), which costs **w** to activate (1 ≤ **w** ≤ 1000000).

## Output

Print a single integer: the minimum total cost required.

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