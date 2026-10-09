# Problem B — Power Grid Feed Interlocks

Time limit: 1 s   Memory limit: 256 MB

## Description

A power grid operates **n** independent feed lines, each of which must be locked into either an ENERGIZED or ISOLATED state before commissioning. The grid is protected by **m** mutual interlocks. Each interlock monitors exactly two specific feed states across the grid. An interlock remains secure as long as at least one of its two monitored states is actively realized in the grid. 

Determine whether a single global configuration of all $n$ feed lines can secure every interlock at once, and if so, report one; otherwise, report that the safety requirements are irreconcilable.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two non-zero signed integers $l_1$ and $l_2$, with $|l_i| \le n$. A positive integer $x$ refers to feed line $x$ being in the ENERGIZED state, while a negative integer $-x$ refers to feed line $x$ being in the ISOLATED state. Each line dictates that at least one of these two monitored states must be present in the grid for that interlock to be secure.

## Output
If no secure configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \ s_2 \ \dots \ s_n$ (each in $\{0, 1\}$) forming any secure configuration, where 1 denotes ENERGIZED and 0 denotes ISOLATED.

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
Multiple secure configurations may exist; any one is accepted. The same feed line index may appear in multiple interlocks.