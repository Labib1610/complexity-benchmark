# Problem A — Workforce Pipeline: Shift Assignment Stage

Time limit: 2 s   Memory limit: 256 MB

An automated workforce management system processes personnel scheduling through a multi-stage pipeline: conflict mapping (Stage 1), shift allocation (Stage 2), and roster publishing (Stage 3). Stage 1 has concluded, establishing a list of $n$ workers and $m$ conflict pairs between workers who cannot share a shift.

Your task is to execute **Stage 2: Shift Allocation**. You must assign each worker to exactly one of three available operational shifts (labeled 1, 2, and 3) such that no conflicting pair shares a shift. If multiple valid shift assignments exist, the system requires selecting the one that produces the lexicographically smallest sequence of shift numbers, ensuring deterministic input for Stage 3 publishing.

## Input
The first line contains two integers $n$ and $m$ — the number of workers and the number of conflict pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$) denoting a conflicting pair of workers.

## Output
If no valid shift allocation exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each $s_i \in \{1, 2, 3\}$), where $s_i$ is the shift assigned to worker $i$. Output the lexicographically smallest sequence among all valid assignments.

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
