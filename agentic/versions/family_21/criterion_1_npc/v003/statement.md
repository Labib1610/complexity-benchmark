# Problem A — Sealing a Facility into Isolated Containment Zones

Time limit: 5 s
Memory limit: 256 MB

## Description
A research facility consists of $n$ rooms. Certain pairs of rooms have a direct bidirectional passage between them, each carrying a sealing cost that reflects the labour and materials to close it permanently. Exactly $k$ rooms are designated containment sites, each holding materials that must never be able to mix with the materials at another containment site. The remediation team will seal a chosen set of passages; a passage, once sealed, no longer permits movement between its two rooms in either direction.

After the works, the containment sites must be **mutually isolated**: for every pair of containment sites, there must be no sequence of unsealed passages connecting them (a sequence connects two rooms if it starts at one, ends at the other, and consecutive passages in the sequence share a room). Rooms that are not containment sites may fall into whichever accessible group of rooms the sealing produces — their placement is unconstrained and irrelevant to acceptance. What is measured is solely the total sealing cost, the sum of the costs of the passages actually sealed.

There is a fixed remediation budget $B$. Choose a set of passages to seal whose total cost does not exceed the budget and whose removal leaves every pair of containment sites mutually isolated according to the rules above, or report that no sealing within budget can isolate all sites simultaneously. (Isolating any one pair may be cheap; the budget must cover separating all sites from one another at once.)

## Input
Line 1: four integers $n$, $m$, $k$, $B$.
Line 2: $k$ containment site ids.
Next $m$ lines: three integers $u$, $v$, $w$ — a passage between room $u$ and room $v$ with sealing cost $w$.

## Output
`YES`, then a line with the number $c$ of removed passages, then $c$ lines "$u\ v$"; or `NO`.

## Example 1

### Input
```
4 3 3 12
1 2 3
1 4 6
2 4 6
3 4 6
```

### Output
```
YES
2
1 4
2 4
```

## Example 2

### Input
```
4 3 3 10
1 2 3
1 4 6
2 4 6
3 4 6
```

### Output
```
NO
```
