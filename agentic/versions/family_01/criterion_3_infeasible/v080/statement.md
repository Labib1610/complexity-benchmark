# Radio Frequency Collision Audit

Time limit: 2 s   Memory limit: 256 MB

A telecommunications authority manages $n$ regional broadcasting stations, assigned numerical IDs from $1$ through $n$ based on their registration order. Due to geographic proximity and shared spectrum allocations, certain pairs of stations experience direct signal overlap, preventing simultaneous unattenuated broadcasts between them.

A regulatory compliance rule flags a critical collision whenever three distinct stations $a$, $b$, and $c$ (with $a < b < c$) form a mutual conflict triplet—meaning direct signal overlap exists between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$.

To prioritize corrective filtering, the authority must isolate the first such triplet in registration order. Specifically, you need to identify the valid triplet $(a, b, c)$ that is lexicographically smallest: minimizing $a$ first, then $b$, and finally $c$. The network configuration is guaranteed to contain at least one such triplet.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$)—the total number of broadcasting stations and the number of station pairs with direct signal overlap, respectively.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that station $u$ and station $v$ experience direct signal overlap. Each unordered pair of stations appears at most once in the input.

It is guaranteed that at least one mutual conflict triplet exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ ($1 \le a < b < c \le n$) on a single line, representing the lexicographically smallest triplet of stations where every pair experiences direct signal overlap.

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
