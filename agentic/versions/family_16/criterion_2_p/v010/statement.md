# Problem B — Signal Pipeline

Time limit: 1 s   Memory limit: 256 MB

## Description

A communication array receives **j** distinct transmissions. Every transmission must go through a two-step pipeline: it must be decrypted, and subsequently analyzed. For each transmission, you are given the duration it takes to decrypt and the duration it takes to analyze. The pipeline operates under the following constraints:

- There is exactly one decryption module and exactly one analysis module. A module can handle at most one transmission at any given moment.
- A transmission's analysis cannot begin until its decryption is entirely complete.
- You must establish a single sequence for all transmissions. Both the decryption module and the analysis module will process the transmissions in this exact sequence.

Determine the sequence that minimizes the total duration from the start of the very first decryption until the completion of the final transmission's analysis. Output this minimum total duration.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the duration required to decrypt and the duration required to analyze the transmission, respectively.

## Output

Print a single integer representing the earliest possible time the final transmission's analysis can be completed.

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

In Example 2, the single transmission takes 5 units of time to decrypt and then 3 units of time to analyze, finishing at time 8.
