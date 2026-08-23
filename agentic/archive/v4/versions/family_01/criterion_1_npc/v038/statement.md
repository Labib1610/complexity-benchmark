# Schedule Compatibility Assignment

Time limit: 2 s   Memory limit: 256 MB

A facility schedules $n$ personnel members, indexed from $1$ to $n$. There are $m$ pairwise incompatibility constraints; each constraint specifies two personnel members who cannot be assigned to the same operational block.

There are 3 available operational blocks, designated by the integer identifiers 1, 2, and 3. Each personnel member must be allocated to exactly one operational block. Consequently, the sum of all assigned block identifiers $\sum_{i=1}^n s_i$ cannot exceed $3n$, a condition that holds for every valid assignment.

Find an allocation of block identifiers $s_1, s_2, \dots, s_n \in \{1, 2, 3\}$ for all personnel such that no incompatible pair shares the same block identifier. If multiple valid allocations exist, select the one that produces the lexicographically smallest sequence $(s_1, s_2, \dots, s_n)$. If no valid allocation is possible, report this outcome.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of personnel members and the number of incompatibility pairs, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that personnel $u$ and personnel $v$ are incompatible.

## Output
If no valid allocation exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$, where $s_i \in \{1, 2, 3\}$ is the operational block assigned to personnel $i$. Output the lexicographically smallest sequence among all valid assignments.

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
