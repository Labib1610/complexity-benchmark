# Problem B — Amplification Factors

Time limit: 1 s
Memory limit: 256 MB

You are tasked with tuning a network of $n$ signal relays. Each relay must be configured with a gain level chosen from the set $\{1, 2\}$.

The system includes $m$ critical links, each joining two relays. To avoid signal distortion, the configuration must obey a strict relative rule across these connections: for any critical link, one of the two relays sharing the link must operate at a gain level that is exactly twice the gain level of the other.

Your goal is to determine whether a valid configuration exists for the entire network.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), indicating a critical link between relay $u$ and relay $v$.

## Output
If it is impossible to configure the network according to the rules, print `NO` on a single line.
If a valid configuration is possible, print `YES` on the first line. On the second line, provide $n$ space-separated integers $z_1 \dots z_n$ (where each $z_i \in \{1, 2\}$) to indicate the assigned gain levels for relays $1$ to $n$. If more than one valid configuration exists, output the sequence that is lexicographically smallest.

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