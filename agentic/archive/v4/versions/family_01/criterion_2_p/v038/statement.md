# Roster Allocation

Time limit: 1 s   Memory limit: 256 MB

An industrial facility schedules $n$ staff members, indexed $1$ through $n$, into two non-overlapping duty periods represented by the values $1$ and $2$. You are given $m$ pairs of staff members who are mutually incompatible and therefore cannot be assigned to the same duty period.

Your task is to assign each staff member $i$ a duty period designation $s_i \in \{1, 2\}$ such that for every mutually incompatible pair, their assigned duty period designations are different.

Furthermore, to maintain administrative consistency:
- Each staff member must receive exactly one duty period designation.
- The overall roster must satisfy all $m$ mutual incompatibility rules simultaneously.

If a valid configuration exists, find the sequence $(s_1, s_2, \dots, s_n)$ that is lexicographically smallest. Otherwise, determine that no valid schedule can be formed.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$) — the number of staff members and the number of mutual incompatibility rules.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — indicating that staff member $u$ and staff member $v$ are mutually incompatible.

## Output
If no valid allocation exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid duty period sequence.

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
