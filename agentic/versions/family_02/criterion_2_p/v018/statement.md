# Problem B — Paired Window Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description
During the commissioning of a control panel, engineers define a series of interaction protocols based on the states of $n$ independent switches. Each switch can be positioned in one of two states, represented as 1 (engaged) or 0 (disengaged).

The behavior of the panel is governed by $m$ safety requirements. Each requirement specifies exactly two potential conditions for specific switches. A condition is defined by a switch index and its desired state—either engaged (represented by a positive integer $+x$) or disengaged (represented by a negative integer $-x$, where $x$ is the switch index). A requirement is considered fulfilled as long as at least one of its two specified conditions matches the actual configuration of the panel. Because these requirements link switches in pairs, a configuration that fails to meet one side of a requirement mandates that the other side must be met, creating cascades of necessary states. The same switch may appear in multiple requirements.

Your task is to determine if there is a comprehensive configuration for all $n$ switches that simultaneously fulfills all $m$ safety requirements. If such a configuration is possible, you must provide it; if the requirements inherently conflict, you must report this impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two non-zero signed integers $l_1$ and $l_2$, with $|l_i| \le n$. A positive integer $x$ indicates the condition that switch $x$ is 1, while a negative integer $-x$ indicates the condition that switch $x$ is 0. At least one of the two conditions in each line must be satisfied.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each in $\{0, 1\}$) representing the state of each switch in any valid configuration. If multiple valid configurations exist, any one is accepted.

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
