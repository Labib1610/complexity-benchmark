# Server Queue Calibration

Time limit: 1 s   Memory limit: 256 MB

## Description

You are configuring a sequential processing queue for **j** data packets. You must choose a single sequence in which to order these packets from position 1 to $j$.

Each packet has two properties: an *arrival delay* (**p1**) and a *processing duration* (**p2**).
The packets arrive at a single processing unit one by one. The unit can process only one packet at a time, and it processes waiting packets in the exact order they arrived.

The exact arrival time of each packet is determined by its position in your chosen sequence:
- The packet you place first arrives at a time equal to its own arrival delay (**p1**).
- Each subsequent packet arrives exactly **p1** seconds after the arrival of the packet immediately preceding it in the sequence. (Thus, a packet's arrival time is the sum of the arrival delays of all packets up to and including itself).

When a packet arrives, its processing begins immediately if the processing unit is idle. If the unit is currently busy processing a previous packet, the newly arrived packet waits in a queue, and its processing begins at the exact moment the unit finishes the previous packet.
Once processing begins on a packet, it takes exactly its processing duration (**p2**) in seconds to complete.

Your objective is to find an arrangement sequence of the **j** packets that minimizes the exact time when the final (the $j$-th) packet finishes processing. Output this minimum possible completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the arrival delay and the processing duration of a packet, respectively.

## Output

Print a single integer: the minimum possible completion time of the final packet.

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
- The first packet (1 3) arrives at time 1. The unit is idle, so it starts processing at time 1 and finishes at 1 + 3 = 4.
- The second packet (2 4) arrives exactly 2 seconds after the first packet, at time 1 + 2 = 3. The unit is busy until time 4. It starts processing this packet at time 4, and finishes at 4 + 4 = 8.
- The third packet (3 2) arrives exactly 3 seconds after the second packet, at time 3 + 3 = 6. The unit is busy until time 8. It starts processing at time 8, and finishes at 8 + 2 = 10.
The final packet finishes processing at time 10, which is the minimum possible completion time.