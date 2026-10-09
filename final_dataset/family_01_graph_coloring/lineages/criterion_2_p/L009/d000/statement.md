# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

The same factory now runs only two shifts, labeled 1 and 2. With $n$ workers, there are $2^n$ possible shift configurations to consider. Given $m$ conflict pairs, search this space to assign each worker a shift so that no conflicting pair shares a shift, or report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a conflicting pair.

## Output
If no valid assignment exists in the configuration space, print a single line NO.
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
