# Problem A — Unbiased Focus Group

Time limit: 5 s   Memory limit: 256 MB

## Description

A professional networking platform maintains a registry of its members and their established contacts. An established contact indicates that two members have previously interacted on the platform.

To conduct an unbiased study, the platform administrators need to assemble a focus group of exactly **k** members. To prevent any shared biases, the focus group must be formed such that absolutely no established contacts exist between any two members selected for the group.

You are given the target size **k**. Your task is to determine whether it is possible to form this focus group, and if so, to identify the members who should be selected.

## Input

The first line contains three integers: the total headcount of members **n**, the total count of established contacts **m**, and the target focus group size **k**.

The headcount **n** ranges from a single individual up to the platform's strict maximum server capacity of 46 profiles.
The count of contacts **m** ranges from zero up to the theoretical maximum where every member has an established contact with every other member.
The target size **k** ranges from one up to the total headcount.

Each of the following **m** lines contains two distinct integers **u** and **v**. These represent the ID numbers of two members who share an established contact. Member IDs are assigned sequentially starting from 1 up to the total headcount. No established contact is listed more than once.

## Output

If a focus group of exactly **k** members meeting the criteria can be formed, print `YES` on the first line. On the second line, print the **k** distinct member ID numbers that make up this group, separated by spaces. If multiple valid groups exist, any of them is accepted.

If no such group can be formed, print `NO`.

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
