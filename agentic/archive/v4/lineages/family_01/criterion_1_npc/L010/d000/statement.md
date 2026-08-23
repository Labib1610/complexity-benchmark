# Problem A — Sequential Shift Allocation

Time limit: 2 s   Memory limit: 256 MB

A factory manages $n$ workers who must each be assigned to one of three available work shifts, labeled 1, 2, and 3. The workers are ordered sequentially from 1 to $n$. A set of $m$ pair restrictions specifies which pairs of workers are incompatible and cannot share the same shift.

Due to standard operational procedures, workers are assigned in sequential order from worker 1 up to worker $n$. Find a valid assignment of shifts to all $n$ workers such that no incompatible pair shares a shift, maximizing the preference for lower shift numbers in order of worker index (i.e., the lexicographically smallest sequence $s_1, s_2, \dots, s_n$). If no such assignment satisfies all restrictions, report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ — the number of workers and the number of incompatible pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ $v$ — an incompatible pair of workers ($1 \le u, v \le n$, $u \ne v$).

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line print $n$ integers $s_1, s_2, \dots, s_n$ (each in \{1, 2, 3\}), where $s_i$ denotes the shift assigned to worker $i$. Output the lexicographically smallest sequence among all valid assignments.

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
