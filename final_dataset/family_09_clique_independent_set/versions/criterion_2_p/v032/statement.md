# Problem B — Harmonious Panel Selection

Time limit: 2 s   Memory limit: 256 MB

## Description

A digital platform has **n** users (numbered 1 to **n**) and **m** logged conflicts. Each conflict indicates that two specific users cannot work together. 

You are tasked with selecting exactly **k** users to form a special advisory panel. To ensure the panel is perfectly harmonious, no two users chosen for the panel can have a logged conflict between them. Since **n** can be up to 100,000, evaluating every potential group of size **k** is impossible due to the sheer number of combinations. You must determine if at least one valid panel of the requested size exists.

Despite the vast search space, the conflict network possesses a strict underlying structure. Every user inherently aligns with one of two unrecorded design preferences (e.g., "dark mode" or "light mode"). Due to the nature of the platform, a conflict only ever arises between two users with differing design preferences. There are absolutely no conflicts between any two users who share the same preference. (Note: The preference of each user is not provided to you, but the network is guaranteed to follow this rule).

Given the target size **k**, determine whether a harmonious panel of exactly **k** users can be assembled, and if so, identify one such panel.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the following **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a logged conflict between user **u** and user **v**. No conflict is listed more than once. It is guaranteed that the conflicts strictly adhere to the structural rule described above.

## Output

If a harmonious panel of exactly **k** users exists, print `YES` on the first line. On the second line, print **k** distinct user numbers that form the panel, separated by spaces. If there are multiple valid panels, any one in which no two users conflict is acceptable.

If no such panel can be formed, print `NO`.

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
