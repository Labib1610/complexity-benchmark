# Hazardous Reagent Distribution

Time limit: 2 s   Memory limit: 256 MB

An industrial facility manages $n$ volatile chemical reagents, numbered $1$ through $n$. The facility operates three distinct storage units labeled $1$, $2$, and $3$. Every reagent must be assigned to precisely one storage unit.

Certain pairs of reagents react dangerously upon contact and must never be placed in the same storage unit. Additionally, safety regulations dictate that a distribution plan is compliant if and only if every reagent is assigned to one unit and no unit contains a reactive pair.

To minimize baseline operational costs, the facility manager seeks the assignment sequence $(s_1, s_2, \dots, s_n)$—where $s_i \in \{1, 2, 3\}$ represents the storage unit assigned to reagent $i$—that is lexicographically smallest. If no safe assignment exists that avoids placing reactive reagents together, the system must report that no compliant plan can be formed.

## Input
The first line contains two space-separated integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of reagents and the number of reactive reagent pairs, respectively.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that reagent $u$ and reagent $v$ react dangerously and cannot share a storage unit.

## Output
If no valid assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1 \ s_2 \ \dots \ s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the storage unit assigned to reagent $i$. If multiple valid assignments exist, output the lexicographically smallest sequence.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
