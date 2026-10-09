# Problem A — Panel Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

A social platform maintains **n** member profiles (numbered 1 to **n**). Over time, the platform has logged **m** bilateral interaction events. Each event involves exactly two distinct members.

A research study aims to divide the members into two distinct categories: a focus panel containing exactly **k** members, and a control group containing the remaining **n** - **k** members. This categorization is considered valid only if it satisfies the following requirement:
- For every logged interaction event, at least one of the two members involved must be assigned to the control group.

Determine whether it is possible to successfully form a valid focus panel of exactly **k** members, and if so, report the members assigned to the panel.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing an interaction event between member **u** and member **v**. No interaction event is listed twice.

## Output

If it is possible to successfully form a valid focus panel of **k** members, print `YES` on the first line. On the second line, print the **k** distinct member numbers that make up the panel, separated by spaces. If multiple valid panels exist, any one is accepted.

If no such panel can be formed, print `NO`.

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