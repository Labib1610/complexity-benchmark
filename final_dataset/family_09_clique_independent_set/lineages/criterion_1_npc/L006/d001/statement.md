# Problem A — Multiplex Assay Design

Time limit: 5 s   Memory limit: 256 MB

## Description

A genetics laboratory needs to formulate a new multiplex assay by selecting a specific number of genetic markers. The pool of available markers contains **n** candidates, which are identified by integers from 1 up to **n**.

Because of the chemical dynamics during testing, certain pairs of these markers undergo primer interference when combined. The research team has cataloged **m** such incompatible pairs.

Your objective is to determine whether it is feasible to assemble an assay that incorporates exactly **k** distinct markers such that no primer interference occurs. This means that no two markers in your chosen combination can be among the **m** incompatible pairs.

## Input

The initial line provides three integers: **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Following this, there are **m** lines. Each line specifies two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), indicating a pair of markers that interfere with one another. Each incompatible pair is given at most once.

## Output

When a successful configuration of exactly **k** markers is possible, print `YES` on the first line. On the next line, print the **k** distinct identifiers of the markers making up your configuration, separated by spaces. The automated evaluation system will verify that your submitted group satisfies all non-interference conditions.

When no such configuration is possible, print `NO`.

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