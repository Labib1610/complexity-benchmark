# Problem C — Shift Assignment Analysis

Time limit: 2 s
Memory limit: 256 MB

You are analyzing a proposed schedule for $n$ workers across 2 available shifts. You are provided with a list of $m$ restricted pairs of workers. If a pair of workers is on this list, they cannot be assigned to the same shift due to safety regulations.

Your task is to identify a specific group of exactly three workers, $a$, $b$, and $c$ (with $a < b < c$), that logically cannot be distributed across the 2 shifts without violating the regulations. To demonstrate this, the chosen group must satisfy all of the following conditions:
- The pair consisting of worker $a$ and worker $b$ appears in the restricted list.
- The pair consisting of worker $b$ and worker $c$ appears in the restricted list.
- The pair consisting of worker $a$ and worker $c$ appears in the restricted list.

### Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$, representing a restricted pair of workers.
It is guaranteed that the provided data contains at least one group of three workers satisfying the conditions above.

### Output
Print three integers $a$, $b$, and $c$ on a single line, representing the identified workers, ordered such that $a < b < c$. If there are multiple valid groups of three workers, output the one that is lexicographically smallest (i.e., minimize $a$; in case of a tie, minimize $b$; if still tied, minimize $c$).

### Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

### Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
