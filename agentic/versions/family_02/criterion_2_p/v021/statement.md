# Problem B — Pressure Release Networks

Time limit: 1 s   Memory limit: 256 MB

## Description

An industrial reactor is equipped with $n$ pressure valves. Before initiating the reaction, each valve must be locked into one of two states: Open (1) or Closed (0).

To prevent catastrophic failure, the reactor features $m$ emergency bypass conduits. Each conduit is wired to monitor exactly two specific valve-states. A valve-state is designated by a non-zero integer $X$:
- A positive integer $X$ indicates that valve $X$ is Open.
- A negative integer $X$ indicates that valve $|X|$ is Closed.

The safety interlock of a conduit operates on a strict dependency principle. Because a conduit monitors exactly two valve-states, failing to match the first state physically forces the second state to become mandatory for the conduit to safely route pressure. Symmetrically, failing to match the second state forces the first to become mandatory. Consequently, a conduit functions safely if and only if at least one of its two monitored valve-states is active in the global configuration.

Your task is to determine whether there exists a single, static configuration of the $n$ valves that allows every bypass conduit to function safely at the same time. If such a configuration exists, you must output it. Otherwise, report that the system's dependencies are mutually contradictory.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two non-zero signed integers $l_1$ and $l_2$, with $|l_i| \le n$, representing the two valve-states monitored by that conduit.

## Output
If no valid configuration exists, print a single line `NO`.
Otherwise print `YES` on the first line. On the second line print $n$ integers $s_1 \ s_2 \ \dots \ s_n$ (each in $\{0, 1\}$) forming any valid configuration. Here, $s_i = 1$ means valve $i$ is Open, and $s_i = 0$ means valve $i$ is Closed. 

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
Multiple valid configurations may exist; any one is accepted. The same valve-state may be monitored by multiple conduits.
