# Archway Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

The archaeological team is restoring an ancient colonnade. The goal is to successfully assemble exactly **k** standalone monuments from the recovered ruins.

The ruins consist of foundation blocks, column shafts, and decorative capitals. Each of these three categories of components has pieces labeled with identifiers from 1 to **k**.

Due to centuries of wear, not all pieces fit together. The architectural team has analyzed the stonework and produced a catalog of viable configurations. A configuration consists of a foundation block, a column shaft, and a decorative capital that can successfully form a single monument.

You must determine if it is possible to select exactly **k** configurations from this catalog such that all selected monuments are structurally disjoint. Specifically, a selection of **k** configurations is valid if and only if no two chosen configurations share the same foundation block, no two chosen configurations share the same column shaft, and no two chosen configurations share the same decorative capital.

## Input

The first line provides two integers, **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k³). Here, **k** represents the maximum identifier for the pieces in each category, and **t** is the total number of viable configurations in the catalog.
The next **t** lines each contain three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k). This denotes that foundation block **x**, column shaft **y**, and decorative capital **z** can successfully form a monument. Every configuration in the input is distinct.

## Output

If a valid selection is possible, output `YES` on the initial line. Following this, output **k** lines each containing three integers `x y z`, specifying the pieces used for each of the **k** monuments. If several valid selections exist, supplying any one of them is sufficient. The monuments may be printed in any sequence.

If it is impossible to find **k** disjoint configurations, output `NO`.

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

In Example 2, both viable configurations use column shaft 1. Consequently, it is impossible to select 2 configurations that do not share a column shaft, making it impossible to form 2 disjoint monuments.