# Problem B — Service Windows on an Exchange Fabric

Time limit: 2 s   Memory limit: 256 MB

## Description
An exchange fabric connects a bank of L-type ports to a bank of R-type ports. Each installed cable joins exactly one L-type port to exactly one R-type port; the rules of the fabric strictly dictate that a cable never joins two ports of the same type. Different ports carry different numbers of cables, and the busiest port in the whole fabric sets the scale of the schedule.

Maintenance is organised into numbered service windows 1, 2, 3, …, and taking a cable offline consumes one whole window. The single binding safety rule is that two cables meeting at a common port may never be serviced in the same window, because a port cannot be relieved of two of its cables at once. Cable lengths, port hardware revisions, traffic classes, and which type a cable's endpoint belongs to are all irrelevant beyond this meeting-rule; only which cables share a port matters.

Because the busiest port has some number of cables and none of them can share a window, at least that many windows are unavoidable. The operations goal is to schedule using **no more** windows than that unavoidable minimum — exactly the busiest-port count. Assign every cable a window drawn from that many windows so that no port ever has two of its cables scheduled in the same window. (The rule that cables only connect L-type to R-type ports guarantees the unavoidable minimum is always achievable; despite appearances, no window beyond the busiest-port count is ever needed.)

## Input
First line: three integers nL, nR, m (1 ≤ nL, nR ≤ 100000, 0 ≤ m ≤ 400000).
Next m lines: two integers u v (1 ≤ u ≤ nL, 1 ≤ v ≤ nR): a cable between L-type port u and R-type port v.

## Output
Print `YES`, then a line with m integers in 1..Δ — the assigned window of cable i in input order (cables meeting at any junction must differ). Here, Δ is the number of cables at the busiest port.

## Example

**Input:**
```
3 3 4
1 1
1 2
2 2
3 3
```

**Output:**
```
YES
1 2 1 1
```
