# Problem B — Dual Isolation Protocol

Time limit: 1 s   Memory limit: 256 MB

A laboratory manages $n$ sensitive chemical compounds, numbered $1$ to $n$. Certain pairs of compounds undergo hazardous reactions if stored together in the same containment unit. There are $m$ such reactive pairs recorded in the system logs.

The facility operates exactly two containment units, designated as unit $1$ and unit $2$.

To ensure safety, every compound must be placed into one of the two units such that no two compounds that form a reactive pair reside in the same unit. That is, for every reactive pair $(u, v)$, compound $u$ and compound $v$ must be stored in different units.

Your task is to determine whether a safe placement exists. If it is possible, output `YES` followed by the unit assignment sequence $s_1, s_2, \dots, s_n$ (where $s_i \in \{1, 2\}$ represents the unit assigned to compound $i$). If several valid assignments exist, output the one that is lexicographically smallest. If no valid placement can satisfy all safety requirements, output `NO`.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a pair of compounds that cannot share a unit.

## Output
If no valid placement exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid unit assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
