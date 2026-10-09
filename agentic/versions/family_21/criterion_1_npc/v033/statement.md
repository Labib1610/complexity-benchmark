# Problem A — Sealing a Facility into Isolated Containment Zones

Time limit: 5 s   Memory limit: 256 MB

## Description
A research facility consists of rooms. Certain pairs of rooms have a corridor between them, each carrying a sealing cost that reflects the labour and materials to close it permanently. Several rooms are designated containment sites, each holding materials that must never mix with the materials at another containment site. The remediation team will seal a chosen set of corridors; a corridor, once sealed, no longer permits passage in either direction.

After the works, if an entity starts at any containment site and repeatedly moves between rooms through unsealed corridors, it must be impossible for it to ever arrive at any other containment site. Rooms that are not containment sites may fall into whichever accessible area the sealing produces — their placement is unconstrained and irrelevant to acceptance. What is measured is solely the total sealing cost, the sum of the costs of the corridors actually sealed.

There is a fixed remediation budget. Choose a set of corridors to seal whose total cost does not exceed the budget and whose removal ensures the movement condition above is met, or report that no sealing within budget can achieve this for all sites simultaneously. (Preventing travel between any one pair may be cheap; the budget must cover preventing travel between all pairs of sites at once.)

## Input
Line 1: four integers n, m, k, B.
Line 2: k containment site ids.
Next m lines: three integers u v w — a corridor connecting room u and room v with a sealing cost of w.

## Output
`YES`, then a line with the number c of sealed corridors, then c lines "u v"; or `NO`.

## Example

### Example Input
```
4 3 3 40
1 2 3
1 4 10
2 4 20
3 4 30
```

### Example Output
```
YES
2
1 4
2 4
```
