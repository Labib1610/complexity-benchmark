# Problem A — Tertiary Production Roster

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant operates three distinct production phases, designated by the codes 1, 2, and 3. The plant employs $n$ technicians, each assigned a unique identification number from 1 to $n$. 

Due to past operational incidents, certain pairs of technicians have incompatible workflows. These specific pairs must be strictly separated and cannot be scheduled for the same production phase. Your task is to allocate exactly one production phase (1, 2, or 3) to each technician such that no two incompatible technicians are assigned to the same phase. If there is no way to satisfy this requirement, you must report that it is impossible.

To maintain compliance with safety regulations, the scheduling system enforces the following constraints on the input data:
- The total number of recorded incompatibilities across the entire facility is capped at 780.
- For any given incompatible pair of technicians, the product of their identification numbers will never exceed 1600.

## Input
The first line provides two integers $n$ and $m$ — the total number of technicians and the total number of incompatible pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$, representing a pair of technicians who cannot share the same production phase.

## Output
If it is impossible to schedule the technicians under the given restrictions, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $p_1, p_2, \dots, p_n$ (where each $p_i \in \{1, 2, 3\}$), representing the production phase assigned to technician $i$. If multiple valid schedules exist, you must output the one that is lexicographically smallest (i.e., compare the phase of technician 1 first, then technician 2, and so forth).

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
