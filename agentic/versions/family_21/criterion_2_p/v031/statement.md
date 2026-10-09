# Problem B — Disconnecting Two Servers

Time limit: 2 s   Memory limit: 256 MB

## Description
An enterprise architecture is a network of servers joined by communication channels, each channel carrying a disabling cost that reflects the administrative overhead needed to close it permanently. Two particular servers are critical nodes whose data must never again share an accessible region: after the remediation, there must be no path of active channels between the two nodes, in either direction. A channel, once disabled, permits no passage at all.

Servers other than the two critical nodes may end up on either side of the eventual partition — their placement is unconstrained and plays no part in whether the plan is accepted. What is measured is solely the total disabling cost, the sum of the costs of the channels actually disabled. There is a fixed remediation budget that this total must not exceed.

Choose a set of channels to disable whose total cost is within the budget and whose removal leaves the two nodes disconnected, or report that no in-budget disabling can separate them. (Isolating exactly two designated nodes operates on different structural principles than dividing a network into many components — procedures designed for multiple components are unnecessary here, and a solver that reaches for them will apply an unneeded structure.)

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
2 4 7
3 4 4
```
### Output
```text
YES
2
1 2
3 4
```
