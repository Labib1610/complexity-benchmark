# Multi-Stage Telemetry Engine: Frequency Allocation

Time limit: 1 s   Memory limit: 256 MB

An automated monitoring pipeline processes operational telemetry across three distinct phases:

1. **Ingestion & Conflict Identification**: The pipeline receives telemetry records for $n$ units (indexed $1$ through $n$) and identifies $m$ pairwise conflict relations.
2. **Frequency Assignment**: Each unit must be assigned to run on frequency $1$ or frequency $2$. To prevent operational interference, any pair of units linked by a conflict relation must be assigned to different frequencies.
3. **Stream Serialization**: The assigned frequencies $(s_1, s_2, \dots, s_n)$ are encoded into a downstream payload. To optimize transmission latency, if multiple valid frequency configurations exist, the system requires the configuration that forms the lexicographically smallest sequence.

You are responsible for implementing Phase 2. Given the list of conflict rules, determine whether a valid assignment exists. If no valid assignment satisfies all interference rules, output `NO`. Otherwise, output `YES` followed by the lexicographically smallest sequence of frequencies $(s_1, s_2, \dots, s_n)$ where $s_i \in \{1, 2\}$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) indicating that unit $u$ and unit $v$ share a conflict relation and cannot be assigned the same frequency.

## Output
If no valid frequency assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid frequency assignment.

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
