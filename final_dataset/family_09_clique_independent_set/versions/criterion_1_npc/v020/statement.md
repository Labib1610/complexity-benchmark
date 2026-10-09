# Problem A — Hazardous Cargo

Time limit: 5 s   Memory limit: 256 MB

## Description

A freight company needs to transport a selection of **n** different types of hazardous materials, numbered 1 through **n**.

Safety regulations dictate that certain pairs of materials react dangerously when in close proximity. There are **m** documented dangerous pairs that must never be stored in the same cargo hold. 

A specialized containment hold is being prepared to transport exactly **k** distinct types of materials. To ensure the safety of the vessel, the chosen materials must be completely stable together—meaning no two materials in the selection can form a dangerous pair.

Given the target **k** and the list of dangerous pairs, determine whether a safe selection of exactly **k** materials exists, and if so, report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a dangerous pair of materials. No pair is listed twice.

## Output

If a safe selection of exactly **k** materials exists, print `YES` on the first line. On the second line, print the **k** distinct material numbers forming this selection, separated by spaces. If multiple safe selections exist, any of them will be accepted.

If no such selection is possible, print `NO`.

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

In Example 2, materials 1, 3, and 5 can be safely stored together because none of the pairs (1, 3), (1, 5), or (3, 5) are listed as dangerous. 
In Example 1, it is impossible to choose 3 materials without including at least one dangerous pair.
