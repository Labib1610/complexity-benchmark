# Problem C — Resonance Cascades

Time limit: 2 s   Memory limit: 256 MB

You are analyzing a high-energy resonance chamber containing $n$ distinct particle types, numbered 1 to $n$. Certain pairs of particle types are highly reactive and will resonate if they come into contact. There are $m$ such reactive pairs.

A *resonance cascade* occurs when three distinct particle types mutually resonate with each other (i.e., all three pairs among the three particle types are reactive). Your task is to prove that the chamber is unstable by identifying a resonance cascade.

It is guaranteed that at least one such set of three particle types exists. Additionally, due to the physical limitations of the chamber, the following properties are guaranteed to hold for every test case:
- No single particle type can resonate with more than $n-1$ other particle types.
- The total number of reactive pairs $m$ is strictly less than $n^2 / 2$.
- For any valid resonance cascade $(a, b, c)$, the sum of the three particle identifiers is strictly less than $3n$.

If there are multiple possible cascades, you must output the one that is lexicographically smallest. A cascade $(a, b, c)$ with $a < b < c$ is lexicographically smaller than $(x, y, z)$ with $x < y < z$ if $a < x$, or if $a = x$ and $b < y$, or if $a = x$, $b = y$, and $c < z$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) — a pair of particle types that resonate with each other. Each reactive pair is listed at most once.
It is guaranteed that at least one cascade of three mutually resonant particle types exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are reactive. Output the lexicographically smallest such triple.

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
