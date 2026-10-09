# Problem A — Secure Audit Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description

A financial institution has **n** accounts, numbered 1 through **n**. The auditing team must select exactly **k** distinct accounts to audit today.

The institution's database contains **m** reconciliation channels. Each channel bridges exactly two specific accounts. 
To prevent database corruption during the audit, a strict safety protocol must be followed: for every reconciliation channel, at least one of its two bridged accounts must be excluded from today's audit. If any channel has both of its bridged accounts selected for the audit, the system will deadlock.

Given the **n** accounts and the configurations of the **m** reconciliation channels, determine whether it is possible to select exactly **k** accounts for a safe audit. If a safe configuration is possible, you must provide one valid selection of accounts.

## Input

The first line of the input contains three integers **n**, **m**, and **k** (1 ≤ **n** ≤ 46, 0 ≤ **m** ≤ **n**·(**n**−1)/2, 1 ≤ **k** ≤ **n**).
The next **m** lines each contain two integers **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), representing the two accounts bridged by a specific reconciliation channel.
The order of the two accounts on a line does not matter, and no channel's pair of accounts is listed more than once.

## Output

If a safe audit of exactly **k** accounts can be configured, print `YES` on the first line. On the second line, print **k** distinct integers representing the account numbers to audit, separated by spaces. If there are multiple valid selections, any one will be accepted.

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