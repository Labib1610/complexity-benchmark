# Problem A — Sealing a Facility into Isolated Containment Zones

Time limit: 5 s   Memory limit: 256 MB

## Description
A research facility remediation project involves three stages: initial surveying, zone isolation planning, and final decontamination. 

The initial survey has mapped the facility as a network of rooms joined by corridors, each corridor carrying a sealing cost that reflects the labour and materials to close it permanently. The survey also identified several rooms as designated containment sites (hubs). Each hub holds materials that must never share an accessible zone with the materials at another hub.

Your task is the second stage: zone isolation planning. The remediation team will seal a chosen set of corridors; a corridor, once sealed, no longer permits passage in either direction. After the works, the hubs must be **mutually isolated**: for every pair of hubs, there must be no remaining path of unsealed corridors connecting them, so each hub ends up in its own separated region of the facility. Rooms that are not hubs may fall into whichever region the sealing produces — their placement is unconstrained and irrelevant to acceptance. What is measured is solely the total sealing cost, the sum of the costs of the corridors actually sealed.

There is a fixed remediation budget allocated for this stage. Choose a set of corridors to seal whose total cost does not exceed the budget and whose removal leaves every pair of hubs disconnected, or report that no sealing within budget can isolate all hubs simultaneously. (Isolating any one pair may be cheap; the budget must cover separating all hubs from one another at once.)

Once this stage concludes, the third stage begins, during which teams will independently decontaminate each separated region based on your plan.

## Input
Line 1: four integers n, m, k, B. 
Line 2: k hub ids. 
Next m lines: three integers u v w — a link.

## Output
`YES`, then a line with the number c of removed links, then c lines "u v"; or `NO`.

## Example

### Input
```
4 3 3 10
1 2 3
1 4 4
2 4 4
3 4 4
```

### Output
```
YES
2
1 4
2 4
```
