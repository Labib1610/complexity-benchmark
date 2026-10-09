# Problem A — Resonant Waveforms

Time limit: 5 s   Memory limit: 256 MB

## Description

A quantum communications array needs to filter data streams through three dimensional parameters:
- **k** frequency bands, identified by integers 1 through **k**,
- **k** polarization states, identified by integers 1 through **k**,
- **k** phase shifts, identified by integers 1 through **k**.

You are provided with a catalog of **t** available signal paths. Each path is a triplet `(x, y, z)`, meaning it operates at frequency band **x**, polarization state **y**, and phase shift **z**.

To achieve perfect resonance, you must activate exactly **k** paths from the catalog. A selection of **k** paths is considered a valid perfect resonance configuration if and only if it satisfies the following energy conditions:
- When you calculate the frequency energy, defined as the sum of $2^x$ (2 raised to the power of **x**) for the **k** chosen paths, the total exactly equals $2^{k+1}-2$.
- When you calculate the polarization energy, defined as the sum of $2^y$ (2 raised to the power of **y**) for the **k** chosen paths, the total exactly equals $2^{k+1}-2$.
- When you calculate the phase energy, defined as the sum of $2^z$ (2 raised to the power of **z**) for the **k** chosen paths, the total exactly equals $2^{k+1}-2$.

Determine whether such a perfect resonance configuration of exactly **k** paths can be formed. If it is possible, output one valid set of **k** paths.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the scale of the system and the number of available signal paths in the catalog.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing an available path. No path is listed more than once.

## Output

If a valid perfect resonance configuration of exactly **k** paths exists, print `YES` on the first line, then print **k** lines, each containing the three parameters `x y z` of one chosen path. Any valid configuration is accepted; the paths may be printed in any order.

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

In Example 2, both available paths have a polarization state of 1. If we select exactly 2 paths from this catalog, the sum of the polarization energy will be $2^1 + 2^1 = 4$. However, for **k** = 2, the required energy is $2^{2+1}-2 = 6$. Since the sum does not match the required energy, it is impossible to form a valid perfect resonance configuration.