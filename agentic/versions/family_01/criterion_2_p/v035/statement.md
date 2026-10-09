# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

The factory must evaluate the $2^n$ possible ways to assign its $n$ workers to shifts to find a valid schedule. Each worker must be assigned to an available shift; the number of available shifts is exactly two (labeled 1 and 2). You are given $m$ constraints. Each constraint specifies a pair of workers who must not be assigned the same shift. Search the space of assignments to find one where no constraint is violated, or report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ $v$ — a constraint pair.

## Output
If no valid assignment exists among the possibilities, print a single line NO.
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
