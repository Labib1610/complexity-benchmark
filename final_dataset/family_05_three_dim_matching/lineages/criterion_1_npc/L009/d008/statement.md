# Problem A — Resonant Waveforms

Time limit: 5 s   Memory limit: 256 MB

## Description

A quantum communications array operates across three distinct parameter spaces:
- **k** frequency bands (indexed 1 to **k**),
- **k** polarization states (indexed 1 to **k**),
- **k** phase shifts (indexed 1 to **k**).

The system features $3k$ orbital resonance levels. The capacity $C_i$ of each level $i$ (for $1 \le i \le 3k$) is defined sequentially:
- The capacity of the first level is $C_1 = 2$.
- For any level $i > 1$, its capacity is given by $C_i = 2 + \sum_{j=1}^{i-1} C_j$.

You are provided with a catalog of **t** potential signal paths. Each path is characterized by a triplet `(x, y, z)`, corresponding to its frequency band, polarization state, and phase shift, respectively.

When a path `(x, y, z)` is activated, it draws power from three specific resonance levels: level $x$, level $k+y$, and level $2k+z$. The energy signature of this path is the arithmetic sum of the capacities of these three levels: $E = C_x + C_{k+y} + C_{2k+z}$.

Your objective is to stabilize the array by activating exactly **k** paths from the catalog. The array reaches a stable state if and only if the combined energy signature of the chosen paths exactly matches the total capacity of all $3k$ levels in the system (i.e., $\sum_{i=1}^{3k} C_i$).

Determine whether there is a subset of exactly **k** paths that achieves this stable configuration. If a valid configuration exists, output one such valid set.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the scale of the system and the number of available signal paths in the catalog.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing an available path. No path is listed more than once.

## Output

If a valid stable configuration of exactly **k** paths exists, print `YES` on the first line, then print **k** lines, each containing the three parameters `x y z` of one chosen path. Any valid configuration is accepted; the paths may be printed in any order.

If no valid configuration exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 1 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, **k** = 2, so there are $3 \times 2 = 6$ resonance levels.
Their capacities are:
- $C_1 = 2$
- $C_2 = 2 + 2 = 4$
- $C_3 = 2 + (2 + 4) = 8$
- $C_4 = 2 + (2 + 4 + 8) = 16$
- $C_5 = 2 + (2 + 4 + 8 + 16) = 32$
- $C_6 = 2 + (2 + 4 + 8 + 16 + 32) = 64$

The total capacity of all 6 levels is $2 + 4 + 8 + 16 + 32 + 64 = 126$. This is the target threshold.

If we select the two available paths:
- The path `1 1 1` draws from levels 1, 3, and 5. Its energy signature is $C_1 + C_3 + C_5 = 2 + 8 + 32 = 42$.
- The path `2 1 2` draws from levels 2, 3, and 6. Its energy signature is $C_2 + C_3 + C_6 = 4 + 8 + 64 = 76$.

The arithmetic sum of these signatures is $42 + 76 = 118$. Since this sum does not exactly equal the target threshold of 126, this configuration is invalid, making it impossible to form a stable configuration.