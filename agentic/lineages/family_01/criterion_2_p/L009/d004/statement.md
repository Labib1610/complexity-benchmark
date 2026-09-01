# Problem B — Harmonic Stability

Time limit: 1 s
Memory limit: 256 MB

You are configuring $n$ resonance crystals in a laboratory. Each crystal must be tuned to a frequency multiplier of either 1 or 2.

The setup contains $m$ harmonic bridges. Each bridge connects exactly two specific crystals. To maintain structural stability, each bridge requires that the frequency multipliers $p_u$ and $p_v$ of the two crystals it connects satisfy the equation $p_u^2 + p_v^2 = 5$. 

You must assign a frequency multiplier to each of the $n$ crystals so that all $m$ bridges are perfectly stable. If no such configuration is possible, you must report it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the two crystals connected by a single harmonic bridge.

## Output
If no valid tuning assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $p_1, \dots, p_n$ (each $p_i \in \{1, 2\}$), where $p_i$ is the frequency multiplier assigned to crystal $i$. If there are multiple valid assignments, output the one that is lexicographically smallest.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```