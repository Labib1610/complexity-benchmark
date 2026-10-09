# Problem B — Sealing Two Sites Apart

Time limit: 2 s   Memory limit: 256 MB

## Description
A research facility is a network of rooms joined by corridors, each corridor carrying a sealing cost that reflects the labour and materials needed to close it permanently. A corridor, once sealed, permits no passage at all.

What is measured is solely the total sealing cost, the sum of the costs of the corridors actually sealed. There is a fixed remediation budget that this total must not exceed. The placement of most rooms is unconstrained; they may end up on either side of the eventual partition, which plays no part in whether the plan is accepted.

The objective of the plan is to isolate two particular rooms which are containment sites. Their materials must never again share an accessible region: after the remediation, there must be no path of unsealed corridors between the two sites, in either direction. Choose a set of corridors to seal whose total cost is within the budget and whose removal leaves the two sites disconnected, or report that no in-budget sealing can separate them.

## Input
Line 1: five integers n, m, s, t, B. Next m lines: three integers u v w — a link.

## Output
`YES`, then a line with the number c of removed links, then c lines "u v"; or `NO`.

## Example

### Input
```text
4 4 1 4 10
1 2 5
1 3 6
2 4 4
3 4 8
```

### Output
```text
YES
2
2 4
1 3
```
