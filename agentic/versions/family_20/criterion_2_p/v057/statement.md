# Problem B — Service Windows on a Cross-Tier Exchange Fabric

Time limit: 2 s   Memory limit: 256 MB

## Description
In the automated maintenance pipeline for a cross-tier exchange fabric, operations are divided into three distinct stages.

**Stage 1: Topology Audit** (Already completed)
An audit system scans the hardware and generates a manifest of all active connections. The fabric is strictly divided into a bank of alpha-tier ports and a bank of beta-tier ports. The audit guarantees that every cable connects exactly one alpha-tier port to exactly one beta-tier port. No cable ever connects two ports in the same tier.

**Stage 2: Schedule Synthesis** (Your task)
The scheduler receives the audit manifest and must assign each cable to a numbered service window (1, 2, 3, …). The hardware imposes a strict safety rule: a single port cannot have more than one of its connected cables serviced simultaneously. Thus, if any two cables share a port (whether alpha-tier or beta-tier), they must be assigned different service windows. 

To minimize overall downtime, the total number of service windows used must not exceed the unavoidable baseline. Let $D$ be the maximum number of cables connected to any single port across the entire fabric. Because all of that port's cables must have distinct windows, at least $D$ windows are required. You must schedule all cables using only windows $1$ through $D$. (Given the cross-tier architecture verified by the audit, it is guaranteed that a valid schedule using exactly $D$ windows always exists.)

**Stage 3: Execution** (Handled downstream)
An automated deployment tool will read your schedule and take the cables offline one window at a time to perform the maintenance.

You do not need to implement the audit or the execution stages; you only need to process the manifest and output the valid window assignments.

## Input
First line: three integers nA, nB, m (1 ≤ nA, nB ≤ 100000, 0 ≤ m ≤ 400000).
Next m lines: two integers u v (1 ≤ u ≤ nA, 1 ≤ v ≤ nB), representing a cable between alpha-tier port u and beta-tier port v.

## Output
Print `YES`, then a single line containing m integers from the range 1 to D (where D is the maximum number of cables connected to any single port). The i-th integer is the window assigned to the i-th cable in the input order. Cables meeting at any port must be assigned different windows.

## Example

**Input:**
```text
3 3 4
1 1
1 2
2 2
3 3
```

**Output:**
```text
YES
1 2 1 1
```
