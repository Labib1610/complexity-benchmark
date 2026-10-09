# Problem B — Configuration State Search

Time limit: 1 s   Memory limit: 256 MB

## Description

A control panel has **n** binary switches. Commissioning supplies **m** hardware interlocks that enforce dependency rules between switches to prevent system faults. 

Each interlock connects two switches and designates a target mode for each. The interlock acts as a conditional override: should the panel be configured such that the first switch fails to match its target mode, the interlock guarantees safety by requiring the second switch to be set to its target mode. The hardware mechanism is symmetric; a failure of the second switch to match its target mode will similarly force the first switch to its target mode. Given the vast number of possible global states, engineers need to know if a valid state exists without an exhaustive search. 

Decide whether a single global ON/OFF setting of all **n** switches satisfies all interlock dependencies at once. If such a configuration exists, report one; otherwise, report that the interlocks are mutually contradictory.

## Input
The first line contains two integers **n** and **m** (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next **m** lines contains two non-zero signed integers $l_1$ and $l_2$, with $|l_i| \le n$. 

The absolute value $|l_i|$ identifies a switch. A positive value indicates a target mode of ON, while a negative value indicates a target mode of OFF. The interlock dictates a conditional requirement: if the switch identified by $|l_1|$ is set to the opposite of its target mode, then the switch identified by $|l_2|$ must be set to its target mode. The requirement works in both directions: if the switch identified by $|l_2|$ is set to the opposite of its target mode, then the switch identified by $|l_1|$ must be set to its target mode.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise print `YES` on the first line. On the second line print **n** integers $s_1 \ s_2 \dots s_n$ (each in {0, 1}) forming any valid assignment, where 1 represents ON and 0 represents OFF.

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
Multiple valid assignments may exist; any one is accepted. The same switch may appear in multiple interlocks.