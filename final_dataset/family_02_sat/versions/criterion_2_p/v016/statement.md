# Fluid Routing Protocols

Time limit: 1 s   Memory limit: 256 MB

## Description

A chemical plant operates a network of $n$ fluid routing valves. Each valve must be permanently configured to either the OPEN or CLOSED state before the reaction begins. 

The safety system enforces $m$ pressure-relief protocols. Every protocol highlights exactly two valve-state conditions. A condition is defined by a specific valve and a required state (OPEN or CLOSED). For the plant to operate safely, every protocol must have at least one of its two conditions met by the global valve configuration.

The protocol generation system guarantees two structural properties for the physical valve indices $A$ and $B$ (the absolute values of the two integers) in any protocol:
1. $A + B \le 2n$
2. $|A - B| < n$

These properties ensure the protocols fit within the legacy memory banks.

Determine if there exists a single global configuration for all $n$ valves that satisfies all $m$ safety protocols simultaneously. If such a configuration exists, you must also provide one. Otherwise, report that the protocols are inherently contradictory.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines describes a safety protocol with two non-zero signed integers $c_1$ and $c_2$. The absolute value $|c_i|$ represents the physical valve index ($1 \le |c_i| \le n$). A positive integer means the condition requires the valve to be OPEN; a negative integer means the condition requires the valve to be CLOSED. At least one of the two conditions $c_1$ or $c_2$ must be satisfied for the protocol to pass.

## Output
If no valid configuration of the $n$ valves can satisfy all protocols, output a single line with `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $v_1, v_2, \dots, v_n$, where $v_i \in \{0, 1\}$, representing a valid configuration (1 for OPEN, 0 for CLOSED). If multiple valid configurations exist, any one is acceptable.

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
