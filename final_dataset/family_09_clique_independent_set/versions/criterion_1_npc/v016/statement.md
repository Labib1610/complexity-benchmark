# Problem A — Unassociated Panel

Time limit: 5 s   Memory limit: 256 MB

## Description

A digital platform has **n** members, identified by integers from 1 to **n**. There are **m** bilateral associations recorded on the platform, each linking two distinct members.

The platform administrators wish to assemble a special panel of exactly **k** members. To ensure diverse perspectives, this panel must be completely unassociated; that is, no two members chosen for the panel can have a bilateral association with each other.

Due to platform limits, it is guaranteed that no single member has more than 45 associations. Additionally, the total number of associations **m** across the entire platform will never exceed 1035.

Your task is to determine if an unassociated panel of exactly **k** members can be formed, and if so, to identify its members.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the following **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a bilateral association between member **u** and member **v**. No association is listed more than once.

## Output

If such a panel can be assembled, print `YES` on the first line. On the second line, print the **k** distinct member identifiers that make up the panel, separated by spaces. Any valid panel where no two members share an association is accepted.

If no such panel exists, print `NO`.

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
