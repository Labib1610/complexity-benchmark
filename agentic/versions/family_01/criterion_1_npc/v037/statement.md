# Problem A — Trichrome Shifts

Time limit: 2 s   Memory limit: 256 MB

A factory runs three shifts labeled 1, 2, 3. There are $n$ workers. Some pairs of workers are in conflict and must not be placed on the same shift. Assign every worker to exactly one of the three shifts so that no conflicting pair shares a shift, or report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ — the number of workers and the number of conflict pairs. The workforce size $n$ is at least 1 and cannot exceed the total number of hours in a standard 40-hour workweek ($1 \le n \le 40$). The count of conflict pairs $m$ is non-negative and cannot exceed the total number of distinct unordered pairs formed from $n$ workers ($0 \le m \le n(n-1)/2$).

Each of the next $m$ lines contains two integers $u$ $v$ ($1 \le u, v \le n$, $u \neq v$) — a conflicting pair.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise print `YES` on the first line. On the second line print $n$ integers $s_1\ s_2\ \dots\ s_n$ (each in $\{1,2,3\}$), where $s_i$ is the shift of worker $i$. Among all valid assignments output the lexicographically smallest sequence (compare $s_1$ first, then $s_2$, and so on).

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
