# Problem A — Resonant Waveforms

Time limit: 5 s   Memory limit: 256 MB

## Description

A quantum communications array needs to filter data streams through three dimensional parameters:
- **k** frequency bands, identified by integers 1 through **k**,
- **k** polarization states, identified by integers 1 through **k**,
- **k** phase shifts, identified by integers 1 through **k**.

You are provided with a catalog of **t** available signal paths. Each path is a triplet `(x, y, z)`, meaning it operates at frequency band **x**, polarization state **y**, and phase shift **z**.

To achieve perfect resonance, you must activate exactly **k** paths from the catalog. A selection of exactly **k** paths is considered a valid perfect resonance configuration if and only if it satisfies the following unified energy condition:
- Consider a base system capacity defined as $C = 2^{3k+1} - 1$.
- For each chosen path `(x, y, z)`, calculate its interference mask as $M = C - 2^x - 2^{k+y} - 2^{2k+z}$.
- When you perform a bitwise AND operation across the interference masks of all **k** chosen paths, the final resulting value must exactly equal 1.

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

In Example 2, **k** = 2, so the base system capacity is $C = 2^{3(2)+1} - 1 = 2^7 - 1 = 127$.
If we select the two available paths:
- The path `1 1 1` has an interference mask of $127 - 2^1 - 2^{2+1} - 2^{4+1} = 127 - 2 - 8 - 32 = 85$.
- The path `2 1 2` has an interference mask of $127 - 2^2 - 2^{2+1} - 2^{4+2} = 127 - 4 - 8 - 64 = 51$.

The bitwise AND of 85 and 51 is 17. Since this final value does not exactly equal 1, this configuration is invalid, making it impossible to form a perfect resonance configuration.