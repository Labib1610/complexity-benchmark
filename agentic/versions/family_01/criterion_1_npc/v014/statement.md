# Problem A — Tri-Phase Allocation

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant runs its daily operations in three consecutive phases, designated as 1, 2, and 3. The plant employs a roster of staff members. Due to interpersonal disputes, certain pairs of staff members are deemed incompatible and are strictly prohibited from working during the same operational phase.

Your task is to allocate each staff member to exactly one of the three phases in a way that respects all incompatibility rules. If no such allocation can be made, you must report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ — the number of staff members and the number of incompatible pairs. The facility has exactly 40 safety badges available, meaning the staff size $n$ is at least one but can never exceed the total badge count. The number of incompatible pairs $m$ is non-negative and is bounded above by the total number of distinct two-person combinations possible among the $n$ staff members.

The following $m$ lines each contain two integers $u$ and $v$ — a pair of staff members who are incompatible.

## Output
If there is no valid allocation, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $p_1, p_2, \dots, p_n$ (where each $p_i \in \{1, 2, 3\}$), representing the phase assigned to staff member $i$. If multiple valid allocations exist, output the one that is lexicographically smallest (comparing the phase of staff member 1 first, then staff member 2, and so forth).

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
