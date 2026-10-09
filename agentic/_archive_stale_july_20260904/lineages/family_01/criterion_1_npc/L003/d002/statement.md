# Problem A — Shift Distribution

Time limit: 2 s
Memory limit: 256 MB

A factory employs $n$ workers. To keep operations running smoothly, the factory operates on three distinct shifts each day, labeled 1, 2, and 3. Every worker must be assigned to exactly one of these three shifts.

However, certain pairs of workers have conflicts. You are provided with a list of historical conflicts between distinct workers. If two workers have a conflict, they cannot be assigned to the same shift.

Your objective is to determine if a valid shift assignment exists for all $n$ workers. If it does, you must find the assignment that minimizes the objective function $\sum_{i=1}^n s_i \cdot 4^{n-i}$, where $s_i$ is the shift number assigned to worker $i$. 

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). The workforce size $n$ is at least 1 and capped at the 40 available workstations. The number of conflict records $m$ ranges from 0 up to the maximum possible number of distinct pairs $n(n-1)/2$.
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of distinct workers who cannot share the same shift.

## Output
If there is no valid way to assign the shifts, output a single line containing `NO`.
If a valid assignment is possible, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), where $s_i$ is the shift assigned to worker $i$. If multiple valid assignments exist, output the sequence $s_1, s_2, \dots, s_n$ that minimizes the value of $\sum_{i=1}^n s_i \cdot 4^{n-i}$.

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