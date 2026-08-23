# Problem A — Maintenance Scheduling

Time limit: 2 s
Memory limit: 256 MB

A transit agency is organizing maintenance for $n$ vehicles. The maintenance process is divided into three distinct phases, denoted by the identifiers 1, 2, and 3. Every vehicle must be assigned to exactly one phase.

Certain pairs of vehicles draw power from the same limited circuit. You are given a list of these shared-circuit pairs. The core operational requirement is that if two vehicles share a circuit, they cannot undergo maintenance in the same phase.

Your task is to find a phase assignment for all vehicles that avoids overloading any circuits. If there are multiple valid ways to schedule the vehicles, you must output the assignment that evaluates to the numerically smallest sequence. This means the schedule must assign the smallest possible phase identifier to vehicle 1; if ties remain, it must minimize the phase identifier for vehicle 2, and so on, continuing sequentially through all $n$ vehicles.

### Input
The first line contains two integers $n$ and $m$ — the number of vehicles and the number of shared-circuit pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$, indicating that vehicle $u$ and vehicle $v$ share a circuit. Vehicles are identified by integers from 1 to $n$.

### Output
If a valid schedule cannot be found, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each being 1, 2, or 3), where $s_i$ represents the phase assigned to vehicle $i$. This sequence must be the valid assignment that is smallest when compared element by element from left to right.

### Example 1
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

### Example 2
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
