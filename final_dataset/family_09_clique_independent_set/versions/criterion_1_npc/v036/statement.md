# Problem A — Unbiased Panel Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

A market research firm is assembling a focus group from a pool of **n** registered participants (numbered 1 through **n**). The firm possesses records of **m** existing relationships, each indicating that two specific participants are already acquainted.

To ensure unbiased feedback, the firm requires a panel where absolutely no participants have prior contact with one another. The goal is to determine if it is possible to select exactly **k** participants such that no two individuals in the chosen panel appear together in any of the relationship records. If such a panel can be formed, you must provide one valid selection of participants.

## Input

The first line provides three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n), representing the number of participants, the number of relationship records, and the required panel size.
The following **m** lines each contain two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), identifying a pair of participants who are acquainted. A specific pair is never listed more than once.

## Output

If a panel meeting the criteria can be formed, output `YES` on the first line. On the second line, output exactly **k** distinct participant identifiers that make up the panel, separated by spaces. If multiple valid panels exist, any one is acceptable.

If it is impossible to form such a panel, output `NO`.

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

In Example 2, participants 1, 3, and 5 have no prior contact with each other according to the records, fulfilling the requirement for a panel of size 3. In Example 1, it is impossible to find 3 participants who are all mutually unacquainted.
