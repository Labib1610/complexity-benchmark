# Shift Schedule Verification

Time limit: 2 s   Memory limit: 256 MB

An industrial facility manages a team of workers labeled with integer IDs from $1$ to $n$. Certain pairs of workers are subject to direct operational interference rules, meaning they cannot perform duties together during the same working session.

To demonstrate that a dual-shift arrangement cannot completely eliminate all operational interference, management wishes to identify a group of three workers where every pair within the group has an active interference rule. Among all such groups of three, you must determine the one with the lexicographically smallest worker IDs $(a, b, c)$ satisfying $a < b < c$.

## Input
The first line contains two integers $n$ and $m$, representing the number of workers and the total number of interference rules, respectively.

The facility's capacity supports a headcount $n$ satisfying $3 \le n \le 2000$. The total count of interference rules $m$ satisfies $3 \le m \le \min\left(\frac{n(n-1)}{2}, 200000\right)$.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that worker $u$ and worker $v$ share a direct interference rule. No unordered pair $(u, v)$ is listed more than once.

It is guaranteed that at least one valid group of three mutually interfering workers exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line, where $1 \le a < b < c \le n$, representing the tuple that is lexicographically minimal (minimizing $a$; breaking ties by smallest $b$; then by smallest $c$).

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
