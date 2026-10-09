# Problem B — Service Windows on a Two-Sided Exchange Fabric

Time limit: 2 s   Memory limit: 256 MB

## Description
An exchange fabric contains ports and cables. Different ports carry different numbers of cables, and the busiest port in the whole fabric sets the scale of the schedule. The ports are divided into a left bank and a right bank, and each cable joins a left port to a right port without ever connecting two ports on the same side.

Maintenance is organised into numbered service windows 1, 2, 3, …, and taking a cable offline consumes one whole window. The single binding safety rule is that two cables meeting at a common port may never be serviced in the same window, because a port cannot be relieved of two of its cables at once. Cable lengths, port hardware revisions, traffic classes, and which side a cable's endpoint sits on are all irrelevant beyond this meeting-rule; only which cables share a port matters.

A maintenance schedule assigns one of $k$ service windows to each of the $m$ cables, meaning the combinatorial space of possible schedules has size $k^m$. The operations goal is to search this space for a valid assignment using exactly $k$ windows, where $k$ is the number of cables at the busiest port. Assign every cable a window drawn from these $k$ windows so that no port ever has two of its cables scheduled in the same window. (The wiring guarantees that at least one valid schedule exists in this space; despite appearances, no window beyond the busiest-port count is ever needed.)

## Input
First line: three integers nL, nR, m (1 ≤ nL, nR ≤ 100000, 0 ≤ m ≤ 400000).
Next m lines: two integers u v (1 ≤ u ≤ nL, 1 ≤ v ≤ nR): a cable between left u and right v.

## Output
Print `YES`, then a line with m integers in 1..k — the allocated window of cable i in input order (cables meeting at any port must differ).

## Example

### Input
```text
3 3 4
1 1
1 2
2 2
3 3
```

### Output
```text
YES
1 2 1 1
```
