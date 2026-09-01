# Problem A — Shift Distribution

Time limit: 2 s
Memory limit: 256 MB

A factory employs $n$ workers. To keep operations running smoothly, the factory operates on three distinct shifts each day, labeled 1, 2, and 3. Every worker must be assigned to exactly one of these three shifts.

However, certain pairs of workers have conflicts. You are provided with a list of historical conflicts between distinct workers. If two workers have a conflict, they cannot be assigned to the same shift.

Your objective is to determine if a valid shift assignment exists for all $n$ workers. If it does, you must find the assignment that is lexicographically smallest when formatted as a sequence of the workers' shift numbers (i.e., the shift number for worker 1 is as small as possible; in case of ties, the shift number for worker 2 is as small as possible, and so forth).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$), representing the number of workers and the number of conflict records.
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of distinct workers who cannot share the same shift.

## Output
If there is no valid way to assign the shifts, output a single line containing `NO`.
If a valid assignment is possible, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), where $s_i$ is the shift assigned to worker $i$. If multiple valid assignments exist, output the one that produces the lexicographically smallest sequence $s_1, s_2, \dots, s_n$.

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