# Problem A — Distributed Portfolio Analysis

Time limit: 2 s   Memory limit: 256 MB

A quantitative trading firm is preparing to run risk simulations on $n$ financial portfolios, numbered from $1$ to $n$. The firm operates three independent analysis engines, designated as Engine 1, Engine 2, and Engine 3. Each portfolio must be routed to exactly one of these engines for processing.

During the pre-processing phase, the firm identified $m$ specific pairs of portfolios that contain overlapping derivative assets. Due to a known issue in the simulation software, if two portfolios with overlapping assets are routed to the same analysis engine, the engine's memory cache will become corrupted, invalidating the results. Therefore, any two portfolios in an overlapping pair must be routed to different engines.

The firm's task scheduler requires the routing plan to be formulated as a sequence of $n$ engine numbers, where the $i$-th number corresponds to the engine assigned to portfolio $i$. To ensure reproducibility in the scheduling logs, if there are multiple valid routing plans that avoid cache corruption, the scheduler must use the sequence that is lexicographically smallest.

If it is impossible to route all portfolios safely across the three engines, the system must abort the simulation batch.

## Input
The first line contains two integers $n$ and $m$ — the number of portfolios and the number of overlapping pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing a pair of portfolios that share overlapping assets and must not be routed to the same engine.

## Output
If no safe routing plan is possible, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $e_1, e_2, \dots, e_n$ (where each $e_i \in \{1, 2, 3\}$), representing the engine assigned to portfolio $i$. Among all valid plans, output the lexicographically smallest sequence (compare $e_1$ first, then $e_2$, and so on).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```