# Harmonic Interference Resolution

Time limit: 1 s
Memory limit: 256 MB

A research facility operates a network of acoustic projectors. To maintain operational stability, every projector in the network must be assigned a fixed pulse cycle of either 1 microsecond or 2 microseconds.

The facility's layout contains multiple interference thresholds, each connecting a specific pair of projectors. A cycle assignment is only viable if it resolves the interference across the entire network. The stability value of a single threshold connecting projector $u$ and projector $v$ is calculated using their assigned pulse cycles, $p_u$ and $p_v$, with the following formula:

$6(p_u + p_v) - (p_u + p_v)^2$

For the network assignment to be viable, the total sum of the stability values across all $m$ thresholds must equal exactly $9m$.

Your objective is to determine if a viable cycle assignment exists for the entire network. If multiple valid assignments are possible, the diagnostic system requires a single deterministic configuration. Among all valid assignments, output the lexicographically smallest sequence of $n$ pulse cycles (ordered from projector 1 to projector $n$). This means selecting the sequence that features the shorter pulse cycle (1 instead of 2) at the earliest projector index where the assignments differ.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 200,000$, $0 \le m \le 200,000$), representing the number of projectors and the number of thresholds, respectively.

Each of the subsequent $m$ lines provides two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that an interference threshold connects the projector indexed $u$ and the projector indexed $v$.

## Output
If it is impossible to find a viable cycle assignment, output `NO` on a single line.
If a viable assignment exists, output `YES` on the first line. On the second line, output $n$ space-separated integers (each being either 1 or 2) representing the pulse cycle assigned to each projector from 1 to $n$. This sequence must be the lexicographically smallest valid assignment.

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