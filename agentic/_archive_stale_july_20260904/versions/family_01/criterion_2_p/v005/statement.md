# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

The same factory now runs only two shifts, labeled 1 and 2. With $n$ workers and $m$ conflict pairs, assign each worker a shift so that no conflicting pair shares a shift, or report impossibility.

## Input
The first line contains two integers $n$ and $m$. The factory employs $n$ workers, where there is always at least one worker but no more than the facility's maximum capacity of $2 \cdot 10^5$. The number of conflict pairs $m$ can be zero, but will not exceed the HR database limit of $2 \cdot 10^5$.
Each of the next $m$ lines contains two integers $u$ and $v$ — a conflicting pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), the lexicographically smallest valid assignment.

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
