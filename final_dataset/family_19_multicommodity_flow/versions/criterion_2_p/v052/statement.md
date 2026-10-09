# Problem B — Reactor Coolant Circulation

Time limit: 2 s
Memory limit: 256 MB

## Description
A thermal management system must manage a critical thermal transfer. The system contains $n$ junctions and $m$ unidirectional pipes. A single type of coolant (indicated by the constant `1` in the system parameters) is utilized.

A specific operation requires circulating exactly $d$ units of this coolant from the primary reservoir $s$ to the core extractor $t$. This circulation must occur within a single operational cycle.

Each pipe directs coolant from junction $u$ to junction $v$ and has a structural threshold, meaning it can safely carry a maximum of $cap$ units of coolant during this cycle. The volume assigned to each pipe must be a non-negative whole number.

Junctions are strictly sealed transit points. For all junctions other than $s$ and $t$, the total volume of coolant arriving from incoming pipes must perfectly match the total volume departing through outgoing pipes. These intermediate junctions cannot store or leak any coolant. The net volume leaving $s$ and the net volume arriving at $t$ must both be exactly $d$.

Determine a valid assignment of coolant volumes for each pipe that satisfies all structural thresholds and junction equilibrium rules, achieving the exact required circulation $d$. If no such configuration is possible, report that the operation cannot be executed.

## Input
Line 1: Three integers $n$, $m$, and $1$.
Line 2: Three integers $s$, $t$, and $d$.
Next $m$ lines: Three integers $u$, $v$, and $cap$, indicating a pipe from junction $u$ to junction $v$ with a structural threshold of $cap$.

## Output
If the operation can be executed, output `YES` on the first line. On the second line, output $m$ space-separated integers representing the volume of coolant assigned to each pipe, in the exact order they were provided in the input. (If multiple valid assignments exist, any will be accepted).
If it cannot be executed, output `NO`.

## Example

**Input:**
```
4 4 1
1 4 7
1 2 5
1 3 2
2 4 5
3 4 2
```

**Output:**
```
YES
5 2 5 2
```
