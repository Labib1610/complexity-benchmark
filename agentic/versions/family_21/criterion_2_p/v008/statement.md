# Problem B — Facility Decommissioning: Phase Two

Time limit: 2 s   Memory limit: 256 MB

## Description
A research facility is undergoing a three-stage decommissioning protocol. Phase one, site inventory, has already produced a full map of the network of rooms joined by corridors, assigning each corridor a sealing cost that reflects the labour and materials needed to close it permanently. 

You are responsible for phase two: the partition step. Two particular rooms are containment sites whose materials must never again share an accessible region: after this phase, there must be no path of unsealed corridors between the two sites, in either direction. A corridor, once sealed, permits no passage at all. Rooms other than the two sites may end up on either side of the eventual partition — their placement is unconstrained and plays no part in whether the plan is accepted. What is measured is solely the total sealing cost, the sum of the costs of the corridors actually sealed. There is a fixed remediation budget that this total must not exceed.

Once phase two is complete, phase three (decontamination) will commence on the separated regions, but that is outside your scope. Your task is only to choose a set of corridors to seal whose total cost is within the budget and whose removal leaves the two sites disconnected, or report that no in-budget sealing can separate them.

## Input
Line 1: five integers $n$, $m$, $s$, $t$, $B$.  
Next $m$ lines: three integers $u$, $v$, $w$ — a link between rooms $u$ and $v$ with sealing cost $w$.

## Output
`YES`, then a line with the number $c$ of removed links, then $c$ lines "$u$ $v$"; or `NO`.

## Example
### Input
```
4 5 1 4 10
1 2 4
1 3 5
2 3 2
2 4 4
3 4 5
```
### Output
```
YES
2
1 2
3 4
```
