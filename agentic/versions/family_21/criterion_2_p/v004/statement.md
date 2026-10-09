# Problem B — Sealing Two Sites Apart

Time limit: 2 s   Memory limit: 256 MB

## Description
A research facility is a network of rooms joined by corridors, each corridor carrying a sealing cost that reflects the labour and materials needed to close it permanently. A remediation plan consists of choosing a subset of corridors to seal, which partitions the facility. Since there are $m$ corridors, there are $2^m$ possible sealing plans to consider. A plan is accepted if it breaks the connectivity between two particular containment sites: there must be no path of unsealed corridors between them, in either direction. A corridor, once sealed, permits no passage at all.

Rooms other than the two sites may end up in any of the resulting disconnected regions — their placement is unconstrained and plays no part in whether the plan is accepted. What is measured is solely the total sealing cost, the sum of the costs of the corridors actually sealed. There is a fixed remediation budget that this total must not exceed.

Search the space of possible sealing configurations to find a set of corridors to seal whose total cost is within the budget and whose removal leaves the two sites disconnected, or report that no in-budget sealing can separate them.

## Input
Line 1: five integers n, m, s, t, B. Next m lines: three integers u v w — a link.

## Output
`YES`, then a line with the number c of removed links, then c lines "u v"; or `NO`.

## Example

**Input:**
```
4 5 1 4 10
1 2 4
1 3 3
2 4 4
3 4 5
2 3 2
```

**Output:**
```
YES
2
1 2
1 3
```
