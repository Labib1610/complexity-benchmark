# Problem B — Drone Track Routing

Time limit: 1 s
Memory limit: 256 MB

## Description

You are designing a flight track that must visit $j$ distinct checkpoints exactly once. You must choose a single sequence in which all the checkpoints are visited.

Two automated drones, the Scout and the Hauler, will traverse your track. Both drones must visit the checkpoints in the exact same single sequence chosen by you.
- The Scout drone performs an inspection at each checkpoint. For a checkpoint given in the input with parameters **p1** and **p2**, the Scout's inspection takes exactly **p1** microseconds. 
- The Hauler drone follows the Scout and performs an extraction taking exactly **p2** microseconds at each checkpoint.

Because the Hauler can only extract after the Scout has inspected, and neither drone can skip ahead, the total time for both drones to finish the sequence is dictated by a critical point. Specifically, for any position $k$ (where $1 \le k \le j$) in your chosen sequence, we calculate a synchronization time by summing the Scout's inspection times for the 1st through the $k$-th checkpoints in your chosen sequence, and adding the Hauler's extraction times for the $k$-th through the $j$-th checkpoints in your chosen sequence. 

The actual time at which the Hauler completely finishes its extraction at the final checkpoint is exactly equal to the maximum of these synchronization times over all $j$ possible choices of $k$.

Your objective is to determine the optimal single sequence of checkpoints that minimizes this final completion time. Report this minimum possible completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000) representing a checkpoint. **p1** is the time required for the Scout's inspection, and **p2** is the time required for the Hauler's extraction.

## Output

Print a single integer: the minimum possible time at which the Hauler finishes its final extraction.

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

In Example 2, there is only one checkpoint, so $j=1$. The chosen sequence has only this checkpoint. The only possible position for the critical point $k$ is 1. The calculated time is the Scout's time for the 1st checkpoint (5) plus the Hauler's time for the 1st checkpoint (3). The maximum over all possible $k$ is 5 + 3 = 8.