# Problem B — Configuration State Search

Time limit: 1 s   Memory limit: 256 MB

## Description

A control panel has **n** binary switches. Commissioning supplies **m** hardware interlocks that must all be respected simultaneously to prevent system faults. 

Each interlock involves two switches and designates a safe mode for each. The interlock acts as a fail-safe that strictly forbids the panel from being configured in the one specific way where both involved switches are simultaneously set to the exact opposite of their designated safe modes. Given the vast number of possible global states, engineers need to know if a valid state exists without an exhaustive search. 

Decide whether a single global ON/OFF setting of all **n** switches avoids all forbidden combinations at once. If such a configuration exists, report one; otherwise, report that the interlocks are mutually contradictory.

## Input
The first line contains two integers **n** and **m** (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next **m** lines contains two non-zero signed integers $l_1$ and $l_2$, with $|l_i| \le n$. 

The absolute value $|l_i|$ identifies a switch. The sign of $l_i$ specifies its safe mode for this interlock (positive for ON, negative for OFF). The interlock dictates that a system fault occurs if switch $|l_1|$ is set to the opposite of its safe mode while switch $|l_2|$ is simultaneously set to the opposite of its safe mode. This specific combination is forbidden.

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