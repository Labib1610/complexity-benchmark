# Problem A — Stable Formulation

Time limit: 5 s   Memory limit: 256 MB

## Description

A pharmaceutical company is developing a new drug and has a catalog of **n** available active compounds, numbered 1 to **n**. Extensive testing has identified **m** specific pairs of compounds that exhibit adverse reactions when combined.

To achieve the desired therapeutic effect, the new drug must be formulated using exactly **k** distinct compounds. However, safety regulations mandate that the final formulation must be completely stable: it cannot contain any two compounds that have an adverse reaction with each other.

Determine if it is possible to select exactly **k** compounds to create a stable formulation, and if so, identify one such valid selection.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ **n** ≤ 46, 0 ≤ **m** ≤ **n**·(**n**−1)/2, 1 ≤ **k** ≤ **n**).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), representing a pair of compounds that have an adverse reaction. No pair is listed more than once.

## Output

If a stable formulation of **k** compounds is possible, output `YES` on the first line. On the second line, output the **k** distinct compound numbers chosen for the formulation, separated by spaces. If multiple stable formulations exist, any valid selection is accepted.

If no such formulation can be created, output `NO`.

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
