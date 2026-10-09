# Problem B — Stable Shipment

Time limit: 2 s   Memory limit: 256 MB

## Description

A laboratory needs to prepare a shipment containing exactly **k** different chemical substances, chosen from an inventory of **n** available substances (numbered 1 through n).

There are **m** known reactive pairs among the inventory. If two substances form a reactive pair, they are incompatible and cannot be included together in the same shipment.

The substances in the inventory inherently belong to one of two fundamental chemical categories (for instance, electron donors and electron acceptors). Because of this underlying chemistry, a reaction is only possible when a substance from the first category is mixed with a substance from the second category. Two substances from the same category will never react with each other. (The category labels are missing from the laboratory's database, but you may deduce them from the reaction data).

A shipment is considered **stable** if no two substances in it form a reactive pair.

Given the target size **k**, determine whether a stable shipment of exactly **k** substances can be formed, and if so, provide a valid selection.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), indicating that substance **u** and substance **v** form a reactive pair. No pair is listed more than once, and the reaction data is guaranteed to adhere to the two-category rule described above (every reaction involves one substance from each category).

## Output

If a stable shipment of exactly **k** substances exists, output `YES` on the first line. On the second line, output **k** distinct substance numbers that form a stable shipment, separated by spaces. If there are multiple valid selections, any of them will be accepted.

If no such shipment can be formed, output `NO`.

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
