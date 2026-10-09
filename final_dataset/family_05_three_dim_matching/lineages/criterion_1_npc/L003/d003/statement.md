# Archway Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

An ancient colonnade is undergoing restoration. The final structure requires exactly **k** standalone arches to be assembled from recovered ruins.

Each arch is constructed from three distinct pieces: a left pillar, a right pillar, and a central keystone. The archaeological team has excavated exactly **k** pieces of each type. Within each of the three types, the individual pieces are labeled with identifiers from 1 up to **k**.

Centuries of wear mean these pieces do not fit together uniformly. The architectural team has analyzed the stonework and produced a catalog of viable triplets. A left pillar, right pillar, and keystone can only be combined if their specific triplet appears in this catalog.

You must determine whether it is possible to reconstruct **k** complete arches. This requires choosing exactly **k** triplets from the catalog such that every excavated left pillar, right pillar, and keystone is utilized exactly once across the entire reconstruction.

## Input

The first line provides two integers, **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k³). Here, **k** represents the number of pieces per category, and **t** is the total number of viable triplets in the catalog.
The subsequent **t** lines each contain three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k). This denotes that left pillar **x**, right pillar **y**, and keystone **z** can successfully form an arch. Every triplet in the input is distinct.

## Output

If a complete reconstruction is possible, output `YES` on the initial line. Following this, output **k** lines each containing three integers `x y z`, specifying the pieces used for each of the **k** arches. If several valid reconstruction plans exist, supplying any one complete plan is sufficient. The arches may be printed in any sequence.

If it is impossible to use all the pieces to form **k** arches, output `NO`.

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

In Example 2, both viable triplets require right pillar 1. Consequently, right pillar 2 cannot be utilized, making it impossible to form 2 complete arches.