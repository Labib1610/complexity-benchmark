# Problem B — Harmonic Stability

Time limit: 1 s
Memory limit: 256 MB

You are configuring $n$ resonance crystals in a laboratory. Each crystal $i$ must be tuned to a frequency multiplier $p_i$ of either 1 or 2.

The setup contains $m$ harmonic bridges. Each bridge connects exactly two specific crystals. 

For each crystal $i$, let $d_i$ be the number of harmonic bridges connected to it. For each of these $d_i$ bridges, consider the crystal at its other end. Let $S_i$ be the sum of the squares of the frequency multipliers of these $d_i$ crystals. (If $d_i = 0$, then $S_i = 0$.)

To maintain structural stability, every crystal $i$ in the setup must satisfy the following resonance equation:
$$S_i + 3 \cdot d_i \cdot p_i = 7 \cdot d_i$$

You must assign a frequency multiplier to each of the $n$ crystals so that the entire setup is perfectly stable. If no such configuration is possible, you must report it.

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