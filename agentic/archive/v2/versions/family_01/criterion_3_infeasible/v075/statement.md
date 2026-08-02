# Joint Collaboration Triad

Time limit: 2 s   Memory limit: 256 MB

A research foundation maintains a directory of $n$ registered experts, identified by unique IDs from $1$ through $n$. Over the years, several pairs of experts have co-authored joint publications. You are provided a list containing $m$ such co-authorship relations.

A panel requires a committee formed by three distinct experts where every two members of the committee have co-authored a publication together.

Find the committee of three experts, denoted by IDs $a, b, c$ with $a < b < c$, such that all three pairs—$(a, b)$, $(a, c)$, and $(b, c)$—have co-authored publications. If multiple valid committees exist, choose the one that minimizes $a$. If a tie remains, minimize $b$, and if still tied, minimize $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$), representing the number of experts and the number of co-authored publication links, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that expert $u$ and expert $v$ have co-authored a publication.
It is guaranteed that at least one such three-expert committee exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the lexicographically smallest committee of mutually co-authoring experts.

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
