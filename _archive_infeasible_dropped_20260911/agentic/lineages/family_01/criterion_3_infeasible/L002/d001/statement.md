# Conflict Resolution Certification

Time limit: 2 s
Memory limit: 256 MB

A manufacturing facility has a roster of $n$ technicians. Over time, there have been $m$ formal conflict reports logged. Each report involves exactly two technicians who refuse to operate on the same shift. The management originally intended to partition the staff into two distinct shifts, but the logged conflicts make any such two-shift partition impossible.

To formally document this failure, you must identify a minimal irreconcilable group. Specifically, you must find a group of exactly three technicians such that every possible pair within this group has a formal conflict report logged between them. 

Because the number of possible three-person groups is large, you must systematically search the conflict logs to find one where all three members mutually refuse to work together. If there are multiple such groups of three technicians, you must report the one that is ordered first according to technician ID. That is, compare the lowest ID of the groups, then the middle ID, and finally the highest ID, selecting the group with the smallest values.

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$), indicating the total number of technicians and the total number of conflict reports.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a pair of technicians who have filed a mutual conflict report. The order of these reports in the log is historical, and each specific pair of technicians is recorded at most once.
It is guaranteed that at least one irreconcilable group of exactly three technicians exists.

## Output
Output a single line containing three integers $a$, $b$, and $c$, ordered such that $a < b < c$, representing the IDs of the three technicians. Every pair among these three must have a conflict report. If multiple such groups exist, output the one that is lexicographically smallest.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```