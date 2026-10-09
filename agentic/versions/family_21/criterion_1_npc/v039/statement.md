# Problem A — Securing a Water Network from Contamination Mixing

Time limit: 5 s   Memory limit: 256 MB

## Description
A municipal water system consists of junctions connected by bidirectional pipes, each pipe carrying a capping cost that reflects the excavation and materials required to block it permanently. Several junctions are designated as distinct contamination sources, each introducing a unique chemical. Mixing any two unique chemicals causes a catastrophic reaction, meaning no two sources can share an active fluid path. The engineering team will cap a chosen set of pipes; a pipe, once capped, no longer permits fluid flow in either direction.

After the intervention, the contamination sources must be mutually isolated: for every pair of sources, there must be no remaining path of uncapped pipes connecting them, so each source ends up in its own separated sub-network. Junctions that are not sources may fall into whichever sub-network the capping produces — their placement is unconstrained and irrelevant to safety. What is measured is solely the total capping cost, the sum of the costs of the pipes actually capped.

There is a fixed emergency budget. Choose a set of pipes to cap whose total cost does not exceed the budget and whose closure leaves every pair of sources disconnected, or report that no intervention within budget can isolate all sources simultaneously.

## Input
Line 1: four integers $n$, $m$, $k$, $B$. 
Line 2: $k$ source ids. 
Next $m$ lines: three integers $u$ $v$ $w$ — a pipe.

## Output
`YES`, then a line with the number $c$ of removed pipes, then $c$ lines "$u$ $v$"; or `NO`.

## Example
**Input**
```
4 3 3 6
1 2 3
1 4 2
2 4 3
3 4 4
```
**Output**
```
YES
2
1 4
2 4
```
