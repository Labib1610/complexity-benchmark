# Problem B — Relay Transmission Protocol

Time limit: 1 s   Memory limit: 256 MB

## Description

You are coordinating the transfer of **j** data packets through a central network relay. The transfer of every packet consists of a continuous upload phase followed by a continuous download phase. For each packet, you are provided the exact duration it takes to upload, and the exact duration it takes to download.

The transfer protocol enforces the following rules:
- You must establish a single, strict sequence for the packets. Both the upload channel and the download channel will handle the packets in this exact sequence.
- The upload channel executes the first phase for all packets, and the download channel executes the second phase. A channel can never handle more than one packet simultaneously.
- The download phase for any specific packet cannot commence until its upload phase has fully concluded.
- Neither channel will artificially delay its operation: each channel begins processing the next packet in the sequence as soon as both the channel is free and the packet is ready for that channel.
- The upload of the first packet in your sequence begins at time 0.

Your objective is to determine a sequence that minimizes the total time required. Calculate and output the earliest possible moment when the final packet in your sequence entirely completes its download phase.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the subsequent **j** lines provides two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the duration required to upload and the duration required to download the respective packet.

## Output

Print a single integer: the earliest possible time at which the final packet finishes downloading.

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

In Example 2, the single packet requires 5 time units to upload and then 3 time units to download, finishing the entire transfer at time 8.
