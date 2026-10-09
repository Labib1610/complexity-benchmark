# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

A factory has $n$ workers and a set of $m$ conflict pairs. The factory schedules exactly two shifts, labeled 1 and 2. The main operational rule is that no conflicting pair of workers may share the same shift. You must assign each worker to a shift so that this rule is respected, or report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a conflicting pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
