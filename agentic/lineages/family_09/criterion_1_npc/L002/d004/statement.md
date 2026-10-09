# Problem A — Resonant Metrics

Time limit: 5 s   Memory limit: 256 MB

## Description

You are configuring an experimental particle trap containing **n** distinct magnetic nodes, identified by integers 1 through **n**. Your objective is to activate exactly **k** of these nodes. The unactivated nodes remain in a passive state.

The trap's containment grid relies on **m** resonant links. Each resonant link couples exactly two specific nodes. The state of the system is evaluated using two global metrics based on these links. 

For any given link coupling node **u** and node **v**, let $S_u$ be 1 if node **u** is activated, and 0 if it is passive. Similarly, let $S_v$ be 1 if node **v** is activated, and 0 if it is passive. The *activation sum* for this link is the integer value $(S_u + S_v)$.

The two global metrics are calculated by summing values over all **m** links:
1. The **Kinetic Metric** is the sum over all links of the value $3^{(S_u + S_v)} - 1$.
2. The **Potential Metric** is the sum over all links of the value $2 \times (S_u + S_v)$.

To maintain equilibrium, the system requires the Kinetic Metric to be exactly equal to the Potential Metric. If they are not equal, the trap will destabilize and fail.

You must determine whether it is possible to select exactly **k** nodes to activate such that the system maintains equilibrium.

Given the layout of the resonant links, find a valid set of **k** activated nodes, or determine that no such set exists.

## Input

The first line provides three integers: **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
The following **m** lines each contain two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a resonant link that couples node **u** and node **v**. No two resonant links couple the exact same pair of nodes.

## Output

If it is possible to safely activate exactly **k** nodes, output `YES` on the first line. On the second line, output the **k** distinct node identifiers that should be activated, separated by spaces. If multiple valid configurations exist, any one is acceptable.

If no safe configuration of exactly **k** nodes is possible, output `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```