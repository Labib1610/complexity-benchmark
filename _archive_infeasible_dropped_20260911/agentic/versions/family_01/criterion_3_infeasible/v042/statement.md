# Problem C — Frequency Allocation Certificate

Time limit: 2 s   Memory limit: 256 MB

The telecommunications authority only has two distinct broadcasting bands available for a new regional network. Towers with overlapping coverage areas must be assigned different bands to avoid interference. You have been informed that a valid allocation for this network is strictly impossible.

Your task is to provide the authority with a concrete proof of this impossibility. A simple and undeniable proof consists of identifying three specific towers where every tower in the trio overlaps with the other two. Such a configuration clearly cannot be resolved with only two bands. The network data is guaranteed to contain at least one such trio.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$), representing the number of radio towers and the number of overlapping pairs, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ — indicating that the coverage areas of tower $u$ and tower $v$ overlap.
It is guaranteed that at least one trio of mutually overlapping towers exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that all three pairs ($a$ and $b$, $a$ and $c$, $b$ and $c$) overlap. Output the lexicographically smallest such trio (minimize $a$; in case of a tie, minimize $b$; then minimize $c$).

## Example 1
### Input
```
4 5
1 2
1 3
2 3
2 4
3 4
```
### Output
```
1 2 3
```

## Example 2
### Input
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
### Output
```
1 2 4
```
