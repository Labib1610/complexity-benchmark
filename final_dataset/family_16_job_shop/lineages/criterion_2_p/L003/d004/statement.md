# Problem B — Factory Processing

Time limit: 1 s   Memory limit: 256 MB

## Description

A factory must process a batch of **j** custom parts. You must arrange the parts into a single production sequence.

The processing requires two stages, handled by the Milling Machine and the Polishing Machine:
- The Milling Machine shapes the parts one by one in your chosen sequence. It starts the first part at time 0 and operates continuously, so each subsequent part begins the instant the previous one finishes.
- Once a part finishes on the Milling Machine, it is immediately placed in the Polishing Machine's waiting queue.
- The Polishing Machine finishes the parts one by one. Because it takes them from the queue in the order they arrive, it processes them in the exact same sequence you chose.
- The Polishing Machine starts working on a part as soon as it is in the queue, provided the machine is not already busy with a previous part. If a part is ready and the machine is free, it never sits idle.

For each part, you are given the time **p1** it requires on the Milling Machine, and the time **p2** it requires on the Polishing Machine.

Determine the optimal sequence of parts to minimize the time at which the Polishing Machine completes the final part. Output this minimum possible time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the processing times required for a part on the Milling Machine and the Polishing Machine, respectively.

## Output

Print a single integer: the smallest possible time at which the final part completes its polishing.

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

In Example 2, the single part takes 5 on the Milling Machine and 3 on the Polishing Machine, finishing its polishing at time 8.