# Problem B — Render Pipeline Bottleneck

Time limit: 1 s   Memory limit: 256 MB

## Description

A distributed rendering pipeline is divided into four sequential stages to generate final animation frames:
- **Stage A**: Asset fetching (completed prior to your involvement).
- **Stage B**: Geometry processing.
- **Stage C**: Ray-tracing.
- **Stage D**: Compositing and encoding.

Your module is responsible only for scheduling Stage B and Stage C for a batch of **j** independent 3D scenes. The hardware constraints are as follows:
- The geometry processor (Stage B) can only compute one scene at a time.
- The ray-tracing engine (Stage C) can also only compute one scene at a time.
- A scene can only begin Stage C after its Stage B computation is completely finished.
- The memory buffer transferring data from Stage B to Stage C operates strictly as a First-In-First-Out (FIFO) queue. Consequently, the scenes must be processed in Stage C in the exact same sequence they were processed in Stage B.

You must determine the optimal sequence of scenes to feed into Stage B. Your goal is to minimize the time at which the final scene completes Stage C, because Stage D cannot begin until the entire batch of scenes is ray-traced.

Assuming Stage B begins processing the first scene at time 0, find the earliest possible time that Stage D can commence.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **t_B** and **t_C** (1 ≤ t_B, t_C ≤ 1000000): the time required to process a scene in Stage B and Stage C, respectively.

## Output

Print a single integer: the earliest possible time Stage D can begin.

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

In Example 2, the single scene takes 5 in Stage B and then 3 in Stage C, finishing at time 8.
