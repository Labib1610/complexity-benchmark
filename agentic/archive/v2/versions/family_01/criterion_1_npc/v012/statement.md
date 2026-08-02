# Problem A — Schedule Slot Allocation

Time limit: 2 s   Memory limit: 256 MB

A facility manages $n$ personnel, numbered 1 through $n$. Every individual must be assigned to work during exactly one of three available daily time slots, denoted 1, 2, and 3.

Certain pairs of individuals have mutual exclusion restrictions that forbid them from being scheduled in the same time slot. Your task is to compute a slot assignment for all personnel such that no restriction is violated, or determine that no such schedule is possible. If multiple valid assignments exist, you must choose the one that forms the lexicographically smallest sequence of slot numbers when ordered from person 1 to person $n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$), representing the number of personnel and the number of mutual exclusion restrictions, respectively.
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that person $u$ and person $v$ cannot share the same time slot.

## Output
If it is impossible to assign every person to a time slot without violating any restriction, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1 \ s_2 \ \dots \ s_n$, where $s_i \in \{1, 2, 3\}$ denotes the time slot assigned to person $i$. If there are multiple valid sequences, print the lexicographically smallest one (that is, compare $s_1$ first, then $s_2$, and so on).

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
