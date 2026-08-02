# Multi-Channel Signal Allocation

**Time limit:** 2 s  
**Memory limit:** 256 MB

A telemetry system must distribute data streams across three operating frequency bands, identified by the integers 1, 2, and 3. The system processes $n$ distinct streams, numbered 1 to $n$. Every stream must be routed through exactly one frequency band.

Certain streams generate inter-channel noise when placed on the same band. You are given $m$ specific pairs of mutually interfering streams that must be assigned to different frequency bands.

Determine if an interference-free routing exists. If such a configuration is possible, find the configuration that minimizes the sequence of assigned bands $s_1, s_2, \dots, s_n$ lexicographically (prioritizing the lowest possible band index for stream 1, then stream 2, through stream $n$).

## Input

The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), where $n$ is the number of data streams (bounded by the system's hardware limit of 40 concurrent channels) and $m$ is the number of interference constraints (which cannot exceed the total number of unordered stream pairs).

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that stream $u$ and stream $v$ cannot share the same frequency band.

## Output

If no valid frequency allocation exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where $s_i \in \{1, 2, 3\}$), representing the frequency band assigned to stream $i$, such that $s_1, s_2, \dots, s_n$ is lexicographically as small as possible.

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
