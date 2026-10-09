# Problem C — Worker Roster

Time limit: 2 s   Memory limit: 256 MB

The factory management is analyzing its worker roster of $n$ employees. You are provided with a log containing $m$ distinct unordered pairs of employees that have been flagged for review.

Your task is to identify a subset of exactly three employees such that the provided log contains exactly three pairs where both employees in the pair belong to this subset.

It is guaranteed that the log contains at least one such subset of three employees. Output one such subset.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a flagged pair of employees. The pairs in the log are distinct, and $u \neq v$.
It is guaranteed that at least one valid subset of three employees exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ representing the identified subset. Output the lexicographically smallest such subset (smallest $a$; ties broken by smallest $b$; then smallest $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```