# Thermal Expansion Framework

Time limit: 1 s   Memory limit: 256 MB

## Description
A structural framework contains $n$ thermal struts. Each strut $i$ ($1 \le i \le n$) is controlled by a binary mode $s_i \in \{0, 1\}$.
- Setting $s_i = 1$ places the strut in heating mode, causing it to expand by $1$ mm.
- Setting $s_i = 0$ places the strut in cooling mode, causing it to contract by $1$ mm.

The framework is reinforced by $m$ rigid braces. Each brace spans exactly two connections across the framework. A brace's connections are specified by two non-zero integers $l_1$ and $l_2$. For any connection $l$:
- The absolute value $|l|$ identifies the strut index it attaches to.
- The sign of $l$ dictates its mechanical orientation relative to the brace:
  - If $l > 0$, it is a standard mount. The connection's displacement matches the strut exactly: $+1$ mm if $s_{|l|} = 1$, and $-1$ mm if $s_{|l|} = 0$.
  - If $l < 0$, it is an inverted mount. The connection's displacement is the exact opposite of the strut: $+1$ mm if $s_{|l|} = 0$, and $-1$ mm if $s_{|l|} = 1$.

Inside each brace, the displacements from its two connections are added together.
A brace will catastrophically fracture if and only if the total combined displacement from its two connections is exactly $-2$ mm (meaning both connections contract, pulling the brace apart beyond its tolerance). If the total displacement is $0$ mm or $+2$ mm, the brace safely absorbs the stress and remains intact.

Your task is to determine whether there is a configuration of modes $s_1, s_2, \dots, s_n$ such that all $m$ braces remain intact. If it is possible, you must provide the configuration. If no such configuration exists, print a single line containing `NO`.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of struts and the number of braces, respectively.

Each of the following $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($1 \le |l_i| \le n$), detailing the two connections for a single brace. The two connections for a brace may attach to the same strut, may be the exact same connection ($l_1 = l_2$), or may be the same strut with opposite signs ($l_1 = -l_2$). The same pair of connections may also appear on multiple braces. 

## Output
If no valid configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$) representing a valid configuration.

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
Multiple valid configurations may exist; any one of them is accepted. If $m = 0$, there are no braces to fracture, so any combination of $n$ valid modes is acceptable.