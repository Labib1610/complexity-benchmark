# Facility Shift Allocation with Incompatibility Constraints

**Time limit:** 2 s  
**Memory limit:** 256 MB

A facility operates in three distinct operational shifts, numbered 1, 2, and 3. A total of $n$ staff members must each be assigned to exactly one shift. 

Certain pairs of staff members are mutually incompatible and cannot be assigned to the same shift. Your task is to determine whether there exists a valid allocation of shifts to all staff members such that no two incompatible staff members share the same shift. If such an allocation exists, find the one that produces the lexicographically smallest sequence of shift assignments.

## Input
The first line contains two integers $n$ and $m$, representing the total number of staff members and the total number of incompatibility relationships, respectively.
* The total headcount $n$ satisfies $1 \le n \le 40$, constrained by the facility's maximum total roster limit.
* The number of incompatibility relationships $m$ is non-negative and cannot exceed the total number of distinct two-person pairings, $\frac{n(n-1)}{2}$.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that staff member $u$ and staff member $v$ are incompatible.

## Output
If no valid shift assignment exists that satisfies all constraints, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the shift assigned to staff member $i$. If multiple valid shift assignments exist, output the sequence that is lexicographically smallest (compare $s_1$ first, then $s_2$, and so on).

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
