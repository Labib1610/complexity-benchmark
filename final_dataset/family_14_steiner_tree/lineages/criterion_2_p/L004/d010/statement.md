# Logistics Network Integration

Time limit: 2 s
Memory limit: 256 MB

## Description

You are planning a logistics network involving $n$ facilities, numbered $1$ through $n$.

You have a list of $m$ potential two-way transit corridors. Each corridor connects a specific pair of facilities $u$ and $v$ and requires an investment of $w$ to establish.

The given list of potential corridors is sufficient to integrate the entire network: there are exactly $m = n - 1$ corridors available in total, and if you were to establish all of them, it would be possible to route shipments between any two facilities in the network (with exactly one unique route between any pair).

Your goal is to select a subset of these corridors to establish so that a specific group of $t$ priority facilities are fully connected. This means that for any two priority facilities, shipments must be able to travel between them using only the established corridors. Shipments may pass through non-priority facilities along the way. The connectivity of the remaining non-priority facilities is not required.

Because the given list of $m$ potential corridors provides exactly one unique route between any two facilities, the minimum-cost valid subset is uniquely determined. Specifically, a corridor must be established if and only if it lies on the unique route between at least one pair of priority facilities. Any corridor not lying on a route between two priority facilities can be safely omitted.

What is the minimum total investment required to establish this valid subset of corridors?

## Input

The first line contains three integers **n**, **m**, and **t**. The number of facilities is **n** (1 ≤ **n** ≤ 200000). The number of potential corridors **m** is always exactly **n** − 1. The number of priority facilities is **t** (1 ≤ **t** ≤ **n**).
The second line contains **t** distinct integers: the identifiers of the priority facilities.
Each of the next **m** lines contains three integers **u**, **v**, and **w**. These represent a potential corridor between facility **u** and facility **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), which costs **w** to establish (1 ≤ **w** ≤ 1000000).

## Output

Print a single integer: the minimum total investment required.

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