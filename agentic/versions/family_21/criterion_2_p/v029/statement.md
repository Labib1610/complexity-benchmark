# Problem B — Securing Two Sites

Time limit: 2 s   Memory limit: 256 MB

## Description
A research facility consists of zones joined by passages. Each passage carries a closure expense reflecting the labour and materials needed to block it permanently. Two particular zones are containment sites whose materials must never again share an accessible region: after the remediation, it must be impossible to travel from one of these sites to the other using unblocked passages. A passage, once blocked, permits no transit at all in either direction.

Zones other than the two sites may end up in any accessible region — their placement is unconstrained and plays no part in whether the plan is accepted. What is measured is solely the total closure expense, the sum of the expenses of the passages actually blocked. There is a fixed remediation budget that this total must not exceed.

Choose a set of passages to block whose total expense is within the budget and whose removal ensures the two sites can no longer reach each other, or report that no in-budget blocking can achieve this.

## Input
Line 1: five integers n, m, s, t, B. 
Next m lines: three integers u v w — representing a passage between zone u and zone v with closure expense w.

## Output
`YES`, then a line with the number c of removed passages, then c lines "u v"; or `NO`.

## Example

### Input
4 5 1 4 11
1 2 5
1 3 6
2 4 7
3 4 8
2 3 2

### Output
YES
2
1 2
1 3
