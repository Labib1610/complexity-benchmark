# Shift Assignment Harmony

Time limit: 2 s   Memory limit: 256 MB

A specialized assembly plant operates across three structured daily shifts, labeled 1, 2, and 3. There are $n$ workers available. To ensure optimal workflow, certain pairs of workers who share equipment or space are flagged as incompatible and must not be scheduled on the exact same shift.

Because team assignments follow a standardized setup, you need to assign every worker to exactly one of the three shifts such that no incompatible pair works together, or determine if no valid roster can be formed.

## Input
The first line contains two integers $n$ and $m$ — the number of workers and the number of incompatible pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).  
Each of the next $m$ lines contains two integers $u$ and $v$ — indicating that worker $u$ and worker $v$ are incompatible.

## Output
If no valid shift assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the shift assigned to worker $i$. If multiple valid assignments exist, output the lexicographically smallest sequence (comparing $s_1$ first, then $s_2$, and so on).

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
