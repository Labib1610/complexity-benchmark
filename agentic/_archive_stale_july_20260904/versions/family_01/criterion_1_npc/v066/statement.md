# Problem A — Orbital Zones

Time limit: 2 s   Memory limit: 256 MB

The Global Aerospace Consortium executes its deployment protocol in three strict phases:

**Phase 1: Payload Integration.** Engineers finalize the structural chassis for $n$ satellites. Based on the operational frequencies of their transponders, they compile a registry of $m$ incompatible satellite pairs that would cause signal collisions if placed near each other.

**Phase 2: Altitude Stratification.** This is the computational step you are responsible for. The consortium maintains exactly three designated altitude bands, labeled 1, 2, and 3. Your module must allocate each of the $n$ satellites to exactly one of these three bands. To guarantee data integrity, no two satellites flagged as incompatible during Phase 1 can be placed in the same band. If no such allocation exists, the mission must be flagged for abort.

**Phase 3: Automated Bootstrapping.** Once deployed, ground control powers on the satellites sequentially from satellite 1 up to $n$. To ensure the initialization sequence is deterministic, the system requires the altitude allocation sequence $z_1, z_2, \ldots, z_n$ to be the lexicographically smallest valid sequence.

You are given the registry from Phase 1. Your task is to perform Phase 2 and output the exact configuration required for Phase 3.

## Input
The first line contains two integers $n$ and $m$ — the number of satellites and the number of incompatible pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of incompatible satellites.

## Output
If the mission must be aborted because no valid allocation exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $z_1, z_2, \ldots, z_n$ (where each $z_i \in \{1, 2, 3\}$), representing the altitude band assigned to satellite $i$. Among all valid allocations, output the lexicographically smallest sequence (comparing $z_1$ first, then $z_2$, and so on).

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
