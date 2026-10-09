# Problem A — Trichrome Shifts

Time limit: 2 s   Memory limit: 256 MB

There are $n$ workers, and some pairs of workers are in conflict. A factory runs three shifts labeled 1, 2, and 3. Two workers must not be placed on the same shift if they are in conflict. Assign every worker to exactly one of the three shifts so that this rule is satisfied, or report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ — the number of workers and the number of conflict pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a conflicting pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $s_1, s_2, \ldots, s_n$ (each in $\{1, 2, 3\}$), where $s_i$ is the shift of worker $i$. Any valid assignment is accepted.

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
