# Shift Assignment Compatibility

Time limit: 2 s   Memory limit: 256 MB

An industrial plant operates across three non-overlapping shifts, designated as 1, 2, and 3. The plant employs $n$ workers, identified by labels from 1 to $n$. Certain pairs of workers are mutually incompatible and cannot be scheduled on the same shift.

Your task is to place every worker into exactly one shift such that no incompatible pair works during the same shift, or to report that no valid schedule can be formed.

## Input

The first line contains two integers $n$ and $m$, representing the total number of workers and the count of conflict pairs. The headcount $n$ reflects the facility's capacity limits ($1 \le n \le 40$). The number of recorded conflicts $m$ ranges from 0 up to the maximum number of unique pairs among all workers ($0 \le m \le n(n-1)/2$).

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that worker $u$ and worker $v$ cannot share a shift. Each unordered pair of workers appears at most once.

## Output

If no valid assignment of workers to shifts exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$, where $s_i \in \{1, 2, 3\}$ specifies the shift assigned to worker $i$. If there are multiple valid schedule configurations, output the one that is lexicographically smallest (that is, minimizing $s_1$, then $s_2$, and so on).

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
