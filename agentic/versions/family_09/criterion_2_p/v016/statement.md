# Harmonious Delegation

Time limit: 2 s   Memory limit: 256 MB

## Description

An organization has **n** members (numbered 1 to **n**) and **m** known interpersonal conflicts. Each conflict involves exactly two members who cannot work together.

The organization's structure ensures that members can be divided into two distinct divisions such that every conflict occurs between a member of one division and a member of the other. There are zero conflicts between any two members who belong to the same division. (The division assignments are not explicitly provided to you; they must be deduced from the conflicts).

You must form a project delegation of exactly **k** members. The delegation must be entirely harmonious, meaning no two members selected for the delegation have a conflict with each other.

To assist with processing, the following properties are guaranteed to hold for the organization:
- The sum of the number of conflicts each member is involved in will never exceed 800,000.
- The number of members who are involved in an odd number of conflicts is always an even number.

Given the target size **k**, determine if a harmonious delegation of exactly **k** members can be formed, and if so, output one valid selection.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ **n** ≤ 100000, 0 ≤ **m** ≤ 400000, 1 ≤ **k** ≤ **n**).
The following **m** lines each contain two integers **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), denoting a conflict between member **u** and member **v**. No conflict is listed more than once, and the input strictly adheres to the two-division structure described above.

## Output

If a harmonious delegation of **k** members is possible, output `YES` on the first line. On the second line, output **k** distinct member numbers that form this delegation, separated by spaces. Any valid harmonious delegation will be accepted.
If no such delegation is possible, output `NO`.

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
