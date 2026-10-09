# Problem A — Resonant Waveforms

Time limit: 5 s   Memory limit: 256 MB

## Description

A quantum communications array operates across three distinct parameter spaces:
- **k** frequency bands (indexed 1 to **k**),
- **k** polarization states (indexed 1 to **k**),
- **k** phase shifts (indexed 1 to **k**).

You are provided with a catalog of **t** potential signal paths. Each path is characterized by a triplet `(x, y, z)`, corresponding to its frequency band, polarization state, and phase shift, respectively.

Your objective is to stabilize the array by activating exactly **k** paths from the catalog. The array reaches a stable state if and only if the combined energy signature of the chosen paths matches a critical threshold. 

Specifically:
- The energy signature of a single path `(x, y, z)` is given by the integer value $E = (1 \ll x) + (1 \ll (k+y)) + (1 \ll (2k+z))$, where $\ll$ denotes the bitwise left-shift operator.
- A set of exactly **k** paths forms a stable configuration if the standard arithmetic sum of their energy signatures equals exactly $(1 \ll (3k+1)) - 2$.

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

In Example 2, **k** = 2, so the target total system footprint is $(1 \ll (3 \times 2 + 1)) - 2 = (1 \ll 7) - 2 = 128 - 2 = 126$.
If we select the two available paths:
- The path `1 1 1` has an energy signature of $(1 \ll 1) + (1 \ll (2+1)) + (1 \ll (4+1)) = 2 + 8 + 32 = 42$.
- The path `2 1 2` has an energy signature of $(1 \ll 2) + (1 \ll (2+1)) + (1 \ll (4+2)) = 4 + 8 + 64 = 76$.

The arithmetic sum of these signatures is $42 + 76 = 118$. Since this sum does not exactly equal the target threshold of 126, this configuration is invalid, making it impossible to form a stable configuration.