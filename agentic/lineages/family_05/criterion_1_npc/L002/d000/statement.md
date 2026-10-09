# Problem A — Synthetic Organisms

Time limit: 5 s   Memory limit: 256 MB

## Description

A laboratory is synthesizing a batch of **k** artificial organisms. Every viable organism must be constructed from exactly three components:

- One membrane type (from a supply of **k** distinct types, numbered 1..k),
- One metabolic pathway (from a supply of **k** distinct pathways, numbered 1..k),
- One replication sequence (from a supply of **k** distinct sequences, numbered 1..k).

Because of biochemical interactions, only certain specific combinations of these three components will result in a stable organism. You are provided with a catalog of **t** stable component triplets `(m, p, s)`.

The laboratory's goal is to select exactly **k** stable combinations from the catalog to synthesize **k** organisms, with the strict requirement that every single membrane type, every metabolic pathway, and every replication sequence from the supplies is utilized in **exactly one** synthesized organism.

Determine whether such a selection is possible, and if so, provide one valid set of **k** combinations.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of each type of component, and the number of stable combinations in the catalog.
Each of the following **t** lines contains three integers **m**, **p**, and **s** (1 ≤ m, p, s ≤ k), representing a stable combination of a membrane type, a metabolic pathway, and a replication sequence. No combination is listed more than once.

## Output

If a valid selection of **k** combinations exists, print `YES` on the first line. Then, print **k** lines, each containing the three components `m p s` of a chosen combination. Any selection that uses every membrane type, metabolic pathway, and replication sequence exactly once is accepted; the combinations may be printed in any order.

If no such selection exists, print `NO`.

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

In Example 2, both stable combinations use metabolic pathway 1, so metabolic pathway 2 can never be utilized.
