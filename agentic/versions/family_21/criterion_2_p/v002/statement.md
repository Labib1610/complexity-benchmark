# Problem B — Damming Two Habitats Apart

Time limit: 2 s   Memory limit: 256 MB

## Description
A wetland ecosystem is a system of lakes joined by canals, each canal carrying a damming cost that reflects the labour and materials needed to close it permanently. Two particular lakes are invasive species habitats whose populations must never again share a navigable waterway: after the conservation effort, there must be no path of undammed canals between the two habitats, in either direction. A canal, once dammed, permits no passage at all.

Lakes other than the two habitats may end up on either side of the eventual separation — their placement is unconstrained and plays no part in whether the plan is accepted. What is measured is solely the total damming cost, the sum of the costs of the canals actually dammed. There is a fixed conservation budget that this total must not exceed.

Choose a set of canals to dam whose total cost is within the budget and whose removal leaves the two habitats disconnected, or report that no in-budget damming can separate them. (Separating just two designated habitats is structurally distinct from isolating many at once — the multi-habitat machinery is unnecessary here, and a solver that reaches for it will waste effort on a fundamentally different separation.)

## Input
Line 1: five integers n, m, s, t, B. Next m lines: three integers u v w — a canal.

## Output
`YES`, then a line with the number c of removed canals, then c lines "u v"; or `NO`.

## Example

**Input:**
4 5 1 4 10
1 2 4
1 3 5
2 3 2
2 4 4
3 4 5

**Output:**
YES
2
2 4
3 4
