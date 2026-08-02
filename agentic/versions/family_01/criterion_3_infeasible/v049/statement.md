# Problem C — Shift Coordination Certificate

Time limit: 2 s   Memory limit: 256 MB

## Description
A facility manager needs to assign personnel to two separate operating sessions. Certain pairs of personnel are prohibited from being assigned to the same session due to operational restrictions. To prove that no two-session assignment can satisfy all conditions, the manager must identify a set of three individuals who are all mutually prohibited from working together—meaning a restriction is logged between every pair chosen from the three.

You are given all logged pairwise restrictions. Your task is to locate the lexicographically smallest set of three individuals $a, b, c$ with $a < b < c$ such that restrictions exist between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$.

## Input
The first line contains two integers $n$ and $m$. The headcount $n$ is at least enough to choose three individuals and does not exceed the facility cap of two thousand ($3 \le n \le 2000$). The number of pairwise restrictions $m$ is at least 3 and bounded by the minimum of all possible pair combinations and two hundred thousand ($3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), representing a restriction between person $u$ and person $v$.

At least one such group of three mutually restricted individuals is guaranteed to exist.

## Output
Print three integers $a$, $b$, $c$ on a single line separated by spaces, with $a < b < c$, indicating the lexicographically smallest trio. Lexicographical order compares $a$ first, then $b$, then $c$.

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
