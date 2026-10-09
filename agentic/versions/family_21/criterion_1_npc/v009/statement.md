# Problem A — Sealing a Facility into Isolated Containment Zones

Time limit: 5 s   Memory limit: 256 MB

## Description
A research facility is a network of rooms joined by corridors. A chosen set of these corridors will be permanently sealed, which prevents passage in either direction. Several rooms are designated containment sites, each holding materials that must never share an accessible zone with the materials at another containment site. After the works, these sites must be **mutually isolated**: for every pair of containment sites, there must be no remaining path of unsealed corridors connecting them. This ensures each site ends up in its own separated region of the facility. Rooms that are not containment sites may fall into whichever region the sealing produces — their placement is unconstrained and irrelevant to acceptance.

Each corridor carries a sealing cost that reflects the labour and materials to close it. What is measured is solely the total sealing cost, the sum of the costs of the corridors actually sealed. There is a fixed remediation budget. Choose a set of corridors to seal whose total cost does not exceed the budget and whose removal leaves every pair of containment sites disconnected, or report that no sealing within budget can isolate all sites simultaneously. (Isolating any one pair may be cheap; the budget must cover separating all sites from one another at once.)

## Input
Line 1: four integers n, m, k, B. 
Line 2: k hub ids. 
Next m lines: three integers u v w — a link.

## Output
`YES`, then a line with the number c of removed links, then c lines "u v"; or `NO`.

## Example

**Input**
4 3 3 10
1 2 3
1 4 5
2 4 4
3 4 5

**Output**
YES
2
1 4
2 4
