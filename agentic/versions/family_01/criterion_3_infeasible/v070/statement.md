# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The facility operates strictly on a two-shift system. The scheduling system maintains a database of personnel restrictions, tracking pairs of employees who have filed grievances against one another. Any two employees with a grievance record cannot be assigned to the same operational shift.

Currently, the scheduling system has flagged the set of employee grievances as fundamentally unresolvable. To formally document this scheduling failure, the system requires a specific type of evidence. 

Your task is to identify a triad of employees such that every possible pair formed from these three individuals has a corresponding grievance record. The existence of such a triad logically demonstrates that two shifts are insufficient, as no two of the three employees can share a shift.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)), representing the number of employees and the number of grievance records. Employee IDs are numbered from 1 to n.
Each of the following m lines contains two integers u and v — a pair of employees who cannot be assigned to the same shift.
It is guaranteed that at least one such triad exists.

## Output
Print three integers a, b, and c on a single line, separated by spaces, with a < b < c, such that the pairs a–b, a–c, and b–c all appear in the grievance records. If there are multiple qualifying triads, output the one that is lexicographically smallest (the one with the smallest a; in case of ties, the smallest b; and then the smallest c).

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
