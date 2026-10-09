# Problem A — Bridging the Core Endpoints

Time limit: 5 s   Memory limit: 256 MB

## Description

A system contains **n** endpoints (numbered 1..n). Certain pairs of endpoints can be bridged by a bidirectional link at a given cost. Among the endpoints, **t** are **core** endpoints. You must select a set of links to activate such that, for any pair of core endpoints, it is possible to travel from one to the other using only the activated links. The remaining endpoints do not have this requirement: you may use links attached to them to form cheaper travel routes between core endpoints, or you may leave them entirely isolated.

Determine the minimum total cost of a set of links that allows travel between all core endpoints.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the core endpoints.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a link bridging endpoints u and v at cost w.
The provided links are guaranteed to be sufficient to allow travel between all core endpoints.

## Output

Print a single integer: the minimum total cost to activate links satisfying the condition.

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

In Example 1, stepping through the non-core endpoint 4 (costs 1+1+1 = 3) is cheaper than bridging the three core endpoints directly (which would cost 4). In Example 3 there is only one core endpoint, so no links need to be activated.
