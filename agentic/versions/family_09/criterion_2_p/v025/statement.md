# Orbital Assembly Tolerances

Time limit: 2 s   Memory limit: 256 MB

## Description

You are tasked with selecting exactly **k** subsystem modules for a new orbital station. There are **n** candidate modules available, numbered 1 to **n**.

Due to electromagnetic interference, certain pairs of modules are incompatible and absolutely cannot be installed on the same station. You are given a list of **m** such incompatible pairs.

The modules were sourced from two different manufacturing consortiums. Because internal standards within each consortium are consistent, incompatibilities only ever arise between a module from the first consortium and a module from the second consortium. Two modules from the same consortium are never incompatible with each other. The consortium origins of the modules are classified and not provided to you, but they can be logically deduced from the interference data.

Furthermore, the interference data is guaranteed to satisfy the following structural constraints:
- There exists a division of the **n** modules into the two consortiums (of sizes $n_1$ and $n_2$) such that $n_1 \times n_2 \ge m$.
- For any arbitrary subset of $S$ modules, the number of incompatibilities strictly between modules in that subset never exceeds $\lfloor S^2 / 4 \rfloor$.

Your objective is to determine if it is possible to select a set of exactly **k** modules such that no two selected modules are incompatible. If such a set exists, you must output one valid selection.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
The next **m** lines each contain two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing an incompatible pair of modules. No pair is listed more than once. The input is guaranteed to be consistent with the two-consortium structure described above.

## Output

If a valid set of exactly **k** modules exists, print `YES` on the first line. On the second line, print **k** distinct integers representing the module numbers in your selection, separated by spaces. Any valid selection of exactly **k** mutually compatible modules will be accepted.

If no such selection is possible, print `NO`.

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
