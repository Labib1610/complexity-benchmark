# Workforce Group Partitioning

Time limit: 1 s   Memory limit: 256 MB

A manufacturing facility splits its daily operations into two distinct time slots, designated Slot 1 and Slot 2. A safety audit has compiled a list of operational conflicts between pairs of personnel. Any two personnel subject to a conflict cannot be scheduled in the same time slot.

There are $n$ personnel, indexed from $1$ to $n$. Your task is to assign each person to either Slot 1 or Slot 2 so that no conflict is violated.

The facility's shift management system can handle a workforce of up to two hundred thousand personnel ($1 \le n \le 2 \cdot 10^5$), and can process at most two hundred thousand conflict pairs ($0 \le m \le 2 \cdot 10^5$).

To guarantee deterministic processing for downstream reporting, if there are multiple valid slot assignments, you must pick the one that yields the lexicographically smallest sequence $s_1, s_2, \dots, s_n$, where $s_i \in \{1, 2\}$ is the slot assigned to person $i$. If no valid assignment exists, report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of personnel and the number of conflict pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), stating that person $u$ and person $v$ cannot be assigned to the same time slot.

## Output
If no conflict-free assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid slot assignment.

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
