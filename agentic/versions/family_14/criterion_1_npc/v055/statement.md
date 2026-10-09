# Problem A — Harmonic Convergence

Time limit: 5 s   Memory limit: 256 MB

## Description

An artificer is calibrating a resonant array consisting of **n** crystal mounts, numbered 1 to **n**. Certain pairs of mounts can be linked using a tuning conduit. The artificer has a blueprint of **m** possible conduit placements, where each conduit requires a specific amount of silver dust to construct. 

Synchronization propagates continuously through any sequence of installed conduits. Therefore, a group of mounts will operate at the exact same frequency if they are connected into a single contiguous network. 

The array contains **t** primary crystals that must operate at the same frequency to function properly. The remaining mounts hold relay crystals, which do not strictly need to be synchronized with the primary crystals. However, the artificer may choose to route conduits through any number of relay mounts if doing so uses less total silver dust than linking the primary mounts directly.

Determine the minimum total amount of silver dust required to construct a set of conduits that synchronizes all primary crystals.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the mounts holding the primary crystals.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a conduit can be constructed between mount **u** and mount **v** using **w** units of silver dust.
It is guaranteed that it is possible to synchronize all primary crystals using some combination of the available conduits.

## Output

Print a single integer: the minimum total silver dust required.

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

In Example 1, synchronizing the primary crystals 1, 2, and 3 by linking each of them to the relay crystal 4 requires 1 + 1 + 1 = 3 units of silver dust. This uses less dust than linking the primary crystals directly with each other (which would cost at least 4 units). In Example 3, there is only 1 primary crystal, so it already operates at its own frequency without any conduits, costing 0.
