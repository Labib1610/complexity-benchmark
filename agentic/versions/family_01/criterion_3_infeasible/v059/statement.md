# Shift Certificate Audit

Time limit: 2 s   Memory limit: 256 MB

An industrial site schedules its staff across two distinct work shifts such that each staff member is placed into exactly one shift. Due to safety rules, specific pairs of staff members are prohibited from working during the same shift.

To demonstrate why two shifts are insufficient to satisfy all safety constraints, an auditor must find a group of three staff members who are all mutually prohibited from sharing a shift. Since each pair among these three staff members cannot be in the same shift, no two-shift setup can accommodate all three simultaneously.

If multiple such groups of three staff members exist, select the one that comes earliest in lexicographical order. Specifically, if the three staff IDs are arranged as $a < b < c$, choose the set that minimizes $a$ first, then $b$, and finally $c$.

## Input
The first line contains two space-separated integers $n$ and $m$. Here $n$ represents the total workforce count, bounded between a minimum team size of 3 and a facility capacity limit of 2000. The integer $m$ represents the total number of pairwise conflicts, which is at least 3 and does not exceed either 200,000 or the total possible number of distinct pairs among $n$ staff members.

The next $m$ lines each contain two space-separated integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that staff member $u$ and staff member $v$ cannot be assigned to the same shift. No conflict pair appears more than once in the input.

It is guaranteed that at least one such mutually conflicting group of three staff members exists.

## Output
Output a single line containing three space-separated integers $a$, $b$, and $c$ ($a < b < c$) representing the lexicographically smallest triple where all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are registered conflicts.

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
