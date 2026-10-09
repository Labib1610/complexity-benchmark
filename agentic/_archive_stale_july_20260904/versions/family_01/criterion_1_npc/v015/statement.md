# Problem A — Shift Allocation Protocol

Time limit: 2 s   Memory limit: 256 MB

A manufacturing facility operates continuously across three sequential time periods, designated as period 1, period 2, and period 3. The facility employs $n$ machinists, and management must allocate each machinist to exactly one of these periods. Safety incident logs indicate that certain pairs of machinists have interpersonal disputes. To prevent workplace disruptions, no two machinists with a documented dispute can be allocated to the same time period.

Management needs to determine if a completely safe allocation is possible. Furthermore, the payroll system requires the final schedule to be submitted as a sequence of $n$ period numbers, corresponding to machinists 1 through $n$. To ensure standardized reporting when multiple safe allocations are possible, the system mandates selecting the sequence that is lexicographically smallest (comparing the first machinist's period first, then the second's, and so on).

## Input
The first line provides two integers $n$ and $m$ — the total number of machinists and the number of documented disputes ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$, representing a pair of machinists who have a dispute.

## Output
If there is no way to allocate the machinists safely, output a single line containing `NO`.
If a safe allocation is possible, output `YES` on the first line. On the second line, output $n$ integers separated by spaces, where the $i$-th integer (which must be 1, 2, or 3) represents the time period assigned to machinist $i$. This sequence must be the lexicographically smallest among all valid allocations.

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
