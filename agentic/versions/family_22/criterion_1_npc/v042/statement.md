# Problem A — Planetary Terraforming Protocol

Time limit: 5 s   Memory limit: 256 MB

## Description
An interstellar corporation is preparing a barren planet for habitation. The project requires deploying exactly $n$ atmospheric processors to the surface. The deployment window is strictly limited: the corporation has exactly $T$ orbital cycles before the fleet must depart. Each processor takes exactly one orbital cycle to install.

During any single orbital cycle, the fleet can dispatch at most $M$ drop ships, meaning at most $M$ processors can be installed per cycle. There is no penalty for dispatching fewer than $M$ ships in a cycle, and no bonus for finishing the deployment early, as long as all $n$ processors are operational before the deadline.

The planetary atmosphere must be altered in a specific sequence to avoid catastrophic weather events. Certain foundational processors act as strict dependencies for more advanced ones. When one processor is a dependency for another, the foundational processor must be fully installed in a strictly earlier orbital cycle before the advanced one can be deployed. They cannot be installed concurrently in the same cycle, because the gases from the foundational processor must fully stabilize first. Processor size or specific drop ship assignments are irrelevant; only the cycle in which a processor is installed matters.

You are given the total number of processors $n$, the drop ship capacity per cycle $M$, the total available cycles $T$, and the number of dependency rules $m$. Assign every processor to a cycle within the deployment window so that all dependency rules are respected and no cycle exceeds the drop ship capacity, or report that the deployment cannot be finished in time. (Note that a timeline respecting all dependencies might still exceed the drop ship capacity in some cycles, and vice versa, so both constraints must be carefully balanced).

## Input
First line: four integers $n$, $M$, $T$, $m$. 
Each of the next $m$ lines: two integers $a$ $b$ — processor $a$ must be installed before processor $b$ is deployed.

## Output
Print `YES` then $n$ integers (the cycle of each processor, for processors $1$ through $n$ respectively, in $1 \dots T$); otherwise `NO`.

## Example

### Input
```text
5 2 3 4
1 3
2 3
3 4
3 5
```

### Output
```text
YES
1 1 2 3 3
```
