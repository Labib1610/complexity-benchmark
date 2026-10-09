# Problem A — Clinical Trial Design

Time limit: 5 s   Memory limit: 256 MB

## Description

A pharmaceutical company is designing a study consisting of **k** concurrent trial arms. The study involves **k** patient demographics, **k** experimental drug formulations, and **k** monitoring facilities, each numbered 1 through **k**. A single trial arm operates by assigning exactly one demographic to receive one formulation at one facility.

Due to regulatory safety protocols, only specific combinations of demographic, formulation, and facility have been medically cleared for testing. You are given the complete list of these cleared combinations.

The study must be structured using exactly **k** cleared combinations so that every demographic is tested, every formulation is evaluated, and every facility is utilized. Furthermore, each demographic, formulation, and facility must be assigned to exactly one trial arm to prevent overlapping data. Determine if a valid study design is possible, and if so, output the selected trial arms.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the group size and the number of cleared combinations.
Each of the next **t** lines contains three integers **d**, **f**, **m** (1 ≤ d, f, m ≤ k), representing a cleared combination of demographic **d**, formulation **f**, and facility **m**. No combination is listed more than once.

## Output

If a valid study design exists, print `YES` on the first line, then print **k** lines, each containing the three integers `d f m` of one chosen trial arm. Any selection in which every demographic, formulation, and facility is used exactly once is accepted; the trial arms may be printed in any order.

If no valid design exists, print `NO`.

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

In Example 2, both cleared combinations use formulation 1, so formulation 2 can never be evaluated.
