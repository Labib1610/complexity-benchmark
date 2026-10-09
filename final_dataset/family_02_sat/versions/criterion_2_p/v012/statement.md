# Problem B — Thermal Vent Protocols

Time limit: 1 s   Memory limit: 256 MB

## Description

A deep-space probe has $n$ thermal vents. Each vent must be permanently configured to either an open state (represented by 1) or a closed state (represented by 0) before entering the atmosphere.

Mission control has transmitted $m$ safety protocols. Each protocol links exactly two vent states. A protocol operates via a strict fallback mechanism: if the first specified state is not adopted by the probe, the second specified state becomes absolutely mandatory to maintain structural integrity. Symmetrically, if the second specified state is not adopted, the first becomes mandatory. This fallback mechanism ensures that for every protocol, at least one of its two specified states is present in the final configuration.

Because these protocols interlock, failing to adopt a state can trigger a cascade of mandatory states across many vents. You must determine whether there exists a single, stable configuration for all $n$ vents such that every protocol is satisfied without any vent being forced into conflicting states. If a stable configuration exists, you must output it; otherwise, report that the protocols are inherently contradictory.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two non-zero signed integers $l_1$ and $l_2$, with $|l_i| \le n$. 
A positive integer $l$ indicates the state where vent $|l|$ is open (1).
A negative integer $l$ indicates the state where vent $|l|$ is closed (0).
Each line represents a single protocol requiring at least one of the two states $l_1$, $l_2$ to be adopted.

## Output
If no valid configuration exists that satisfies all protocols, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$) representing the state of each vent from 1 to $n$ in a valid configuration.

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
Multiple valid configurations may exist; any one is accepted. The same vent may appear in multiple protocols.
