# Vault Assignment for Chemical Storage

Time limit: 1 s   Memory limit: 256 MB

A chemical processing plant manages $N$ hazardous compounds, numbered $1$ through $N$. To safely store these materials, the facility operates two separate containment units: Vault 1 and Vault 2. Every compound must be placed into exactly one vault.

Certain pairs of compounds are mutually volatile and cannot be stored together. If two compounds form a volatile pair, they must be assigned to different containment units (one in Vault 1 and the other in Vault 2).

You are given the list of all volatile pairs. Determine whether it is possible to assign every compound to a vault without placing any volatile pair in the same unit. If such an assignment exists, find the assignment sequence $s_1, s_2, \dots, s_N$ (where $s_i \in \{1, 2\}$ indicates the vault number for compound $i$) that is lexicographically smallest. If no valid assignment can satisfy all conditions, output `NO`.

## Input
The first line contains two integers $N$ and $M$ ($1 \le N \le 200\,000$, $0 \le M \le 200\,000$), representing the total number of compounds and the number of volatile pairs, respectively.

The following $M$ lines each contain two space-separated integers $u$ and $v$ ($1 \le u, v \le N$, $u \neq v$), indicating that compound $u$ and compound $v$ form a volatile pair.

## Output
If no safe assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $N$ space-separated integers $s_1, s_2, \dots, s_N$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid vault assignment sequence.

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
