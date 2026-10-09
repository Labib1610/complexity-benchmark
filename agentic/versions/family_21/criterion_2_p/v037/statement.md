# Problem B — Sealing Two Sites Apart

Time limit: 2 s   Memory limit: 256 MB

## Description
A research facility is a network of rooms joined by corridors, each corridor carrying a sealing cost that reflects the labour and materials needed to close it permanently. Two particular rooms are containment sites whose materials must never again share an accessible region: after the remediation, there must be no path of unsealed corridors between the two sites, in either direction. A corridor, once sealed, permits no passage at all.

Rooms other than the two sites may end up on either side of the eventual partition — their placement is unconstrained and plays no part in whether the plan is accepted. What is measured is solely the total sealing cost, the sum of the costs of the corridors actually sealed. There is a fixed remediation budget that this total must not exceed.

Choose a set of corridors to seal whose total cost is within the budget and whose removal leaves the two sites disconnected, or report that no in-budget sealing can separate them.

## Input
Line 1: five integers representing the total room inventory $n$, the corridor count $m$, the two site identifiers $s$ and $t$, and the available funds $B$. 
Next $m$ lines: three integers $u$ $v$ $w$ — a link between room $u$ and room $v$ with sealing cost $w$.

## Output
`YES`, then a line with the number $c$ of removed links, then $c$ lines "$u$ $v$"; or `NO`.

## Example

**Input**
```
4 5 1 4 12
1 2 4
1 3 8
2 3 2
2 4 6
3 4 5
```

**Output**
```
YES
2
2 4
3 4
```
