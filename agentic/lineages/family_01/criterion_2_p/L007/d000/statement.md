# Problem B — Frequencies and Interference

Time limit: 1 s   Memory limit: 256 MB

A communication network now uses only two frequencies, labeled 1 and 2. With $n$ radio towers and $m$ interfering pairs, assign each tower a frequency so that no interfering pair shares a frequency, or report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an interfering pair of towers.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $f_1 \dots f_n$ (each in $\{1,2\}$), the lexicographically smallest valid assignment.

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
