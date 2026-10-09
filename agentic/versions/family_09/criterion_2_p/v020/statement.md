# Problem B — Non-Reactive Protein Isolate

Time limit: 2 s   Memory limit: 256 MB

## Description

A biochemical laboratory is studying **n** newly synthesized proteins, numbered 1 to **n**. When mixed in a solution, certain pairs of these proteins will bind to each other, forming an unusable precipitate. There are **m** such known binding pairs.

Through structural analysis, the researchers have established a fundamental property of this specific batch of proteins: they implicitly fall into **two distinct structural families** (for example, "lock" and "key" shapes). As a result, **binding only ever occurs between a protein from one family and a protein from the other** — two proteins from the same family will never bind to each other. (The family classifications are not provided in the dataset; you may recover them from the binding interactions).

A set of proteins forms a **stable isolate** if no two proteins in the set bind to each other.

Given a target size **k**, determine whether a stable isolate of exactly **k** proteins can be formed, and if so, identify one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a pair of proteins that bind to each other. No binding pair is listed twice, and the interactions are guaranteed to follow the two-family structure described above (every binding event occurs between the two families).

## Output

If a stable isolate of exactly **k** proteins exists, print `YES` on the first line, then on the second line print **k** distinct protein numbers forming such an isolate, separated by spaces. Any isolate in which no two proteins bind to each other is accepted.

If no such isolate exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```

## Note

In Example 1, proteins 1 and 2 belong to the same structural family and therefore do not bind, making them a valid stable isolate of size 2. In Example 3, the largest possible stable isolate contains only 2 proteins, so a target of 3 is impossible.
