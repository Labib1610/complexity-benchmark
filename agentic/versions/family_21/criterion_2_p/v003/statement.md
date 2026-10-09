# Problem B — Sealing Two Sites Apart

Time limit: 2 s   Memory limit: 256 MB

## Description
A research facility is a collection of rooms joined by bidirectional corridors, each corridor carrying a sealing cost that reflects the labour and materials needed to close it permanently. Two particular rooms are containment sites whose materials must never again share an accessible region: after the remediation, there must be no sequence of unsealed corridors that allows travel between the two sites. A corridor, once sealed, permits no passage at all.

Rooms other than the two sites may end up accessible to either site or neither — their status is unconstrained and plays no part in whether the plan is accepted. What is measured is solely the total sealing cost, the sum of the costs of the corridors actually sealed. There is a fixed remediation budget that this total must not exceed.

Choose a set of corridors to seal whose total cost is within the budget and whose closure ensures the two containment sites cannot reach each other, or report that no in-budget sealing can achieve this.

## Input
Line 1: five integers $n$, $m$, $s$, $t$, $B$. 
Next $m$ lines: three integers $u$ $v$ $w$ — a corridor between room $u$ and room $v$ with sealing cost $w$.

## Output
`YES`, then a line with the number $c$ of sealed corridors, then $c$ lines "$u$ $v$"; or `NO`.

## Example

### Input
```text
4 5 1 4 10
1 2 5
1 3 6
2 4 5
3 4 5
2 3 2
```

### Output
```text
YES
2
2 4
3 4
```
