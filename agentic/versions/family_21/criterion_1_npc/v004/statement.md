# Problem A — Sealing a Facility into Isolated Containment Zones

Time limit: 5 s   Memory limit: 256 MB

## Description
A research facility is a network of rooms joined by corridors, each corridor carrying a sealing cost that reflects the labour and materials to close it permanently. Several rooms are designated containment sites (hubs), each holding materials that must never share an accessible zone with the materials at another containment site. The remediation team will seal a chosen set of corridors; a corridor, once sealed, no longer permits passage in either direction.

After the works, the containment sites must be **mutually isolated**: for every pair of containment sites, there must be no remaining path of unsealed corridors connecting them, so each site ends up in its own separated region of the facility. Rooms that are not containment sites may fall into whichever region the sealing produces — their placement is unconstrained and irrelevant to acceptance. What is measured is solely the total sealing cost, the sum of the costs of the corridors actually sealed.

Because finding the cheapest way to isolate any single pair of containment sites is a standard, efficiently solvable procedure, the main task is to coordinate these local separations globally. You are given a fixed remediation budget $B$. Choose a set of corridors to seal whose total cost does not exceed $B$ and whose removal leaves every pair of containment sites disconnected, or report that no sealing within budget can isolate all sites simultaneously.

## Input
Line 1: four integers $n$, $m$, $k$, $B$. 
Line 2: $k$ hub ids. 
Next $m$ lines: three integers $u$ $v$ $w$ — a link, where $u$ and $v$ are room ids and $w$ is the sealing cost.

## Output
`YES`, then a line with the number $c$ of removed links, then $c$ lines "$u$ $v$"; or `NO`.

## Example
**Input:**
```
4 3 3 20
1 2 3
1 4 10
2 4 10
3 4 10
```

**Output:**
```
YES
2
1 4
2 4
```
