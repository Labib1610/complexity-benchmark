# Problem C — Impossible Ribbon: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A manufacturing plant is decorating a continuous ribbon of length **T** millimeters. The order consists of **j** distinct motifs. The decoration process involves two operational phases for each motif: an alpha phase and a beta phase.

For each motif, the alpha phase requires a continuous segment of length **p1** mm, and the beta phase requires a continuous segment of length **p2** mm. 

A valid application must adhere to the following rules:
1. For any single motif, its beta phase segment must be positioned so that its left endpoint is greater than or equal to the right endpoint of its alpha phase segment.
2. All alpha phase segments for all motifs share the primary channel, so they must be placed such that no two alpha segments overlap (their intersection has a length of zero).
3. All beta phase segments for all motifs share the secondary channel, so they must also be placed such that no two beta segments overlap.
4. All segments must be completely contained within the ribbon's span, from 0 to **T**.

Every provided order represents an impossible configuration—there is no valid arrangement of segments that can satisfy all constraints on a ribbon of length **T**. Instead of attempting to place them, your task is to identify the bottleneck that proves the configuration is unachievable, providing a short certificate the system can verify.

A configuration is impossible because it violates a fundamental 1D spatial invariant. Exactly one of the following invariants is broken. Output the applicable certificate:

- **Motif Span Invariant:** For some motif **i**, there exists no assignment of its alpha phase (as a sub-interval of length **p1**) and beta phase (as a sub-interval of length **p2**) within [0, **T**] such that the beta phase's left endpoint is greater than or equal to the alpha phase's right endpoint. Output `JOB i` (where **i** is the 1-based index of the motif).
- **Alpha Channel Invariant:** There exists no assignment of the alpha phases for all **j** motifs (each as a sub-interval of its respective length **p1**) within [0, **T**] such that the intersection of any two alpha sub-intervals has a length of zero. Output `LOAD 1`.
- **Beta Channel Invariant:** There exists no assignment of the beta phases for all **j** motifs (each as a sub-interval of its respective length **p2**) within [0, **T**] such that the intersection of any two beta sub-intervals has a length of zero. Output `LOAD 2`.

You are guaranteed that exactly one of these invariants will be broken for the given input.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the alpha phase length and beta phase length of a motif.

## Output

Print a single line: `JOB i` (for a motif bottleneck) or `LOAD c` (for a channel bottleneck, where **c** is 1 for the alpha channel or 2 for the beta channel).

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

In Example 1, for motif 1, its alpha and beta phases require 70 mm and 60 mm respectively. There is no assignment of these two segments as sub-intervals within [0, 100] such that the beta phase's left endpoint is greater than or equal to the alpha phase's right endpoint, breaking the Motif Span Invariant. Thus `JOB 1` is the correct proof of impossibility. 

In Example 2, no single motif breaks the Motif Span Invariant. However, the alpha phases require segments of lengths 50, 50, 50, and 50. There is no assignment of these four segments as sub-intervals within [0, 150] such that the intersection of any two has a length of zero, breaking the Alpha Channel Invariant. Thus `LOAD 1` is the correct output.