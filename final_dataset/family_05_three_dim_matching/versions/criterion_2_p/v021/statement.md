# Problem B — Material Synthesis

Time limit: 2 s   Memory limit: 256 MB

## Description

You are synthesizing a new material that requires **k** distinct chemical processes to run simultaneously. Each process requires exactly three components:
- One catalyst (labeled 1 to **k**)
- One reagent (labeled 1 to **k**)
- One solvent (labeled 1 to **k**)

You are provided a catalog of **t** stable process configurations. Each configuration specifies a compatible triplet: a catalyst, a reagent, and a solvent.

Due to molecular bonding properties, a catalyst will only react in the presence of its specific counterpart reagent. In the catalog, any given catalyst is always listed with the exact same reagent. Furthermore, each reagent acts as a counterpart to only one catalyst, meaning no reagent is ever listed with multiple different catalysts.

Your goal is to select exactly **k** configurations from the catalog such that every catalyst, every reagent, and every solvent from 1 to **k** is utilized in exactly one of the chosen processes. Determine if this is possible, and if so, report one valid set of configurations.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of each component type and the number of stable configurations.

Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a stable configuration consisting of catalyst **x**, reagent **y**, and solvent **z**. No configuration is listed more than once. The catalog guarantees that for any catalyst, all its listed configurations use the same reagent, and different catalysts use different reagents.

## Output

If a valid set of **k** processes exists, print `YES` on the first line, then print **k** lines, each containing the three integers `x y z` of one chosen configuration. The chosen configurations may be listed in any order. Any valid set is accepted.

If no valid set exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
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
2 2 1
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
