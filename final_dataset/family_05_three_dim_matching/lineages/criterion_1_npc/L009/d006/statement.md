# Problem A — Resonant Waveforms

Time limit: 5 s   Memory limit: 256 MB

## Description

A quantum communications array needs to align its data streams across three distinct parameter spaces:
- **k** frequency bands, labeled 1 through **k**,
- **k** polarization states, labeled 1 through **k**,
- **k** phase shifts, labeled 1 through **k**.

You are given a catalog of **t** available signal paths. Each path is defined by a triplet `(x, y, z)`, specifying its frequency band **x**, polarization state **y**, and phase shift **z**.

To stabilize the array, you must activate exactly **k** paths from the catalog. A selection of exactly **k** paths forms a valid stable configuration if and only if it satisfies the following energy equivalence:
- For each activated path `(x, y, z)`, its resonance footprint is defined as $F = 100^x + 100^{k+y} + 100^{2k+z}$.
- The total system footprint, calculated as the sum of the resonance footprints of all **k** activated paths, must be exactly equal to $\frac{100^{3k+1} - 100}{99}$.

Determine whether a valid stable configuration of exactly **k** paths exists. If so, output one such valid set of **k** paths.

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

In Example 2, **k** = 2, so the target total system footprint is $\frac{100^{3(2)+1} - 100}{99} = \frac{100^7 - 100}{99} = 1010101010100$.
If we select the two available paths:
- The path `1 1 1` has a resonance footprint of $100^1 + 100^{2+1} + 100^{4+1} = 100 + 1000000 + 10000000000 = 10001000100$.
- The path `2 1 2` has a resonance footprint of $100^2 + 100^{2+1} + 100^{4+2} = 10000 + 1000000 + 1000000000000 = 1000001010000$.

The sum of these footprints is $10001000100 + 1000001010000 = 1010002020100$. Since this sum does not exactly equal the target footprint of 1010101010100, this configuration is invalid, making it impossible to form a stable configuration.