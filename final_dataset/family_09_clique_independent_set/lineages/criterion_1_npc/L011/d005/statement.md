# Problem A — Panel Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

A social network tracks **n** member profiles, identified by numbers from 1 to **n**. The system has recorded **m** bilateral interaction events, each representing an exchange between two distinct members. 
For each member $i$, let $W_i$ be the total number of recorded interaction events they participated in.

A research initiative requires selecting exactly **k** members to form a focus panel. The remaining $n-k$ members will form the control group. To ensure unbiased cross-group metrics, the selection must satisfy a specific structural balance condition.

First, calculate the **Expected Cross-Load (ECL)** of the proposed split:
$$ECL = 5m + 2 \sum_{i \in \text{Panel}} W_i + 3 \sum_{j \in \text{Control}} W_j$$

Next, calculate the **Actual Cross-Load (ACL)** by examining every recorded interaction event:
- If the event is between a Panel member and a Control member, it adds 10 to the ACL.
- If the event is between two Panel members, it adds 5 to the ACL.
- If the event is between two Control members, it adds 11 to the ACL.

The focus panel is considered valid if and only if it contains exactly $k$ members and its $ACL$ exactly equals its $ECL$.

Your objective is to evaluate whether it is possible to construct a valid focus panel under these constraints. If such a panel can be formed, you must also provide a list of its members.

## Input

The first line provides three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Following this are **m** lines, each containing two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v). These indicate an interaction event between member **u** and member **v**. Each interaction event is listed at most once.

## Output

If a valid focus panel of exactly **k** members can be formed, output `YES` on the first line. On the next line, output the **k** distinct member numbers that constitute the panel, separated by spaces. Any valid panel will be accepted if more than one exists.

If forming such a panel is impossible, output `NO`.

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