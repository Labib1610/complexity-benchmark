# Problem A — Temporal Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

At a chronophysics facility, researchers are working with **n** temporal anchors (labeled 1 to **n**). The facility's reactor can activate any of **m** possible bidirectional stabilization links. Each stabilization link binds a specific pair of anchors, ensuring they drift at the exact same rate. Activating a given link requires a known one-time expenditure of chroniton particles.

Because drifting is a transitive property, if anchor $X$ is bound to $Y$, and $Y$ is bound to $Z$, then $X$, $Y$, and $Z$ all drift at the same rate and exist within a single unified temporal frame. 

Within the set of **n** anchors, exactly **t** have been identified as primary anchors. The remaining **n** − **t** anchors are auxiliary; they have no intrinsic value, but they can be bound to other anchors if it proves useful.

Your task is to determine the absolute minimum total chroniton expenditure required to activate a subset of stabilization links such that every one of the **t** primary anchors shares the exact same unified temporal frame.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the labels of the primary anchors.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a stabilization link that can bind anchor u and anchor v at the cost of w chroniton particles.
It is guaranteed that the available links are sufficient to place all primary anchors in the same temporal frame.

## Output

Print a single integer: the minimum total chroniton expenditure to ensure all primary anchors share a unified temporal frame.

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

In Example 1, binding the primary anchors through the auxiliary anchor 4 requires activating three links (costing 1+1+1 = 3), which is more efficient than binding the three primary anchors directly to one another (which would cost 4). In Example 3, there is only one primary anchor, so no stabilization links need to be activated.
