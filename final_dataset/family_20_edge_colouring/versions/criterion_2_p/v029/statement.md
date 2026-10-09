# Problem B — Service Windows on a Cross-Tier Exchange Fabric

Time limit: 2 s   Memory limit: 256 MB

## Description
An exchange fabric connects a bank of alpha-tier ports to a bank of beta-tier ports. Each installed cable joins exactly one alpha port to exactly one beta port, and no cable ever runs between two ports in the same tier — the wiring strictly crosses tiers. Different ports carry different numbers of cables, and the most heavily connected port in the whole fabric sets the scale of the schedule.

Maintenance is organised into numbered service windows 1, 2, 3, …, and taking a cable offline consumes one whole window. The single binding safety rule is that two cables meeting at a common port may never be serviced in the same window, because a port cannot be relieved of two of its cables at once. Cable lengths, port hardware revisions, traffic classes, and which tier a cable's endpoint sits in are all irrelevant beyond this meeting-rule; only which cables share a port matters.

Because the most heavily connected port has some number of cables and none of them can share a window, at least that many windows are unavoidable. The operations goal is to schedule using **no more** windows than that unavoidable minimum — exactly the peak connection count. Assign every cable a window drawn from that many windows so that no port ever has two of its cables scheduled in the same window. (The cross-tier wiring guarantees the unavoidable minimum is always achievable; despite appearances, no window beyond the peak connection count is ever needed.)

## Input
First line: three integers nA, nB, m (1 ≤ nA, nB ≤ 100000, 0 ≤ m ≤ 400000).
Next m lines: two integers u v (1 ≤ u ≤ nA, 1 ≤ v ≤ nB): a cable between alpha u and beta v.

## Output
Print `YES`, then a line with m integers in 1..D (where D is the peak connection count) — the window assigned to cable i in input order (cables meeting at any port must differ).

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
