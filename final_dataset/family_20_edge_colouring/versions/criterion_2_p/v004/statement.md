# Problem B — Service Windows on a Two-Sided Exchange Fabric

Time limit: 2 s   Memory limit: 256 MB

## Description
An exchange fabric connects a bank of left-side ports to a bank of right-side ports. Each installed cable joins exactly one left port to exactly one right port, and no cable ever runs between two ports on the same side. Different ports carry different numbers of cables, and the busiest port in the whole fabric sets the scale of the schedule.

Maintenance is organised into numbered service windows 1, 2, 3, …, and taking a cable offline consumes one whole window. The single binding safety rule is that two cables meeting at a common port may never be serviced in the same window, because a port cannot be relieved of two of its cables at once. With $m$ cables to schedule and multiple possible windows for each, the space of potential configurations is massive. Cable lengths, port hardware revisions, traffic classes, and which side a cable's endpoint sits on are all irrelevant beyond this meeting-rule; only which cables share a port matters.

Because the busiest port has some number of cables (let this be $\Delta$) and none of them can share a window, at least that many windows are unavoidable. The operations goal is to search the vast space of $\Delta^m$ possible assignments to find a valid schedule using **no more** windows than that unavoidable minimum — exactly the busiest-port count $\Delta$. Assign every cable a window drawn from that many windows so that no port ever has two of its cables scheduled in the same window. (The two-sided wiring guarantees a valid configuration always exists to be found; despite appearances, no window beyond the busiest-port count is ever needed.)

## Input
First line: three integers nL, nR, m (1 ≤ nL, nR ≤ 100000, 0 ≤ m ≤ 400000).
Next m lines: two integers u v (1 ≤ u ≤ nL, 1 ≤ v ≤ nR): a cable between left u and right v.

## Output
Print `YES`, then a line with m integers in 1..Δ — the shift of cable i in input order (cables meeting at any junction must differ).

## Example

### Input
```text
3 3 4
1 1
1 2
2 1
3 3
```

### Output
```text
YES
1 2 2 1
```
