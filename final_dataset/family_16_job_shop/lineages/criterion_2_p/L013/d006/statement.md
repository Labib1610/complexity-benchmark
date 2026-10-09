# Server Queue Calibration

Time limit: 1 s   Memory limit: 256 MB

## Description

You are configuring a sequential processing queue for **j** data packets. You must choose a single sequence in which to order these packets from position 1 to $j$.

Each packet has two properties: a *synchronization cost* (**p1**) and an *update cost* (**p2**).

When you deploy a specific sequence of packets, the server evaluates the queue's worst-case latency by calculating the impact of a hypothetical "context switch" at every possible packet position. 

Specifically, if the context switch occurs at packet position $k$ (where $1 \le k \le j$), the latency for that specific switch is the sum of:
- The synchronization costs (**p1**) of all packets from position 1 up to and including position $k$.
- The update costs (**p2**) of all packets from position $k$ up to and including position $j$.

The *overall calibration time* of your chosen sequence is defined as the **maximum** latency calculated across all $j$ possible context switch positions.

Your objective is to find an arrangement sequence of the **j** packets that minimizes this overall calibration time. Output this minimum possible overall calibration time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the synchronization cost and the update cost of a packet, respectively.

## Output

Print a single integer: the minimum possible overall calibration time of the sequence.

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

In Example 1, an optimal sequence is to order the packets as: (1 3), then (2 4), then (3 2).
If the context switch is at position 1:
- Synchronization costs: packet 1 (1). Sum = 1.
- Update costs: packets 1, 2, 3 (3 + 4 + 2). Sum = 9.
- Latency = 1 + 9 = 10.

If the context switch is at position 2:
- Synchronization costs: packets 1, 2 (1 + 2). Sum = 3.
- Update costs: packets 2, 3 (4 + 2). Sum = 6.
- Latency = 3 + 6 = 9.

If the context switch is at position 3:
- Synchronization costs: packets 1, 2, 3 (1 + 2 + 3). Sum = 6.
- Update costs: packet 3 (2). Sum = 2.
- Latency = 6 + 2 = 8.

The maximum latency among all switch positions is 10. Thus, the overall calibration time is 10, which is the minimum possible.