# Problem B — Sealing Two Sites Apart

Time limit: 2 s   Memory limit: 256 MB

## Description
A research facility is a network of rooms joined by corridors, each corridor carrying a sealing cost that reflects the labour and materials needed to close it permanently. You must evaluate the $2^m$ possible subsets of corridors and select a configuration to seal permanently. A corridor, once sealed, permits no passage at all. The chosen subset must satisfy the structural property that two particular rooms (the containment sites) never again share an accessible region: after the remediation, there must be no path of unsealed corridors between them, in either direction.

Rooms other than the two sites may end up on either side of the eventual partition — their placement is unconstrained and plays no part in whether the plan is accepted. What is measured is solely the total sealing cost, the sum of the costs of the corridors actually sealed. There is a fixed remediation budget that this total must not exceed.

Choose a valid subset of corridors to seal whose total cost is within the budget, or report that no such in-budget configuration exists.

## Input
Line 1: five integers $n$, $m$, $s$, $t$, $B$. Next $m$ lines: three integers $u$ $v$ $w$ — a link.

## Output
`YES`, then a line with the number $c$ of removed links, then $c$ lines "$u$ $v$"; or `NO`.

## Example

### Input
```
4 4 1 4 10
1 2 2
1 3 5
2 4 6
3 4 2
```

### Output
```
YES
2
1 2
3 4
```
