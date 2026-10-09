# Production Schedule

Time limit: 2 s   Memory limit: 256 MB

A manufacturing facility operates continuously across three daily production shifts labeled 1, 2, and 3. The facility employs $n$ machine operators. Due to past safety incidents, certain pairs of operators cannot be scheduled during the same shift. You must assign each operator to exactly one of the three production shifts such that no two operators with a recorded safety conflict work at the same time. If no such schedule can be created, you must report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ — the number of machine operators and the number of safety conflicts ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of operators with a safety conflict.

## Output
If no valid schedule exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{1,2,3\}$), where $s_i$ is the shift of operator $i$. Any valid schedule is accepted.

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
