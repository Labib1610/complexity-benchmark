# Problem B — Vibration Control

Time limit: 1 s
Memory limit: 256 MB

The automated factory upgrade consists of three distinct phases. 

First, in Phase A, a robotic inspector surveys the $n$ newly installed machines (numbered 1 through $n$). It detects $m$ pairs of machines that share a delicate structural support.

Second, in Phase B, the central computer must assign an operating rhythm to each machine. Every machine must receive a rhythm from the set {1, 2}. To prevent catastrophic vibration, any two machines sharing a structural support must receive different rhythms.

Finally, in Phase C, the machines are powered on using the assigned rhythms, and production begins.

Your software is responsible for Phase B. You will receive the structural data produced by Phase A. You must determine if a safe rhythm assignment is possible. If it is, you must output a valid sequence of rhythms. Because the system requires a deterministic outcome, if there are multiple valid ways to assign the rhythms, you must output the valid sequence where the rhythm of machine 1 is as small as possible. If there are still ties, the rhythm of machine 2 must be as small as possible, and so on. If no safe assignment is possible, Phase C must be aborted.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$, representing a pair of machines that share a structural support.

## Output
If the machines cannot be assigned rhythms safely, print a single line containing `NO`.
If a safe assignment exists, print `YES` on the first line. On the second line, print $n$ space-separated integers $r_1, r_2, \ldots, r_n$ (where each $r_i \in \{1, 2\}$), representing the required rhythm for each machine in order from 1 to $n$.

## Example 1
**Input:**
```
4 4
1 2
2 3
3 4
1 4
```
**Output:**
```
YES
1 2 1 2
```

## Example 2
**Input:**
```
3 3
1 2
1 3
2 3
```
**Output:**
```
NO
```
