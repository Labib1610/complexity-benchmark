# Problem B — Amplification Factors

Time limit: 1 s
Memory limit: 256 MB

You are configuring a network of $n$ signal relays. You must assign each relay an amplification factor of exactly 1 or 2.

The network contains $m$ critical links, each connecting a pair of relays. To prevent signal distortion, the combined amplification across any critical link must be strictly regulated. Specifically, the product of the amplification factors of the two relays sharing a critical link must be exactly 2.

Determine if it is possible to assign an amplification factor to every relay such that all critical link constraints are satisfied.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of relays connected by a critical link.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $z_1 \dots z_n$ (where each $z_i \in \{1, 2\}$) representing the amplification factors for relays $1$ through $n$. If there are multiple valid assignments, output the one that is lexicographically smallest.

## Example 1
**Input:**
```
4 4
1 2
2 3
3 4
1 4
```
**Output:**
```
YES
1 2 1 2
```

## Example 2
**Input:**
```
3 3
1 2
1 3
2 3
```
**Output:**
```
NO
```