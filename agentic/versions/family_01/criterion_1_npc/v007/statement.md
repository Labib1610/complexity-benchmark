# Problem A — Trichrome Shifts

Time limit: 2 s   Memory limit: 256 MB

A factory operates three shifts labeled 1, 2, 3. There are $n$ workers. Certain pairs of workers are in conflict and cannot be scheduled on the same shift.

You must assign every worker $i$ to exactly one shift $s_i \in \{1, 2, 3\}$ such that:
- No two workers in conflict share the same shift.
- The shift assignment satisfies the global capacity constraint: $n \le \sum_{i=1}^n s_i \le 3n$.

If no valid assignment exists, report that it is impossible. Otherwise, output the assignment that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ — the number of workers and the number of conflict pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the next $m$ lines contains two integers $u$ $v$ — a conflicting pair.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise print `YES` on the first line. On the second line print $n$ integers $s_1\ s_2\ \dots\ s_n$ (each in \{1, 2, 3\}), where $s_i$ is the shift of worker $i$. Among all valid assignments output the lexicographically smallest sequence (compare $s_1$ first, then $s_2$, and so on).

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
