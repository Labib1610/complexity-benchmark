# Spectrum Allocation for Sensor Nodes

Time limit: 2 s   Memory limit: 256 MB

A wireless telemetry network consists of $n$ sensor nodes numbered $1$ through $n$. To minimize signal degradation, each node must be assigned to work on one of three available frequency bands: Band 1, Band 2, or Band 3.

Certain pairs of nodes are located close to each other, creating mutual interference. There are $m$ such interfering pairs. Two nodes that form an interfering pair cannot be assigned to the same frequency band.

To comply with regulatory standards, any valid allocation must satisfy the following Global Thermal Bounds:
1. For every subset of $k$ nodes ($1 \le k \le n$), the sum of their assigned band numbers cannot exceed $3k$.
2. The average band number across all $n$ nodes must lie within the range $[1.0, 3.0]$.

Your task is to determine if a valid band assignment exists for all $n$ nodes. If multiple valid assignments exist, select the one that yields the lexicographically smallest sequence of band numbers $(s_1, s_2, \dots, s_n)$ where $s_i \in \{1, 2, 3\}$ is the band assigned to node $i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of sensor nodes and the number of interfering pairs, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$) indicating that node $u$ and node $v$ interfere with each other.

## Output
If no valid assignment exists, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$) representing the lexicographically smallest sequence of assigned bands.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
