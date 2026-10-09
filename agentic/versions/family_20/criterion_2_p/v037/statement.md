# Problem B — Service Windows on a Two-Sided Exchange Fabric

Time limit: 2 s   Memory limit: 256 MB

## Description
An exchange fabric connects a bank of left-side ports to a bank of right-side ports. Each installed cable
joins exactly one left port to exactly one right port, and no cable ever runs between two ports on the
same side — the wiring is strictly two-sided. Different ports carry different numbers of cables, and the
busiest port in the whole fabric sets the scale of the schedule.

Maintenance is organised into numbered service windows 1, 2, 3, …, and taking a cable offline consumes one
whole window. The single binding safety rule is that two cables meeting at a common port may never be
serviced in the same window, because a port cannot be relieved of two of its cables at once. Cable
lengths, port hardware revisions, traffic classes, and which side a cable's endpoint sits on are all
irrelevant beyond this meeting-rule; only which cables share a port matters.

Because the busiest port has some number of cables and none of them can share a window, at least that many
windows are unavoidable. The operations goal is to schedule using **no more** windows than that
unavoidable minimum — exactly the busiest-port count (Δ). Assign every cable a window drawn from that many
windows so that no port ever has two of its cables scheduled in the same window. (The two-sided wiring
guarantees the unavoidable minimum is always achievable; despite appearances, no window beyond the
busiest-port count is ever needed.)

## Input
First line: three integers nL, nR, m. The left and right banks each contain at least one port, up to a physical limit of 100,000 ports per bank. The total number of cables m starts from an empty fabric of zero up to a maximum installation of 400,000 cables.
Next m lines: two integers u v. Each line identifies a cable between left port u (numbered between 1 and nL inclusive) and right port v (numbered between 1 and nR inclusive).

## Output
Print `YES`, then a line with m integers in 1..Δ — the shift of cable i in input order (cables meeting
at any junction must differ).

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
