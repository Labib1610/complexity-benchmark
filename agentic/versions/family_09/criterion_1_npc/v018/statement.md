# Problem A — Focus Panel Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

An online platform consists of **n** registered accounts, numbered 1 through **n**. The platform's database contains records of **m** mutual interactions, where each record links two distinct accounts.

When selecting participants for a focus panel, the organizers enforce a strict isolation rule to prevent biased feedback. Specifically, if any two accounts have a recorded interaction between them, they cannot both be chosen for the same panel. A panel is only considered valid if it strictly adheres to this condition—meaning absolutely no recorded interactions exist between any pair of the selected accounts.

The organizers have a target size in mind for an upcoming study. They must assemble a valid panel containing exactly **k** accounts. Decide whether such a panel can be constructed, and if it can, identify the accounts that form it.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), indicating a recorded interaction between account **u** and account **v**. No interaction is listed twice.

## Output

If a valid panel of exactly **k** accounts exists, print `YES` on the first line. On the second line, print the **k** distinct account numbers chosen, separated by spaces. Any valid selection of **k** accounts is accepted.

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

## Note

In Example 2, accounts 1, 3, and 5 have no recorded interactions among them. In Example 1, it is impossible to find three accounts such that no two of them have interacted.
