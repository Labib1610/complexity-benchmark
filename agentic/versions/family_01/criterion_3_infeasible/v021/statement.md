# Signal Interference Identification

Time limit: 2 s   Memory limit: 256 MB

An electronic laboratory contains $n$ measurement units labeled $1$ through $n$. There are $m$ recorded instances of cross-talk interference between pairs of units. Each recorded instance indicates that two specific units interfere with one another.

It is guaranteed that there is at least one set of three distinct units where every pair among the three produces cross-talk interference.

Your task is to find three units $a, b, c$ with $a < b < c$ such that cross-talk interference exists between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$. If there are multiple such groups, output the lexicographically smallest one (minimizing $a$, then $b$, then $c$).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$).

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a pair of interfering units.

It is guaranteed that at least one qualifying group of three units exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, corresponding to the lexicographically smallest group of three units where every pair interferes.

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
