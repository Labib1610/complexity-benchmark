# Problem A — Shift Allocation Protocol

Time limit: 2 s
Memory limit: 256 MB

A manufacturing facility operates continuously across three sequential time periods: Shift 1, Shift 2, and Shift 3. The facility employs $n$ machinists, and management must assign each machinist to exactly one of these three shifts. 

Safety incident logs indicate that certain pairs of machinists have interpersonal disputes. The conflict data is provided as a list of simple pairwise restrictions. There are no complex group constraints; every rule simply states that two specific machinists cannot be assigned to the same shift. Because there are exactly three shifts available, assigning a machinist to one shift mathematically leaves exactly two valid shift options for any conflicting colleague. 

Management needs to determine if a completely safe allocation is possible, where no two machinists with a documented dispute share the same shift. 

Furthermore, the payroll system requires the final schedule to be submitted as a sequence of $n$ shift numbers, corresponding to machinists 1 through $n$. To standardize reporting, the system mandates selecting the sequence of shift numbers that is lexicographically smallest. This means that among all valid schedules, you must choose the one that places machinist 1 in the earliest possible shift; in the event of ties, it must place machinist 2 in the earliest possible shift, and so forth.

## Input
The first line provides two integers $n$ and $m$ — the total number of machinists and the number of documented disputes ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$, representing a pair of machinists who have a dispute.

## Output
If there is no way to allocate the machinists safely across the three shifts, output a single line containing `NO`.
If a safe allocation is possible, output `YES` on the first line. On the second line, output $n$ integers separated by spaces, where the $i$-th integer (which must be 1, 2, or 3) represents the shift assigned to machinist $i$. This sequence must be the lexicographically smallest among all valid safe allocations.

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
