# Problem B — Synchronization Phase Verification

Time limit: 2 s   Memory limit: 256 MB

## Description
The system initialization sequence consists of three phases. You are responsible for the second phase, the synchronization routine.

In the preceding diagnostic phase, the system identifies $q$ transmitter nodes (assigned IDs 1 through $q$) and $q$ receiver nodes (assigned IDs $q+1$ through $2q$). It tests the signal pathways and generates a log of $t$ stable connections. Each stable connection operates between one specific transmitter and one specific receiver.

Your task is to take this log and choose a subset of connections to activate. The strict requirement for the synchronization routine is that every single node—all $2q$ transmitters and receivers—must participate in exactly one activated connection. No node may be left dormant, and no node may handle multiple connections.

If you find a valid configuration, it will be passed to the final deployment phase, which assigns independent frequency bands to your chosen connections. If no such configuration exists, the deployment phase cannot proceed, as it expects complete integration of all components.

Decide whether the given log allows for a valid configuration. If it does, output one; otherwise, report that it is impossible.

## Input
The first line contains two integers $q$ and $t$ (1 ≤ $q$ ≤ 100000, 0 ≤ $t$ ≤ 400000), representing the number of transmitters (and receivers) and the number of stable connections identified in the first phase.
The following $t$ lines each contain two integers $a$ and $b$ (1 ≤ $a$ ≤ $q$ < $b$ ≤ $2q$), indicating a stable connection between transmitter $a$ and receiver $b$.

## Output
If it is possible to satisfy the synchronization requirements, print `YES` on the first line, followed by $q$ lines. Each of these lines must contain the two IDs of one chosen connection. If it is impossible, print `NO`.

## Example

**Input**
```text
3 4
1 4
1 5
2 5
3 6
```

**Output**
```text
YES
1 4
2 5
3 6
```
