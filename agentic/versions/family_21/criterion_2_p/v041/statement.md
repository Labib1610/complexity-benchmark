# Problem B — Structural Isolation

Time limit: 2 s   Memory limit: 256 MB

## Description
An underground facility is made up of several chambers. Corridors run between specific pairs of chambers. Any corridor can be permanently blocked by injecting a specific volume of fast-curing resin. Once blocked, transit through that corridor is permanently halted in both directions.

Two particular chambers are designated as primary quarantine targets. To enforce the containment protocol, it must be completely impossible to travel between these two targets via any succession of unblocked corridors.

It is acceptable for other chambers to remain reachable from either quarantine target, provided that no route exists that bridges the two targets. You have access to a strictly capped inventory of resin. You need to determine a collection of corridors to block so that the total resin expended is at most this inventory cap, and the two targets are successfully separated. If no such collection exists within the cap, you must indicate this.

## Input
The first line contains five integers: the number of chambers, the number of corridors, the identifier of the first quarantine target, the identifier of the second quarantine target, and the total resin cap. 
The following lines detail the corridors, one per line. Each line contains three integers: the identifiers of the two chambers it links, and the volume of resin required to block it. 

## Output
If the separation can be accomplished without exceeding the cap, print `YES` on the first line. On the second line, print the number of blocked corridors, $c$. Then, print $c$ lines, each containing the two chamber identifiers for one of the blocked corridors. If the cap is strictly exceeded or separation is impossible, print `NO`.

## Example

**Input**
```text
4 4 1 4 10
1 2 4
1 3 7
2 4 5
3 4 2
```

**Output**
```text
YES
2
1 2
3 4
```
