# Problem B — Optical Array Alignment

Time limit: 1 s   Memory limit: 256 MB

## Description
An optical array contains $n$ distinct filters, numbered 1 through $n$. A complete configuration assigns each filter exactly one of two modes: "active" (represented by the value 1) or "bypassed" (represented by the value 0).

During the system's alignment phase, it logs $m$ interference constraints. Every constraint consists of exactly two filter requirements. A single requirement specifies a desired mode for a particular filter: a positive integer $+i$ means filter $i$ is required to be "active", while a negative integer $-i$ means filter $i$ is required to be "bypassed". A constraint is considered resolved if at least one of its two requirements is met by the filter modes. Because each constraint contains exactly two requirements, a mode that violates one requirement strictly dictates that the other requirement must be satisfied, creating chains of necessary consequences.

Your objective is to evaluate the full set of constraints and determine if there exists a complete configuration for all $n$ filters such that every single constraint is resolved. If such a configuration is achievable, you must output one valid configuration. If the logged constraints inherently contradict each other such that no configuration can resolve them all, you must report this failure.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two non-zero signed integers $l_1$ and $l_2$, with $|l_i| \le n$. At least one of the two stated requirements must hold for the constraint to be resolved.

## Output
If no valid configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$) forming any valid configuration.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid configurations may exist; any one is accepted. The same filter index may appear in multiple constraints.
