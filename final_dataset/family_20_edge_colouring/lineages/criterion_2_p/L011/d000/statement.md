# Problem B — Service Windows on a Cross-Tier Exchange Fabric

Time limit: 2 s   Memory limit: 256 MB

## Description
An exchange fabric connects a bank of primary ports to a bank of secondary ports. Each installed cable joins exactly one primary port to exactly one secondary port, and no cable ever runs between two ports of the same tier — the wiring strictly bridges the two tiers. Different ports carry different numbers of cables, and the most heavily utilized port in the whole fabric sets the scale of the schedule.

Maintenance is organised into numbered service windows 1, 2, 3, …, and taking a cable offline consumes one whole window. The single binding safety rule is that two cables meeting at a common port may never be serviced in the same window, because a port cannot be relieved of two of its cables at once. Cable lengths, port hardware revisions, traffic classes, and which tier a cable's endpoint sits on are all irrelevant beyond this meeting-rule; only which cables share a port matters.

Because the most heavily utilized port has some number of cables and none of them can share a window, at least that many windows are unavoidable. The operations goal is to schedule using **no more** windows than that unavoidable minimum — exactly the peak-utilization count. Assign every cable a window drawn from that many windows so that no port ever has two of its cables scheduled in the same window. (The cross-tier wiring guarantees the unavoidable minimum is always achievable; despite appearances, no window beyond the peak-utilization count is ever needed.)

## Input
First line: three integers nA, nB, m (1 ≤ nA, nB ≤ 100000, 0 ≤ m ≤ 400000).
Next m lines: two integers u v (1 ≤ u ≤ nA, 1 ≤ v ≤ nB): a cable between primary u and secondary v.

## Output
Print `YES`, then a line with m integers in 1..Δ — the window of cable i in input order (cables meeting at any port must differ, and Δ is the maximum number of cables at any single port).

## Example

**Input**
```text
3 3 4
1 1
1 2
2 2
3 3
```

**Output**
```text
YES
1 2 1 1
```
