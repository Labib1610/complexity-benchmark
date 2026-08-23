# Hazardous Triad Identification in Chemical Repositories

Time limit: 2 s   Memory limit: 256 MB

A chemical synthesis plant maintains $n$ numbered compounds, assigned labels from $1$ through $n$. Certain pairs of compounds undergo severe exothermal reactions when brought into proximity; a safety register documents $m$ such unstable pairwise combinations.

A critical risk arises when three distinct compounds $a$, $b$, and $c$ are pairwise unstable with one another—meaning $a$ reacts with $b$, $b$ reacts with $c$, and $a$ reacts with $c$.

Safety protocol requires locating the highest-priority volatile group of three. For any valid set of three compounds arranged in ascending order of their labels $a < b < c$, priority is determined by comparing their labels lexicographically: a triple $(a_1, b_1, c_1)$ has higher priority than $(a_2, b_2, c_2)$ if $a_1 < a_2$, or if $a_1 = a_2$ and $b_1 < b_2$, or if $a_1 = a_2$, $b_1 = b_2$, and $c_1 < c_2$.

Identify and report the highest-priority triple of compounds $a$, $b$, and $c$ with $a < b < c$ such that all three pairwise interactions $(a, b)$, $(a, c)$, and $(b, c)$ appear in the safety register. It is guaranteed that at least one such triple exists.

## Input

The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), indicating the number of compounds and the number of recorded unstable pairs, respectively.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), denoting an unstable pair of compounds. No pair is listed more than once.

It is guaranteed that at least one valid triple exists.

## Output

Print three space-separated integers $a$, $b$, and $c$ on a single line, satisfying $a < b < c$, representing the lexicographically smallest valid triple.

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
