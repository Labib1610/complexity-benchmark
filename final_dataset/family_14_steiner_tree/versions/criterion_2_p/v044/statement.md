# Optimal Channel Configuration

Time limit: 2 s
Memory limit: 256 MB

## Description

Given a system of $n$ endpoints and $m$ potential bidirectional channels, you must assign a state $x_i \in \{0, 1\}$ to each channel $i$. Setting $x_i = 1$ establishes the channel and incurs a cost $w_i$, while $x_i = 0$ leaves it unestablished at zero cost.

Your objective is to minimize the cost function $C(x) = \sum_{i=1}^m w_i x_i$ subject to a global connectivity constraint. 

A specific subset of $t$ endpoints are designated as essential. An assignment of states is considered valid if and only if all essential endpoints are in the same connected component (i.e., for any pair of essential endpoints, there exists at least one path between them consisting entirely of channels with $x_i = 1$). Non-essential endpoints may be freely used to route these paths.

Since each of the $m$ channels can be independently established or ignored, the search space consists of $2^m$ possible state assignments. The initial layout of the $m$ potential channels guarantees that $m = n - 1$ and that there is exactly one sequence of channels linking any two endpoints.

Find the minimum value of $C(x)$ among all valid assignments.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers representing the identifiers of the essential endpoints.
Each of the following **m** lines describes a potential channel with three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), meaning there is a channel between endpoint u and endpoint v with cost w. The channels follow the layout guarantees described above.

## Output

Print a single integer: the minimum total cost $C(x)$ of a valid assignment.

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

In Example 1, the essential endpoints 1 and 4 can only be connected through endpoints 2 and 3, so the assignment must set $x_i = 1$ for all three channels (yielding $C(x) = 5+1+2 = 8$). In Example 2, there is only one essential endpoint, so setting $x_i = 0$ for all channels satisfies the constraint and yields $C(x) = 0$.
