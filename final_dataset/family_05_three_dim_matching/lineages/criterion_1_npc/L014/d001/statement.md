# Problem A — Compound Synthesis

Time limit: 5 s   Memory limit: 256 MB

## Description

A laboratory is synthesizing complex compounds. The inventory contains **k** distinct base fluids, **k** catalysts, and **k** thermal profiles, all indexed from 1 to **k**.

A stable reaction is a specific combination of one base fluid, one catalyst, and one thermal profile. You are given a registry of **t** known stable reactions.

A full experimental batch requires exactly **k** stable reactions from the registry. The critical constraint for a valid batch is a global exact-incidence requirement: the total set of chosen reactions must collectively involve each individual base fluid exactly once, each individual catalyst exactly once, and each individual thermal profile exactly once.

Your task is to determine whether such a batch can be formed from the registry. If it can, you must also output the specific reactions that comprise it.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k), representing the number of items per ingredient category and the number of stable reactions in the registry.

The next **t** lines each contain three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), indicating a stable reaction composed of base fluid **x**, catalyst **y**, and thermal profile **z**. No reaction appears more than once in the registry.

## Output

If a full experimental batch can be formed, print `YES` on the first line. Then, output **k** lines, each containing three integers `x y z` representing a reaction in the chosen batch. If there are multiple valid batches, any of them is accepted, and you may print the chosen reactions in any order.

If it is impossible to form a full batch, print `NO`.

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

In Example 2, both stable reactions require catalyst 1, leaving catalyst 2 impossible to be covered by the chosen set of reactions.