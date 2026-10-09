# Problem A — Account Panel

Time limit: 5 s   Memory limit: 256 MB

## Description

A digital platform has **n** accounts (numbered 1 to n) and **m** historical interaction records. Each record indicates that two specific accounts have interacted directly.

You need to assemble an oversight panel consisting of exactly **k** accounts. To ensure unbiased perspectives, the panel must be chosen such that no two accounts on the panel have ever had a direct interaction.

Given the target size **k**, determine if such a panel can be formed, and if so, list the accounts that comprise it.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing an interaction record between account **u** and account **v**. No pair of accounts will have more than one interaction record listed.

## Output

If a valid panel of exactly **k** accounts exists, output `YES` on the first line. On the second line, output **k** distinct account numbers that form the panel, separated by spaces. If there are multiple valid selections, any one of them is acceptable.

If no such panel can be formed, output `NO`.

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
