# Frequency Allocation Pipeline

Time limit: 1 s   Memory limit: 256 MB

The city's environmental monitoring project follows a strict three-phase deployment pipeline.

**Phase A: Hardware Installation.** Technicians physically mount $n$ sensors on streetlights. During this phase, proximity data is collected, resulting in a list of $m$ sensor pairs that are physically close enough to cause signal overlap.

**Phase B: Frequency Allocation.** This is the step your software module must handle. Each sensor must be configured to use either frequency band 1 or frequency band 2. To prevent data loss, no two sensors identified as a close pair in Phase A can be assigned the same frequency band. If a valid configuration exists, your module must output it. To ensure reproducible builds, the automated testing framework requires the lexicographically smallest sequence of band assignments. A sequence $s_1, \dots, s_n$ is lexicographically smaller than another valid sequence $t_1, \dots, t_n$ if, at the first sensor index $i$ where they differ, $s_i < t_i$. If no such configuration is possible, your module must flag the failure.

**Phase C: Network Activation.** If your module outputs a valid configuration, the central server pushes the firmware updates and begins data collection. If your module flags a failure, the system halts and schedules a manual repositioning of the hardware.

Your task is to implement the logic for Phase B.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of installed sensors and the number of close pairs identified in Phase A.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of sensors that will experience signal overlap if assigned the same frequency band.

## Output
If Phase B cannot be completed successfully without signal overlap, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid frequency allocation.

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
