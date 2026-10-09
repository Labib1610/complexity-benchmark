# Problem B — Plant Routing Guidelines

Time limit: 1 s   Memory limit: 256 MB

## Description

A chemical plant contains $n$ valves. Before starting a batch, every valve must be locked into either the primary position (denoted by 1) or the secondary position (denoted by 0).

The plant's safety system is governed by $m$ fallback guidelines. A guideline is constructed by specifying exactly two target valve positions. A target position is represented by a non-zero integer $v$: if $v > 0$, it refers to valve $v$ being in the primary position; if $v < 0$, it refers to valve $|v|$ being in the secondary position.

The guidelines operate as a mutual fallback mechanism. For any given guideline, if the plant's final configuration fails to align with one of the two target positions, the system strictly demands that the configuration aligns with the other target position. Consequently, a guideline is satisfied as long as the configuration does not simultaneously miss both of its targets.

You must determine whether there exists a single global configuration for all $n$ valves that satisfies every fallback guideline. If a valid configuration exists, report it; otherwise, report that the guidelines cannot be simultaneously met.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two non-zero integers $l_1$ and $l_2$, with $|l_i| \le n$. These represent the two target positions for a fallback guideline.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $s_1\ s_2\ \dots\ s_n$ (each in $\{0, 1\}$) forming any valid configuration.

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
Multiple valid configurations may exist; any one is accepted. The same target position may appear in multiple guidelines, and a guideline may specify the same target twice.
