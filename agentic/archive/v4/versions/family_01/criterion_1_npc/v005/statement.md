# Shift Assignment with Incompatibilities

Time limit: 2 s   Memory limit: 256 MB

A facility operates across three distinct time slots, identified as 1, 2, and 3. There are $n$ workers who must each be assigned to a single time slot. Certain pairs of workers are incompatible and cannot be assigned to the same time slot. Determine whether it is possible to assign every worker to a time slot such that no incompatible pair shares a slot, and if so, find the valid assignment.

## Input
The first line contains two integers $n$ and $m$.
* The headcount $n$ satisfies $1 \le n \le 40$, bounded by the facility's single-shift room capacity.
* The number of incompatible pairs $m$ ranges from $0$ up to the total number of distinct two-worker combinations, $\frac{n(n-1)}{2}$.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that worker $u$ and worker $v$ are incompatible.

## Output
If no valid shift assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), where $s_i$ is the time slot assigned to worker $i$. If multiple valid assignments exist, output the lexicographically smallest sequence (compare $s_1$ first, then $s_2$, and so on).

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
