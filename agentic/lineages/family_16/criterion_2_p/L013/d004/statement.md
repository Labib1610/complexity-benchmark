# Energy Node Calibration

Time limit: 1 s   Memory limit: 256 MB

## Description

You are configuring a linear array of **j** energy nodes. You must choose a single sequence in which to arrange these nodes from position 1 to position $j$.

Each node has two properties: a *charging duration* (**p1**) and a *discharging duration* (**p2**).
Once you fix the sequence $S = (S_1, S_2, \dots, S_j)$, the system's *peak stress* is determined by evaluating the nodes sequentially from the first to the last. 

We maintain a running stress tracker, $E$, which starts at $0$.
Additionally, we maintain the running sum of charging durations, $C$, which also starts at $0$.

For each node in your sequence, in order:
1. Add the node's charging duration (**p1**) to $C$.
2. Update the stress tracker $E$ by setting it to the larger of its current value and the new value of $C$.
3. Add the node's discharging duration (**p2**) to $E$.

After all $j$ nodes have been processed, the final value of $E$ is the peak stress of the sequence.

Your objective is to find an arrangement sequence that minimizes the final peak stress $E$. Output this minimum possible peak stress.

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

In Example 2, there is only one node. The sequence is fixed to just this node.
Initially, $C = 0$ and $E = 0$.
For the single node (5 3):
1. Its charging duration (5) is added to $C$, making $C = 5$.
2. $E$ is updated to the maximum of its current value (0) and $C$ (5), so $E$ becomes 5.
3. Its discharging duration (3) is added to $E$, making $E = 8$.
After processing, the final peak stress is 8.