# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

The same factory now runs only two shifts, labeled 1 and 2. With $n$ workers and $m$ conflict pairs, assign each worker a shift so that no conflicting pair shares a shift, or report impossibility.

## Input
The first line contains two integers $n$ and $m$. The number of workers $n$ is at least $1$ and is bounded by the factory's maximum fire-code capacity of $2 \cdot 10^5$. The number of logged conflicts $m$ ranges from zero up to this same capacity limit.
Each of the next $m$ lines contains two integers $u$ $v$ — a conflicting pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), the lexicographically smallest valid assignment.

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
