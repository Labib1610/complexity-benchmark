# Problem A — Sequential Layer Alignment

Time limit: 5 s   Memory limit: 256 MB

## Description

You are configuring a sequential data pipeline. The system is highly structured, consisting of exactly three distinct, non-overlapping layers:
- Layer 1 contains **k** data sources.
- Layer 2 contains **k** transformer nodes.
- Layer 3 contains **k** storage destinations.

Components in each layer are indexed from 1 to **k**.

Many network routing tasks involve pairing two types of components directly. In this system, the architecture is strictly three-tiered, so data must flow sequentially across all stages. You are provided with a list of **t** compatible pathways. Each pathway is a validated triplet `(source, transformer, destination)` that bridges the three layers.

Your goal is to achieve maximum, uniform utilization across the entire pipeline. To do this, you must select exactly **k** pathways from the provided list such that no two selected pathways share any component. Because the layers are completely disjoint and equal in size, this strict selection guarantees that every single source, every single transformer, and every single destination is activated exactly once.

Determine if such a perfect alignment is possible, and if so, output the chosen pathways.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of components in each of the three layers, and the number of compatible pathways.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k). This indicates a compatible pathway connecting source **x**, transformer **y**, and destination **z**. No pathway is listed more than once.

## Output

If a perfect alignment of **k** pathways exists, print `YES` on the first line. Then, print **k** lines, each containing the three integers `x y z` of a selected pathway. If multiple valid alignments exist, you may output any of them. The pathways can be printed in any order.

If no such alignment exists, print `NO`.

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

In Example 2, both compatible pathways require transformer node 1, meaning transformer node 2 can never receive an assignment.
