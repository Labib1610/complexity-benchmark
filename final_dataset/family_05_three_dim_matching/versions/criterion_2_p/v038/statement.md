# Problem B — Orbital Stabilization

Time limit: 2 s   Memory limit: 256 MB

## Description

A planetary defense grid requires the stabilization of **k** orbital sectors. There are three categories of hardware, each containing exactly **k** units:
- **k** sensor clusters, numbered 1 to **k**,
- **k** relay stations, numbered 1 to **k**,
- **k** control frequencies, numbered 1 to **k**.

To stabilize a sector, you must establish an alignment protocol consisting of exactly one sensor cluster, one relay station, and one control frequency. You are provided with a list of **t** viable protocols, each given as a triplet `(u, v, w)`.

Due to the rigid physical tethers in the grid, each sensor cluster is hardwired to exactly one relay station. Consequently, across all viable protocols, any specific sensor cluster will only ever be listed alongside its uniquely tethered relay station, and no two distinct sensor clusters will share the same relay station. Furthermore, due to bandwidth limits, no single sensor cluster appears in more than **k** viable protocols in the input list, and the sum of the identifiers in any given protocol never exceeds **3k**.

Your task is to activate a set of exactly **k** protocols from the viable list such that every sensor cluster, every relay station, and every control frequency is incorporated into exactly one active protocol. Determine if such a configuration is achievable, and if so, report one valid set.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of units per category and the total number of viable protocols.
Each of the next **t** lines contains three integers **u**, **v**, **w** (1 ≤ u, v, w ≤ k), representing a viable protocol comprising sensor cluster **u**, relay station **v**, and control frequency **w**. No protocol is listed more than once. For each sensor cluster, every listed protocol uses the same relay station, and different sensor clusters use different relay stations.

## Output

If a valid stabilization configuration of **k** protocols exists, print `YES` on the first line, then print **k** lines, each containing the three members `u v w` of one activated protocol (in any order). Any valid set of protocols is accepted.

If no valid configuration exists, print `NO`.

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
