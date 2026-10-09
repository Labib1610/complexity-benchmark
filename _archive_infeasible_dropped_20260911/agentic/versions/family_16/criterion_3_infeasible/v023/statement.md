# Invalid Blueprint: Certification

Time limit: 2 s
Memory limit: 256 MB

## Description

You are analyzing a blueprint for placing **j** pairs of structural elements (each pair is designated as a `JOB` in the system outputs) onto two parallel coordinate axes, Axis 1 and Axis 2.

Each pair **i** (from 1 to **j**) consists of a primary segment of length **p1** and a secondary segment of length **p2**. The placement must satisfy the following geometric constraints:

1. For every pair, its primary segment must be placed on Axis 1, and its secondary segment must be placed on Axis 2.
2. Segments placed on the same axis must not overlap (though they may touch at their endpoints).
3. For every pair **i**, the starting coordinate of its secondary segment on Axis 2 must be greater than or equal to the ending coordinate of its primary segment on Axis 1.
4. All segments must be placed entirely within the coordinate interval [0, **T**].

For every input in this problem, it is **guaranteed that no valid placement exists**. Your task is to identify and output a certificate proving this impossibility. Exactly one of the following conditions will always apply. Print the one that holds:

- **Individual Span Exceeded:** If a specific pair **i** cannot be placed within the interval [0, **T**] because the constraint between its primary and secondary segments forces it to span a total distance greater than **T** by itself.
  Print: `JOB i` — where **i** (1-based) is the index of the pair.

- **Axis Overcapacity:** If an axis cannot accommodate all of its assigned segments because their combined length strictly exceeds **T**.
  Print: `LOAD c` — where **c** is 1 or 2, corresponding to the axis whose total segment length exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the lengths of the primary and secondary segments for that pair.

## Output

Print a single line: `JOB i` (if **p1** + **p2** > **T** for pair **i**) or `LOAD c` (if the sum of all segment lengths on Axis **c** exceeds **T**).

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, pair 1 requires a primary segment of 70 and a secondary segment of 60. Because the secondary segment cannot start before the primary segment ends, the minimum coordinate span required for this pair alone is 70 + 60 = 130. Since 130 > 100, `JOB 1` proves the placement is impossible.

In Example 2, no single pair exceeds the interval length of 150. However, Axis 1 must accommodate four primary segments of length 50 without overlapping. Their combined length is 50 + 50 + 50 + 50 = 200. Since 200 > 150, `LOAD 1` is the certificate.
