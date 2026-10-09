# Problem B — Facility Configuration

Time limit: 1 s   Memory limit: 256 MB

## Description

A complex industrial facility contains $n$ independent subsystems. Each subsystem must be locked into one of two operational modes: Active or Dormant. This results in an enormous configuration space of $2^n$ possible global states, which can make manual verification impossible. 

During certification, inspectors compile a list of $m$ operational dependencies that the final state must respect. Each dependency is defined by exactly two acceptable conditions (a condition being a specific subsystem set to a specific mode). A dependency is considered resolved if the global state exhibits at least one of its two conditions.

Your task is to search the configuration space to determine if there exists a valid global state that simultaneously resolves all $m$ dependencies. If such a state exists, you must provide one. If no such state exists among the $2^n$ possibilities, report this.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two non-zero signed integers $c_1$ and $c_2$, with $|c_i| \le n$. These represent the two conditions for a single dependency. The absolute value of an integer represents the subsystem index (from 1 to $n$). A positive integer means the condition is that the subsystem is Active. A negative integer means the condition is that the subsystem is Dormant. 

## Output
If no valid global state exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1\ s_2\ \ldots\ s_n$ (each in $\{0, 1\}$) forming any valid configuration. An output of 1 indicates the subsystem is Active, while 0 indicates it is Dormant.

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
Multiple valid configurations may exist; any one is accepted. The same subsystem may appear in multiple dependencies.
