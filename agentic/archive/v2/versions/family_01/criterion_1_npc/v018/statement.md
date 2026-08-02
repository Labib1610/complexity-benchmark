# Operational Scheduling

Time limit: 2 s   Memory limit: 256 MB

An industrial plant maintains a roster of $n$ workers, indexed from $1$ to $n$. A collection of $m$ incompatible worker pairs is specified; two workers forming an incompatible pair cannot perform duties during the same time window.

The plant's daily operations are divided into three distinct time windows, designated by the identifiers 1, 2, and 3. Each worker must be assigned to exactly one of these three time windows. A schedule is considered valid if no two workers in any incompatible pair are assigned to the same time window.

Determine if a valid schedule exists. If multiple valid schedules exist, output the one that produces the lexicographically smallest sequence of time window assignments $s_1, s_2, \dots, s_n$. If no valid schedule exists, report this outcome.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of workers and the number of incompatible pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) representing an incompatible pair of workers.

## Output
If no valid schedule exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), where $s_i$ denotes the assigned time window for worker $i$. Among all valid schedules, print the lexicographically smallest sequence.

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
