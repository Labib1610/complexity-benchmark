# Conflict Resolution Certification

## Time and Memory Limits
Time limit: 2 s
Memory limit: 256 MB

## Description
A manufacturing facility has a roster of $n$ technicians. Over time, there have been $m$ formal grievances logged. Each report is a log entry stating that technician $u$ has filed a grievance against technician $v$. 

The management intended to divide the staff into two shifts, but the logged grievances make this impossible. To formally document this scheduling failure, you must locate a specific obstruction: a completely fractured triad. 

A triad is a group of exactly three distinct technicians. A triad is considered completely fractured if, for every technician within that triad, they appear in at least one log entry (either as the filer or as the receiver of the grievance) with each of the other two technicians in the triad. 

Because the number of possible three-person combinations is large, you must systematically search the grievance logs to find one. If there are multiple completely fractured triads, you must report the triad that is ordered first according to technician ID. That is, when each triad's IDs are written in increasing numerical order, you must select the one that is lexicographically smallest (compare the lowest ID of the triads, then the middle ID, and finally the highest ID, selecting the triad with the smallest sequence of values).

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$), indicating the total number of technicians and the total number of grievance reports.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a log entry where technician $u$ filed a grievance against technician $v$. It is guaranteed that at least one completely fractured triad exists.

## Output
Output a single line containing three integers $a$, $b$, and $c$, ordered such that $a < b < c$, representing the IDs of the three technicians in the chosen triad. If multiple such triads exist, output the one that is lexicographically smallest.

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