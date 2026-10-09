# Problem A — Harmonic Convergence

Time limit: 5 s   Memory limit: 256 MB

## Description

You are analyzing a system of $n$ distinct frequencies (numbered 1 to $n$). Within this system, a specific subset of $t$ frequencies are designated as *anchors*. Your objective is to unify all anchor frequencies into a single synchronized cluster.

Initially, each frequency operates in its own independent cluster. You are given a list of $m$ available synchronization operations. Each operation specifies two frequencies, $u$ and $v$, and an energy cost $w$. If you choose to execute an operation, the entire cluster containing $u$ and the entire cluster containing $v$ are permanently merged into a single, combined cluster. 

You may select any subset of the available operations to execute. The total energy cost is the sum of the costs $w$ of the operations you choose. You can merge clusters that contain non-anchor frequencies if doing so helps achieve your goal for a lower total energy cost.

Determine the minimum total energy cost required to reach a state where all $t$ anchor frequencies belong to the same cluster.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le 10$, $1 \le n \le 100$, $0 \le m \le n(n-1)/2$).
The second line contains $t$ distinct integers: the ids of the anchor frequencies.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$): an available operation that merges the clusters containing frequency $u$ and frequency $v$ for an energy cost of $w$.
The provided operations are sufficient to place all anchor frequencies into the same cluster.

## Output

Print a single integer: the minimum total energy cost to unify all anchor frequencies.

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

In Example 1, executing the operations to merge frequencies 1, 2, and 3 with frequency 4 costs 1+1+1 = 3. This places all three anchor frequencies (1, 2, and 3) into the same cluster as frequency 4, which is cheaper than merging the anchor frequencies directly with each other (which would cost 4). In Example 3, there is only one anchor frequency, which inherently exists in its own cluster, requiring no operations.
