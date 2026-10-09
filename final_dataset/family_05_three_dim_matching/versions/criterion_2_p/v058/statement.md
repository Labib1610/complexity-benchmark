# Equilibrium Complexes

Time limit: 2 s   Memory limit: 256 MB

## Description

In a biochemical simulation, a logging system observes and records **t** stable tertiary complexes. Each complex is a triplet comprising one protein chain, one receptor site, and one catalyst enzyme.

The simulation environment contains exactly **k** distinct variants of protein chains, **k** distinct variants of receptor sites, and **k** distinct variants of catalyst enzymes, each identified by an integer from 1 to **k**.

The fundamental physical laws of this environment dictate a rigid affinity between protein chains and receptor sites. Specifically, each protein chain is exclusively compatible with one specific receptor site, establishing a perfect one-to-one correspondence between all **k** chains and all **k** sites. Consequently, every recorded tertiary complex strictly adheres to this rule: any complex containing a given protein chain will always feature its uniquely associated receptor site.

Your task is to determine whether the simulation can reach an equilibrium state based on the logged data. Equilibrium is achieved if and only if the **t** observed complexes can be filtered down to a core set of exactly **k** complexes such that every single variant of protein chain, every single variant of receptor site, and every single variant of catalyst enzyme is present exactly once in the core set.

If equilibrium is possible, you must also output one such valid core set.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of variants in each molecule category and the number of observed stable complexes.

Each of the next **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), representing a stable complex composed of protein chain **x**, receptor site **y**, and catalyst enzyme **z**. No complex is listed more than once. The input guarantees that for any given protein chain, all complexes containing it will feature the same receptor site, and no two distinct protein chains will be paired with the same receptor site.

## Output

If a valid core set of **k** complexes exists, print `YES` on the first line. Then, print **k** lines, each containing the three integers `x y z` of a complex in the chosen core set. The complexes may be printed in any order. Any valid core set is accepted.

If no valid core set exists, print `NO`.

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
