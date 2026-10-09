# Problem A — Deactivating a Facility into Distinct Accessible Areas

Time limit: 5 s   Memory limit: 256 MB

## Description
A research facility is a network of rooms joined by corridors, each corridor carrying a deactivation expense that reflects the labour and materials to close it permanently. Several rooms are designated chambers, each holding materials that must never share an accessible zone with the materials at another designated chamber. The remediation team will deactivate a chosen set of corridors; a corridor, once deactivated, no longer permits passage in either direction.

After the works, the designated chambers must be unable to reach one another: for every pair of designated chambers, there must be no remaining sequence of active corridors connecting them, so each chamber ends up in its own distinct accessible area of the facility. Rooms that are not designated chambers may fall into whichever area the deactivation produces — their placement is unconstrained and irrelevant to acceptance. What is measured is solely the total deactivation expense, the sum of the expenses of the corridors actually deactivated.

There is a fixed remediation budget. Choose a set of corridors to deactivate whose total expense does not exceed the budget and whose removal leaves every pair of designated chambers without any sequence of active corridors between them, or report that no deactivation within budget can separate all chambers from one another at once. (Separating any one pair may be cheap; the budget must cover separating all chambers from one another at once.)

## Input
Line 1: four integers n, m, k, B. Line 2: k designated chamber ids. Next m lines: three integers u v w — a corridor.

## Output
`YES`, then a line with the number c of deactivated corridors, then c lines "u v"; or `NO`.

## Example
**Input:**
```text
4 3 3 20
1 2 3
1 4 10
2 4 10
3 4 10
```

**Output:**
```text
YES
2
1 4
2 4
```
