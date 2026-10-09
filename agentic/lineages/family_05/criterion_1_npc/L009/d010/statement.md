# Problem A — Resonant Waveforms

Time limit: 5 s   Memory limit: 256 MB

## Description

A quantum communications array operates across three distinct parameter spaces:
- **k** frequency bands (indexed 1 to **k**),
- **k** polarization states (indexed 1 to **k**),
- **k** phase shifts (indexed 1 to **k**).

You are provided with a catalog of **t** potential signal paths. Each path is characterized by a triplet `(x, y, z)`, corresponding to its frequency band, polarization state, and phase shift, respectively.

When a path `(x, y, z)` is activated, it emits three independent resonance signatures based on its parameters:
- A frequency signature of $2^x$
- A polarization signature of $2^y$
- A phase signature of $2^z$

Your objective is to stabilize the array by activating a selection of **exactly k** paths from the catalog. 

The array reaches a stable state if and only if the sum of the signatures across all **k** chosen paths meets the theoretical maximum for each parameter space. Specifically, a selection of exactly **k** paths is valid if and only if all three of the following conditions are satisfied simultaneously:
1. The sum of the frequency signatures of the **k** chosen paths exactly equals $2^{k+1} - 2$.
2. The sum of the polarization signatures of the **k** chosen paths exactly equals $2^{k+1} - 2$.
3. The sum of the phase signatures of the **k** chosen paths exactly equals $2^{k+1} - 2$.

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

In Example 2, **k** = 2. The target sum for each parameter space is $2^{2+1} - 2 = 8 - 2 = 6$.
We must select exactly 2 paths. The only option is to select both available paths: `1 1 1` and `2 1 2`.
- Their frequency signatures are $2^1$ and $2^2$. Sum = $2 + 4 = 6$. (Matches target)
- Their polarization signatures are $2^1$ and $2^1$. Sum = $2 + 2 = 4$. (Does not match target)
- Their phase signatures are $2^1$ and $2^2$. Sum = $2 + 4 = 6$. (Matches target)

Because the polarization signature sum is 4 (not 6), this selection is invalid. No valid selection of exactly 2 paths exists.