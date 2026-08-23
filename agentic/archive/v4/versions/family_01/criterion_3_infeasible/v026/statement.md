# Station Cluster Audit

Time limit: 2 s   Memory limit: 256 MB

## Description
A communications network consists of numbered relay stations. Certain pairs of stations are linked by dedicated direct two-way lines. Engineers are conducting an audit to find any group of three distinct stations that are all directly linked to one another.

It is guaranteed that at least one such group of three mutually connected stations exists in the network. Your task is to identify the lexicographically smallest such triple.

## Input
The first line contains two space-separated integers $n$ and $m$.

The station count $n$ is at least equal to the minimum group size of 3 and does not exceed the total rack capacity of 2000 stations ($3 \le n \le 2000$). The line count $m$ is at least 3 and cannot exceed the lesser of total possible station pairings or the hardware channel limit of 200,000 ($3 \le m \le \min(n(n-1)/2, 200000)$).

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a direct two-way line between station $u$ and station $v$. No pair of stations is listed more than once.

## Output
Print three space-separated integers $a$, $b$, $c$ on a single line with $a < b < c$, indicating three stations where all three pairs ($a$–$b$, $a$–$c$, $b$–$c$) are directly linked.

If multiple valid triples exist, output the lexicographically smallest one (smallest $a$; if tied, smallest $b$; if still tied, smallest $c$).

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
