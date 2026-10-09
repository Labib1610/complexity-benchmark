# Priority Site Connectivity

Time limit: 2 s   Memory limit: 256 MB

## Description

A facility network consists of **n** stations (numbered 1..n). Certain pairs of stations can be linked by building a conduit, which incurs a specific cost. A subset of **t** stations are marked as **essential**. Your objective is to select a set of conduits to build so that every essential station can communicate with every other essential station, possibly relaying through intermediate stations.

The given candidate conduits provide a fully integrated blueprint: using all candidate conduits, it is possible to travel between any two stations, and there are exactly **n − 1** candidate conduits in total.

Determine the minimum total cost of the conduits you must build to ensure all essential stations are linked together.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line provides **t** distinct integers: the identifiers of the essential stations.
The following **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing a candidate conduit between station u and station v with a building cost of w. The candidate conduits follow the blueprint described above.

## Output

Print a single integer representing the minimum total building cost required to link all essential stations.

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

In Example 1 the essential stations 1 and 4 are joined only through 2 and 3, so all three conduits (5+1+2 = 8) are needed. In Example 2 there is one essential station, so no conduits are needed.