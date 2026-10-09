# Energy Node Calibration

Time limit: 1 s   Memory limit: 256 MB

## Description

You are configuring a linear array of **j** energy nodes. You must choose a single sequence in which to arrange these nodes from position 1 to position $j$.

Each node has two properties: a *charging duration* and a *discharging duration*.
Once you fix the sequence $S = (S_1, S_2, \dots, S_j)$, the system's *peak stress* is determined by a pivot index $k$ ($1 \le k \le j$). The stress at a specific pivot index $k$ is calculated as the sum of the charging durations of all nodes from position 1 up to $k$, plus the sum of the discharging durations of all nodes from position $k$ up to $j$. 

Formally, if $p1_{S_i}$ is the charging duration of the node at position $i$ and $p2_{S_i}$ is its discharging duration, the peak stress of the sequence $S$ is given by the exact formula:
$$F(S) = \max_{1 \le k \le j} \left( \sum_{i=1}^{k} p1_{S_i} + \sum_{i=k}^{j} p2_{S_i} \right)$$

Note that the node at the pivot index $k$ is included in both sums: its charging duration contributes to the first sum, and its discharging duration contributes to the second sum. For example, if $k=2$, the calculation uses the charging durations of the nodes at positions 1 and 2, and the discharging durations of the nodes at positions 2 through $j$.

Your objective is to find an arrangement sequence $S$ that minimizes the peak stress $F(S)$. Output this minimum possible peak stress.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the charging duration and the discharging duration of a node, respectively.

## Output

Print a single integer: the minimum possible peak stress.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2, there is only one node. The sequence is fixed, and the only valid pivot index is $k=1$. The stress is the charging duration (5) plus the discharging duration (3), giving a peak stress of 8.