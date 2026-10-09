# Problem A — Deployment State Resolution

Time limit: 2 s   Memory limit: 256 MB

## Description
During the final stage of an automated deployment sequence, the system must set the operational mode for $n$ micro-switches. Every switch must be placed into exactly one of two modes: *engaged* or *isolated*.

Before the deployment can proceed, a hardware scanner generates a list of $m$ safety interlocks. Every interlock is defined by exactly three dependencies. A dependency is a requirement that a particular micro-switch be placed in a specific mode.

For an interlock to be considered secure, the final deployment state must align with at least one of its three dependencies. 

Your task is to determine whether it is possible to assign a mode to every micro-switch such that all $m$ interlocks are simultaneously secure. The same micro-switch may be referenced by many different interlocks, sometimes requiring it to be engaged and other times requiring it to be isolated.

If a secure state can be achieved, you must output a valid mode assignment. If the interlocks collectively conflict such that at least one interlock will always fail, the deployment must be aborted.

## Input
The first line contains two integers $n$ and $m$ (1 ≤ $n$ ≤ 90, 0 ≤ $m$ ≤ 400) — the number of micro-switches and the number of safety interlocks.
Each of the following $m$ lines describes one interlock using three non-zero integers $d_1, d_2, d_3$. The absolute value of each integer is between 1 and $n$, inclusive, and denotes a micro-switch ID.
A positive integer $x$ means the dependency requires micro-switch $x$ to be engaged.
A negative integer $x$ means the dependency requires micro-switch $|x|$ to be isolated.

## Output
If no secure state can be achieved, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $s_1, s_2, \ldots, s_n$. The value of $s_i$ should be `1` if micro-switch $i$ is engaged, and `0` if it is isolated. If there are multiple secure assignments, any valid one will be accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each interlock specifies exactly three dependencies. It is possible for the same micro-switch to appear more than once within a single interlock's dependencies.
