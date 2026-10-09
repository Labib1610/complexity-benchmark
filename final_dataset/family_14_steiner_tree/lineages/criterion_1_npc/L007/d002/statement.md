# Problem A — Campus Network Integration

Time limit: 5 s   Memory limit: 256 MB

## Description

A campus consists of **n** locations (numbered 1 to n). You are given a set of **t** priority locations that must all be able to communicate with one another. To enable this, you can purchase communication links between specific pairs of locations, each having a known price.

The selected links must form a single connected structure that includes all priority locations. You may incorporate any non-priority locations into this structure if doing so results in a more cost-effective overall design.

Determine the minimum total price of the links that must be purchased to ensure every priority location is linked to the others in this manner.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the priority locations.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a communication link available between locations u and v at price w.
The available links are sufficient to integrate all priority locations.

## Output

Print a single integer: the minimum total price to integrate all priority locations.

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

In Example 1, incorporating location 4 into the connected structure (prices 1+1+1 = 3) is cheaper than joining the three priority locations directly (which would price 4). In Example 3 there is only one priority location, so no links need to be purchased.