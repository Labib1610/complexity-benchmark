# Problem B — Configuration State Search

Time limit: 1 s   Memory limit: 256 MB

## Description

A control panel has **n** binary switches, each of which can be set to ON or OFF. Commissioning supplies **m** hardware interlocks that enforce dependency rules between switches to prevent system faults. 

Each interlock connects two switches and is defined by two non-zero integers $l_1$ and $l_2$. The absolute value $|l_i|$ identifies the switch index. 

To determine if an interlock is satisfied, we assign a state value $V(x)$ to each switch $x$: $V(x) = 1$ if switch $x$ is ON, and $V(x) = -1$ if switch $x$ is OFF. 
Similarly, we extract the sign of each connection $sgn(l_i)$: $sgn(l_i) = 1$ if $l_i > 0$, and $sgn(l_i) = -1$ if $l_i < 0$.

An interlock is satisfied if and only if the sum of the products of the state values and the connection signs is non-negative. That is, for an interlock given by $l_1$ and $l_2$, the current configuration must satisfy:
$$V(|l_1|) \times sgn(l_1) + V(|l_2|) \times sgn(l_2) \ge 0$$

A system fault occurs if any of the **m** interlocks is not satisfied. Given the vast number of possible global states, engineers need to know if a valid state exists without an exhaustive search. 

Decide whether a single global ON/OFF setting of all **n** switches avoids all system faults simultaneously. If such a configuration exists, report one; otherwise, report that the interlocks are mutually contradictory.

## Input
The first line contains two integers **n** and **m** (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next **m** lines contains two non-zero signed integers $l_1$ and $l_2$, with $|l_i| \le n$. 

The absolute value $|l_i|$ identifies a switch. The sign of $l_i$ provides the coefficient $sgn(l_i)$ used in the interlock's evaluation formula.

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