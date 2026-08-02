# Research Lab Schedule Synchronization

Time limit: 2 s   Memory limit: 256 MB

A research facility needs to schedule $n$ sensitive experimental setups, numbered $1$ through $n$. The facility operates across three distinct operational blocks labeled $1$, $2$, and $3$. Every experiment must be assigned to exactly one of these three blocks.

Certain pairs of experiments emit electromagnetic interference and cannot be executed within the same operational block. You are given the full list of these conflicting pairs.

Determine whether it is possible to assign every experiment to a block such that no conflicting pair shares a block. If a valid assignment exists, find the sequence of assigned blocks $s_1, s_2, \dots, s_n$ (where $s_i \in \{1, 2, 3\}$ is the block assigned to experiment $i$) that is lexicographically smallest. If no valid assignment exists, report that it is impossible.

## Input
The first line contains two space-separated integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of experiments and the number of interference constraints.

Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that experiment $u$ and experiment $v$ cannot share the same operational block.

## Output
If no valid assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$, representing the block assigned to each experiment from $1$ to $n$. If there are multiple valid assignments, output the one that is lexicographically smallest.

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
