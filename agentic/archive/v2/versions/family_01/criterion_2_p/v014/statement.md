# Day and Night

**Time limit:** 1 s  
**Memory limit:** 256 MB

A facility operates across two distinct work periods, labeled 1 and 2. A total of $n$ staff members, indexed from $1$ to $n$, must each be assigned to exactly one period. Certain pairs of staff members are incompatible and cannot work during the same period.

Your task is to determine whether a valid partition of staff members into these two work periods exists such that no incompatible pair is assigned to the same period. If multiple valid schedule assignments exist, you must output the one that is lexicographically smallest (that is, the sequence $s_1, s_2, \dots, s_n$ that minimizes $s_1$, then $s_2$, and so on).

## Input
The first line contains two integers $n$ and $m$. Here $n$ represents the total headcount of staff members, which is at least 1 and capped at the facility's maximum roster capacity of two hundred thousand ($1 \le n \le 2\cdot 10^5$). The integer $m$ represents the total number of conflict pairs, bounded between 0 and two hundred thousand ($0 \le m \le 2\cdot 10^5$).

Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), denoting an incompatibility constraint between staff member $u$ and staff member $v$.

## Output
If no schedule can satisfy all constraints, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), specifying the lexicographically smallest valid assignment of work periods for staff members $1$ through $n$.

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
