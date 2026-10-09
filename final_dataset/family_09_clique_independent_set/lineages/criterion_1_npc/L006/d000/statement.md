# Problem A — Multiplex Assay Design

Time limit: 5 s   Memory limit: 256 MB

## Description

A genetics laboratory is designing a new multiplex assay to simultaneously test for multiple genetic markers. There are **n** candidate markers, numbered 1 through **n**.

Due to the chemical properties of the testing process, certain pairs of markers cannot be tested together because their primers interfere with each other. The laboratory has identified **m** such interfering pairs.

The goal is to select exactly **k** distinct markers to include in the assay. The selection must be completely free of interference: no two markers in the chosen set can be an interfering pair.

Determine if it is possible to design an assay with exactly **k** markers under these conditions, and if so, identify one such valid set.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the following **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a pair of markers that exhibit primer interference. No interfering pair is listed more than once.

## Output

If a valid assay containing exactly **k** markers exists, output `YES` on the first line. On the second line, output the **k** distinct marker numbers chosen for the assay, separated by spaces. Any valid selection is accepted.

If no such assay can be formed, output `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```

## Note

In Example 2, markers 1, 3, and 5 can be tested together because none of the pairs (1,3), (1,5), or (3,5) exhibit primer interference. 
In Example 1, it is impossible to find three markers where no two interfere with each other.
