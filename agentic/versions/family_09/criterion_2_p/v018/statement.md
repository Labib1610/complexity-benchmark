# Problem B — Platform Demographics

Time limit: 2 s   Memory limit: 256 MB

## Description

A digital platform hosts **n** accounts, labeled 1 through **n**, with **m** mutual contacts established between certain pairs of accounts.

The user base inherently divides into exactly two separate demographics. Due to platform restrictions, contacts can only be established across these demographics; an account will never have a contact with another account from its own demographic. The specific demographic identity of each account is not explicitly provided in the data, but you may deduce it from the contacts.

Your system is given a parameter **k**. You must determine if it is possible to select exactly **k** accounts such that there is absolutely no mutual contact between any two accounts in your selection. If such a selection is possible, you must also provide one valid example of it.

## Input

The first line provides three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
The next **m** lines each contain two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a mutual contact between account **u** and account **v**. No contact is given more than once. It is guaranteed that the contacts strictly adhere to the demographic rule described above.

## Output

If it is possible to choose exactly **k** accounts without any mutual contacts among them, print `YES` on the first line. On the second line, output the **k** distinct account identifiers of your selection, separated by spaces. Any valid selection will be accepted.

If no such selection can be made, print `NO`.

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
