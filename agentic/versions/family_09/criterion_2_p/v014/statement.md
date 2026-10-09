# Problem B — Disconnected Cohort (Polarized Network)

Time limit: 2 s   Memory limit: 256 MB

## Description

A social platform hosts registered accounts and bidirectional interactions. The userbase is completely polarized into two hidden factions. Because of this strict division, every recorded interaction occurs exclusively between an account in one faction and an account in the other. Interactions between accounts within the same faction are non-existent.

Your goal is to assemble a "disconnected cohort" of a specific size. A cohort is considered disconnected if no two accounts within it share an interaction.

Given the interaction logs, you must determine if it is possible to select exactly the target number of accounts such that they form a disconnected cohort. The faction memberships are not provided, but the interaction rules guarantee they exist.

## Input

The first line of the system log provides three integers: the registered headcount $n$, the total number of bidirectional interactions $m$, and the required cohort size $k$.
- The headcount $n$ is strictly positive. The platform's license restricts the maximum headcount to exactly $10^5$.
- The interaction count $m$ can be zero. The system's total storage capacity for interactions is exactly four times the maximum licensed headcount, which serves as the absolute upper limit for $m$.
- The cohort size $k$ is strictly positive and naturally cannot exceed the registered headcount $n$.

The following $m$ lines each contain two distinct account identifiers $u$ and $v$ (ranging from $1$ to $n$), representing an interaction between them. No interaction is duplicated in the logs. It is guaranteed that the interactions strictly follow the polarized faction structure described above.

## Output

If a disconnected cohort of exactly $k$ accounts exists, output `YES` on the first line. On the second line, output $k$ distinct account identifiers that make up this cohort, separated by spaces. If multiple valid cohorts exist, any of them will be accepted.

If no such cohort can be formed, output `NO`.

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

## Note

In Example 1, accounts 1 and 2 belong to the same faction and thus have no interaction. In Example 3, the largest possible disconnected cohort contains only 2 accounts, making a cohort of 3 impossible.
