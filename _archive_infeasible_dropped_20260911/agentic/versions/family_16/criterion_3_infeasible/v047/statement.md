# Delay Justification

Time limit: 2 s   Memory limit: 256 MB

## Description

A video rendering studio must process **j** scenes. Each scene must first be rendered on the GPU cluster, and then encoded on the CPU cluster. The GPU cluster can only render one scene at a time, and the CPU cluster can only encode one scene at a time. A scene cannot begin encoding until its rendering is fully complete.

The client requires all scenes to be completely finished within **T** minutes. You are given the rendering time and encoding time for each scene.

The project manager has determined that this deadline cannot be met under any sequence of scenes. To justify the delay to the client, you must provide a certificate of impossibility. The input data guarantees that exactly one of the following reasons applies. Print the applicable reason:

- `JOB i` — A single scene takes too long: scene **i** (1-based index) has a combined rendering and encoding time strictly greater than **T**.
- `LOAD c` — A cluster is overloaded: the sum of all processing times on cluster **c** exceeds **T**. Use **c** = 1 for the GPU cluster and **c** = 2 for the CPU cluster.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the rendering time on the GPU cluster and the encoding time on the CPU cluster for that scene.

## Output

Print a single line containing either `JOB i` or `LOAD c` as described above.

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```
