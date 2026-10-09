# Problem A — Focus Group Selection

Time limit: 5 s
Memory limit: 256 MB

## Description

A social network contains **n** users, identified by numbers from 1 to **n**, and **m** mutual friendship links. 

The platform administrators want to assemble a focus group of exactly **k** users to gather independent opinions. To ensure no bias, the focus group must be entirely disconnected: no two users in the group can be friends with each other. 

A natural strategy to build such a group is sequential elimination: find a user with the fewest friends, invite them to the group, and then disqualify all their friends from being selected. By repeating this, you ensure that no two invited users share a link. While this step-by-step filtering is fast and guarantees the group has no internal links, it may stop before reaching **k** users even if a valid group of size **k** is actually possible. 

Your task is to analyze the network and determine if *any* valid focus group of exactly **k** users exists, regardless of how it is found. If it does, you must output one such group.

## Input

The first line provides three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
The following **m** lines each contain two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a friendship link between user **u** and user **v**. Each mutual link is given exactly once.

## Output

If a focus group of exactly **k** completely disconnected users exists, output `YES` on the first line. On the second line, output the **k** distinct user identifiers that make up the group, separated by spaces. If multiple such groups exist, any valid group is acceptable.

If it is impossible to form a focus group of that size, output `NO`.

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
