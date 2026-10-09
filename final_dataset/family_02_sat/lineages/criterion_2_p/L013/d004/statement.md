# Problem B — Paired Window Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description
A control panel features $n$ binary switches, each taking a state $s_i \in \{0, 1\}$. The commissioning team has provided $m$ hardware interlocks. Each interlock connects two expected positions across a pair of switches.

An expected position is specified by a non-zero integer $l$. The absolute value $|l|$ identifies the switch index ($1 \le |l| \le n$). The sign of $l$ defines a target state $t(l)$, where $t(l) = 1$ if $l > 0$, and $t(l) = 0$ if $l < 0$.

Each of the $m$ interlocks provides a pair of expected positions, $l_1$ and $l_2$. For the system to be safely configured, every interlock must satisfy the following algebraic constraint:
$(s_{|l_1|} - t(l_1)) \times (s_{|l_2|} - t(l_2)) = 0$

Your task is to determine whether a global configuration $s_1, s_2, \dots, s_n$ exists such that all $m$ equations are simultaneously satisfied. If such a configuration exists, you must provide it. If no such configuration is possible, you must report that the system is unconfigurable.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of switches and the number of interlocks, respectively.

Each of the following $m$ lines contains two non-zero signed integers $l_1$ and $l_2$ ($1 \le |l_i| \le n$). For each expected position, the absolute value indicates the switch index. A positive integer defines an expected position of ON (target state $1$), while a negative integer defines an expected position of OFF (target state $0$). The two expected positions in an interlock may refer to the same switch, and may be identical or opposite.

## Output
If no valid configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$) representing a valid configuration, where $1$ denotes ON and $0$ denotes OFF.

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
Multiple valid configurations may exist; any one of them is accepted. The same switch may be monitored by multiple interlocks.