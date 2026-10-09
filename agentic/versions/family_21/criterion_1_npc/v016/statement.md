# Problem A — Sealing a Facility into Isolated Containment Zones

Time limit: 5 s   Memory limit: 256 MB

## Description
A research installation consists of a network of rooms connected by corridors. Each corridor has a specific sealing cost, representing the labour and materials required to permanently block passage through it. Once a corridor is sealed, it can no longer be traversed in either direction.

Within this installation, several specific rooms are classified as containment sites. Each containment site houses volatile materials that must never be accessible from any other containment site. The remediation crew has been tasked with selecting a subset of corridors to seal such that all containment sites are completely separated from one another. 

Specifically, after the selected corridors are sealed, the containment sites must be **mutually isolated**: there must be no valid path of unsealed corridors between any pair of containment sites. Rooms that are not containment sites are not subject to isolation requirements; they can end up in any of the resulting accessible zones.

The operation is constrained by a fixed budget. You must find a set of corridors to seal such that:
1. Every containment site is disconnected from every other containment site.
2. The total sealing cost (the sum of the costs of the sealed corridors) is at most the budget.
3. The total number of sealed corridors is at most the initial number of corridors in the installation.
4. The number of distinct accessible zones (maximal sets of rooms reachable from one another via unsealed corridors) remaining in the installation after the operation is at least the number of containment sites.

If it is possible to achieve this within the budget, output the chosen corridors. If no such set of corridors exists that satisfies all conditions simultaneously within the budget, you must report that it is impossible.

## Input
The first line provides four integers $n$, $m$, $k$, and $B$: the number of rooms, the number of corridors, the number of containment sites, and the total sealing budget, respectively. 
The second line contains $k$ integers representing the room identifiers of the containment sites. 
The following $m$ lines each contain three integers $u$, $v$, and $w$, indicating that a corridor connects room $u$ and room $v$ with a sealing cost of $w$.

## Output
If the isolation can be achieved within the budget, print `YES` on the first line. On the second line, print the integer $c$, representing the number of corridors to be sealed. Following this, print $c$ lines, each containing two integers $u$ and $v$ representing a sealed corridor (the order of corridors, and the order of rooms within each pair, does not matter).
If the isolation cannot be achieved within the budget, print `NO`.

## Example
**Input:**
```
4 3 3 5
1 2 3
1 4 2
2 4 3
3 4 4
```

**Output:**
```
YES
2
1 4
2 4
```
