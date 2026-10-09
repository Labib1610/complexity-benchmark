# Datacenter Activation

Time limit: 2 s   Memory limit: 256 MB

## Description

A datacenter contains **n** server racks, numbered 1 to **n**. A single, non-redundant network topology links them all: there are exactly **n − 1** fiber conduits, and data can travel between any two racks via exactly one sequence of conduits. Each conduit has a specific activation cost.

A client has leased a specific subset of **t** racks. You must activate a set of conduits so that all leased racks can communicate with each other, either directly or by routing through unleased racks. Unleased racks on the active routes will act as pass-through switches.

Determine the minimum total activation cost required to connect all of the client's leased racks.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers representing the identifiers of the leased racks.
Each of the following **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating a fiber conduit between rack **u** and rack **v** with an activation cost of **w**.

## Output

Print a single integer representing the minimum total activation cost to connect all leased racks.

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
