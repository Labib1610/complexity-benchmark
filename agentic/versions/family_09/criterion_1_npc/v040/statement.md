# Problem A — Audit Committee Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

As part of a routine security compliance audit, a platform's user base is evaluated. The full audit process involves three phases:

First, the system aggregates the communication logs to identify all pairs of accounts that have established a direct channel. 

Second, an audit committee of exactly **k** accounts must be formed. To ensure unbiased reporting and prevent collusion, the committee must be strictly decentralized. Specifically, you must select exactly **k** accounts such that no direct channel exists between any two accounts in your selection.

Finally, the selected accounts will be automatically provisioned with cryptographic tokens to independently verify the platform's integrity logs.

Your task is to implement the second phase: given the total number of accounts **n** (numbered 1 to **n**), the list of **m** direct channels identified in the first phase, and the required committee size **k**, determine if a valid committee can be formed, and report one if it can.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a direct channel between account **u** and account **v**. No channel is listed more than once.

## Output

If a valid committee of **k** accounts is possible, print `YES` on the first line. On the second line, print the **k** distinct account identifiers that make up the committee, separated by spaces. If multiple valid committees exist, you may output any of them.

If it is impossible to form such a committee, print `NO`.

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
