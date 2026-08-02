# Roster Incompatibility Audit

Time limit: 2 s   Memory limit: 256 MB

A facility employs $n$ workers, numbered $1$ through $n$. A central registry maintains a list of $m$ prohibited pairings: pairs of workers who are mutually incompatible and cannot share an assignment.

An audit requires finding a three-worker team $a, b, c$ that is completely non-cooperative—meaning that all three pairwise relationships ($a$ with $b$, $a$ with $c$, and $b$ with $c$) are listed in the registry as prohibited.

It is guaranteed that at least one such three-worker team exists in the provided registry. Find and report the team $a, b, c$ satisfying $a < b < c$ that is lexicographically smallest (i.e., smallest possible $a$; breaking ties by smallest $b$; breaking further ties by smallest $c$).

## Input

The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), the number of workers and the number of prohibited pairings.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that worker $u$ and worker $v$ form a prohibited pairing. No unordered pair of workers appears more than once.

It is guaranteed that at least one three-worker team exists where all three pairs are prohibited.

## Output

Print three space-separated integers $a, b, c$ on a single line such that $1 \le a < b < c \le n$, all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are prohibited, and the triple $(a, b, c)$ is lexicographically smallest.

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
