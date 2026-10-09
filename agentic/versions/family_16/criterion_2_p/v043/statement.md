# Problem B — Data Pipeline Optimization

Time limit: 1 s   Memory limit: 256 MB

## Description

A secure server must process $j$ incoming data packets. Every packet requires sequential processing through exactly two cryptographic modules: first it must pass through the Decryptor, and immediately afterward it must pass through the Analyzer. For each packet, you are given the exact duration it takes to be processed in the Decryptor and the duration it takes in the Analyzer.

The server operates under the following hardware constraints:
- The Decryptor can only process a single packet at a time.
- The Analyzer can only process a single packet at a time.
- A packet becomes available to the Analyzer only at the instant it finishes its time in the Decryptor.
- You must dictate a single, strict processing sequence for the packets. Both the Decryptor and the Analyzer will handle the packets in this exact same order. 
- The Analyzer will process available packets as soon as it is free. If the Analyzer finishes a packet and is ready for the next one in your sequence, but the Decryptor is still working on that next packet, the Analyzer must remain idle until the packet is handed over.

Your task is to determine the single processing arrangement—out of all $j!$ possibilities—that allows the Analyzer to complete the final packet as early as possible. Report this minimum overall completion time.

## Input

The first line contains a single integer $j$ ($1 \le j \le 200000$).
Each of the next $j$ lines contains two integers $t_D$ and $t_A$ ($1 \le t_D, t_A \le 1000000$), representing the time required for the packet in the Decryptor and the Analyzer, respectively.

## Output

Print a single integer: the earliest possible time at which all packets have completed both modules.

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

In Example 2, the single packet takes 5 time units in the Decryptor and then 3 time units in the Analyzer, finishing at time 8.
