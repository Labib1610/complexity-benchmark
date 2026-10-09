# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

The same facility now requires exactly two distinct roles, labeled 1 and 2. With $n$ personnel (numbered 1 to $n$) and $m$ incompatible pairs, designate a role for each person so that no incompatible pair receives the same role, or report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an incompatible pair of personnel.

## Output
If no valid designation exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), the lexicographically smallest valid designation.

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
