# Conflict Resolution Certification

Time limit: 2 s
Memory limit: 256 MB

A manufacturing facility has a roster of $n$ technicians. Over time, there have been $m$ formal conflict reports logged. Each report involves exactly two technicians who refuse to operate on the same shift. The management intended to divide the staff into two shifts, but the logged conflicts make this impossible.

To formally document this failure, you must locate a specific obstruction: a trio of distinct technicians where each technician in the trio has a logged conflict with the other two technicians in the trio.

Because the number of possible three-person combinations is large, you must systematically search the conflict logs to find one. If there are multiple qualifying trios of technicians, you must report the trio that is ordered first according to technician ID. That is, when each trio's IDs are written in increasing numerical order, you must select the one that is lexicographically smallest (compare the lowest ID of the trios, then the middle ID, and finally the highest ID, selecting the trio with the smallest sequence of values).

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$), indicating the total number of technicians and the total number of conflict reports.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a pair of technicians who have filed a mutual conflict report. It is guaranteed that at least one such trio of distinct technicians exists.

## Output
Output a single line containing three integers $a$, $b$, and $c$, ordered such that $a < b < c$, representing the IDs of the three technicians in the chosen trio. If multiple such trios exist, output the one that is lexicographically smallest.

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