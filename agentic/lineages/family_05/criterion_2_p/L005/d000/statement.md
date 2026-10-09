# Equilibrium Complexes

Time limit: 2 s   Memory limit: 256 MB

## Description

In a biochemical simulation, there are three categories of molecules, each containing exactly **k** distinct variants numbered 1 through **k**:
- Protein chains
- Receptor sites
- Catalyst enzymes

The fundamental physics of this simulation dictates a rigid affinity between the first two categories. Specifically, each protein chain can only interact with one specific receptor site, and this relationship forms a perfect one-to-one correspondence across all **k** chains and **k** sites.

During the simulation's runtime, the logging system records **t** instances of stable tertiary complexes. A stable tertiary complex is defined as a specific triplet consisting of one protein chain, one receptor site, and one catalyst enzyme. Because the physical laws are strictly enforced, every recorded triplet containing a given protein chain will always feature its exclusively associated receptor site.

The simulation will only achieve equilibrium if it is possible to filter these recorded complexes down to a core set of exactly **k** triplets. This core set must be comprehensively exhaustive and mutually exclusive across all three categories—meaning every single protein chain, every single receptor site, and every single catalyst enzyme must appear in exactly one triplet within the chosen core set.

Given the list of **t** stable tertiary complexes observed during the run, determine whether an equilibrium state can be reached. If it is possible, identify one valid core set of **k** complexes.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of variants in each molecule category and the number of observed stable complexes.

Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a stable complex composed of protein chain **x**, receptor site **y**, and catalyst enzyme **z**. No complex is listed more than once. The input guarantees that for any given protein chain, all complexes containing it will feature the same receptor site, and no two distinct protein chains will be paired with the same receptor site.

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
