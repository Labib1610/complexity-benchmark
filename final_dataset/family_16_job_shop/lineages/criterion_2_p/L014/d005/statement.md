# Problem B — Drone Track Routing

Time limit: 1 s
Memory limit: 256 MB

## Description

You are designing a flight track that must visit $j$ distinct checkpoints exactly once. You must choose a single sequence in which all the checkpoints are visited.

Two automated drones, the Scout and the Hauler, will traverse your track. 
- The Scout drone starts at time 0 and visits the checkpoints in your chosen sequence. At each checkpoint, the Scout performs an inspection. For a checkpoint given in the input with parameters **p1** and **p2**, the Scout's inspection takes exactly **p1** microseconds. Travel time between checkpoints is instantaneous (0 microseconds), so the Scout continuously moves to the next checkpoint and begins its inspection as soon as the current one finishes.
- The Hauler drone follows the Scout along the exact same sequence of checkpoints. At each checkpoint, the Hauler performs an extraction that takes exactly **p2** microseconds. The Hauler's operation is strictly constrained: it can only begin its extraction at a checkpoint after the Scout has completely finished its inspection at that same checkpoint. Additionally, the Hauler can only perform one extraction at a time, meaning it cannot begin extraction at the next checkpoint in the sequence until it has finished its extraction at the current one. If the Hauler finishes an extraction but the Scout is still inspecting the next checkpoint, the Hauler must wait. Travel time for the Hauler is also instantaneous.

Your objective is to determine the optimal sequence of checkpoints that minimizes the time at which the Hauler completely finishes its extraction at the final checkpoint in the sequence. Report this minimum possible completion time.

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

In Example 2, there is only one checkpoint. The Scout drone begins at time 0 and finishes its inspection at time 5. The Hauler drone immediately begins its extraction and finishes at time 5 + 3 = 8.