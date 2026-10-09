# Problem B — Factory Schedules

Time limit: 1 s   Memory limit: 256 MB

The same factory now runs only two schedules, labeled 1 and 2. With $n$ workers and $m$ incompatible pairs, designate each worker a schedule so that no incompatible pair shares a schedule, or report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an incompatible pair.

## Output
If no valid arrangement exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), the lexicographically smallest valid arrangement.

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
