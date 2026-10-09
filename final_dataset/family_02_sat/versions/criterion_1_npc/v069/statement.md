# Problem A — Mayoral Platform

Time limit: 2 s   Memory limit: 256 MB

## Description

A newly elected mayor is finalizing a legislative platform consisting of **n** distinct proposals. For each proposal, the mayor must make a firm decision: it will either be ENACTED or REJECTED. There is no middle ground, and no proposal can be left undecided.

To ensure a smooth term, the mayor must secure the backing of **m** powerful interest groups. Each interest group has submitted a list of exactly three demands regarding the platform. A demand specifies a particular proposal and the outcome the group desires for it (either ENACTED or REJECTED). 

An interest group is pragmatic: they will fully support the mayor as long as **at least one** of their three demands is met by the final platform. Meeting more than one demand for a group provides no additional benefit, but if the platform fails to meet any of a group's three demands, that group will organize a protest and block the mayor's agenda.

Different interest groups may care about the same proposals, sometimes with conflicting desires. The mayor must determine if there is a single, comprehensive platform (a decision of ENACTED or REJECTED for all **n** proposals) that avoids any protests by satisfying every interest group simultaneously.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
Each of the next m lines contains three non-zero signed integers d1 d2 d3,
with |di| ≤ n. A positive value represents a demand that the corresponding proposal is ENACTED, while a negative value represents a demand that it is REJECTED. At least one of the three stated demands must hold for each group.

## Output
If there is no way to form a platform that satisfies all interest groups, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}), where si is the state of proposal i (1 for ENACTED, 0 for REJECTED). Any valid platform configuration is accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each interest group always lists exactly three demands. The same proposal index may appear more than once in a group's list.
