# Problem A — Campus Network Integration

Time limit: 5 s   Memory limit: 256 MB

## Description

A campus operates **n** wireless access points (numbered 1 to n). You are given a set of **t** priority access points that must all be configured to operate on the exact same broadcast channel. To achieve this, you can purchase channel-bridging modules for specific pairs of access points, each having a known installation price.

When a purchased module bridges two access points, it forces them to use the same channel. Because this requirement is transitive, any collection of access points that are bridged together—whether directly or indirectly through intermediate access points—will all share a common channel. You may bridge any non-priority access points into this configuration if doing so results in a more cost-effective overall design.

Determine the minimum total price of the modules that must be purchased to ensure every priority access point shares the same broadcast channel.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the priority access points.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a channel-bridging module available between access points u and v at price w.
The available modules are sufficient to synchronize all priority access points.

## Output

Print a single integer: the minimum total price of the modules to ensure all priority access points share the same channel.

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

In Example 1, bridging access point 4 with each of 1, 2, and 3 (prices 1+1+1 = 3) forces all four to share the same channel, which is cheaper than bridging the three priority access points directly (which would price 4). In Example 3 there is only one priority access point, so no modules need to be purchased.