# Problem B — Production Line Configuration

Time limit: 1 s   Memory limit: 256 MB

## Description

A manufacturing plant contains $n$ distinct machines. Each machine must be calibrated to one of two operational modes: mode 1 or mode 0. The plant managers have compiled a list of $m$ critical safety tolerances. Each tolerance lists exactly two desired machine states. A tolerance is considered met if at least one of its two listed states matches the actual calibration of the machines.

Determine if there is a way to calibrate all $n$ machines such that every single safety tolerance is met simultaneously. If such a plant-wide calibration is possible, provide one. Otherwise, indicate that the tolerances cannot all be met.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two non-zero integers $l_1$ and $l_2$, where $|l_i| \le n$. These represent the two desired states for a tolerance. A positive integer $x$ means machine $x$ being in mode 1 is desired. A negative integer $x$ means machine $|x|$ being in mode 0 is desired. For each tolerance, the final calibration must match at least one of the two desired states.

## Output
If there is no valid way to calibrate the machines to meet all tolerances, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$) representing the chosen mode for each machine from 1 to $n$.

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
Multiple valid calibrations may exist; any one is accepted. The same machine may appear in multiple tolerances.
