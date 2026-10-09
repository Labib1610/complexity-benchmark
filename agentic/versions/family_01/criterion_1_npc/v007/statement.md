# Problem A — Trichrome Shifts

Time limit: 2 s   Memory limit: 256 MB

A factory runs three shifts labeled 1, 2, 3. There are $n$ workers. Some pairs of workers are in conflict and must not be placed on the same shift. It is guaranteed that no worker is in conflict with more than 39 other workers, and the total number of conflicts across the factory does not exceed 780. Assign every worker to exactly one of the three shifts so that no conflicting pair shares a shift, or report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ — the number of workers and the number of conflict pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a conflicting pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{1,2,3\}$), where $s_i$ is the shift of worker $i$. Any valid assignment is accepted.

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
