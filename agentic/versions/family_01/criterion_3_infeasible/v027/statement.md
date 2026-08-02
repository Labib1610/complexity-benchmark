# Chemical Safety Audit: Priority Hazard Identification

Time limit: 2 s   Memory limit: 256 MB

A chemical manufacturing facility stores $n$ distinct substances, assigned unique index numbers from $1$ to $n$. Due to reactivity risks, certain pairs of substances are strictly prohibited from sharing a storage container. You are given a roster of $m$ such prohibited pairs.

A critical safety vulnerability occurs whenever three distinct substances $a$, $b$, and $c$ are pairwise prohibited from being stored together—that is, substance $a$ is prohibited with substance $b$, substance $b$ is prohibited with substance $c$, and substance $a$ is prohibited with substance $c$.

Safety protocol mandates reporting the single most critical vulnerability. When comparing two valid triples $(a_1, b_1, c_1)$ and $(a_2, b_2, c_2)$ each arranged such that $a_i < b_i < c_i$, triple 1 takes priority over triple 2 if $a_1 < a_2$; if $a_1 = a_2$, then if $b_1 < b_2$; and if $a_1 = a_2$ and $b_1 = b_2$, then if $c_1 < c_2$.

Find and output the highest-priority triple of substances $a$, $b$, and $c$ with $a < b < c$ such that all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are present in the prohibited roster. It is guaranteed that at least one such triple exists.

## Input

The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of substances and the number of prohibited pairs, respectively.

Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that substance $u$ and substance $v$ cannot share a container. No pair of substances is listed more than once.

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
