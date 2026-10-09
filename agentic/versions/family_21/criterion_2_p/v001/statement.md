# Problem B — Securing Two Sites Apart

Time limit: 2 s   Memory limit: 256 MB

## Description
A research facility is a complex of rooms joined by corridors, each corridor carrying a sealing cost that reflects the labour and materials needed to close it permanently. Two particular rooms are containment sites whose materials must never again share an accessible region: after the remediation, there must be no sequence of unsealed corridors between the two sites, in either direction. A corridor, once sealed, permits no passage at all.

Rooms other than the two sites may end up on either side of the eventual barrier — their placement is unconstrained and plays no part in whether the plan is accepted. What is measured is solely the total sealing cost, the sum of the costs of the corridors actually sealed. There is a fixed remediation budget that this total must not exceed.

Choose a set of corridors to seal whose total cost is within the budget and whose removal leaves the two sites mutually inaccessible, or report that no in-budget sealing can achieve this. (Securing just two designated sites is far more tractable than managing many at once — the multi-site machinery is unnecessary here, and a solver that reaches for it will waste effort on a fundamentally simpler requirement.)

## Input
Line 1: five integers n, m, s, t, B. Next m lines: three integers u v w — a link.

## Output
`YES`, then a line with the number c of removed links, then c lines "u v"; or `NO`.

## Example

### Input
```
4 5 1 4 10
1 2 5
1 3 5
2 4 5
3 4 5
2 3 5
```

### Output
```
YES
2
1 2
1 3
```
