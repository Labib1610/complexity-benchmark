# Problem A — Operational Rotation Subsystem

Time limit: 2 s   Memory limit: 256 MB

The factory's monthly scheduling pipeline consists of three distinct phases. 

In Phase 1, the safety committee conducts a comprehensive risk assessment using past incident reports and machinery proximity sensors. They observe all $n$ machinery operators and compile a log of specific operator pairs whose simultaneous presence on the factory floor creates a hazard. This log is passed directly to your system.

In Phase 2, your subsystem must process this log to generate a schedule. You are required to assign every operator to exactly one of three operational rotations (labeled 1, 2, and 3, corresponding to morning, evening, and night). To pass the safety check, you must guarantee that no two operators flagged as a hazardous pair in Phase 1 are placed into the same rotation. If the safety constraints are too restrictive, your subsystem must raise an alert.

In Phase 3, the financial module will read your generated assignments, apply union-mandated hourly multipliers based on the rotation number, and calculate final payroll amounts. You do not need to implement Phase 1 or Phase 3; your only task is to execute Phase 2 and output the rotation assignments.

## Input
The first line of the input contains two integers $n$ and $m$ — the total number of operators and the number of hazardous pairs identified in Phase 1 ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of operators who cannot be assigned to the same rotation.

## Output
If it is impossible to satisfy all safety constraints across the three rotations, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the rotation assigned to operator $i$. If multiple valid schedules exist, you may output any of them.

## Example 1
**Input:**
```
4 5
1 2
1 3
2 3
1 4
2 4
```
**Output:**
```
YES
1 2 3 3
```

## Example 2
**Input:**
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
**Output:**
```
NO
```
