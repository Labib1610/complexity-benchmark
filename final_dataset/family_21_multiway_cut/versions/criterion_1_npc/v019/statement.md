# Problem A — Stabilising the Synthesis Pathways

Time limit: 5 s   Memory limit: 256 MB

## Description
A complex biochemical system is modeled as a set of stable intermediate compounds and the reversible transition pathways between them. Each transition pathway requires a specific amount of energy to suppress using a targeted inhibitor. 

Among the compounds, there are $k$ distinct *reactive anchors*. If any two reactive anchors can still transform into one another—either directly or through a chain of intermediate compounds—the entire system will destabilize. To prevent this, you must apply inhibitors to a selected set of transition pathways. Once a pathway is inhibited, compounds can no longer transition along it in either direction.

Compounds that are not reactive anchors can end up in any resulting isolated group; their final grouping does not affect stability. The only requirement is that no sequence of uninhibited pathways allows one reactive anchor to reach another.

You are given an energy quota. Determine a single set of transition pathways to inhibit such that the total energy required does not exceed the quota, and no two reactive anchors remain connected by any valid sequence of transitions. (Isolating any single pair might require little energy, but your chosen set of inhibitors must separate all reactive anchors from one another simultaneously.) If it is impossible to achieve this within the quota, you must report it.

## Input
Line 1: four integers $n$, $m$, $k$, $B$. 
Line 2: $k$ integers — the IDs of the reactive anchors. 
Next $m$ lines: three integers $u$, $v$, $w$ — indicating a transition pathway between compound $u$ and compound $v$ that requires $w$ energy to inhibit.

## Output
If stabilization is possible within the quota, print `YES` on the first line. On the second line, print the number $c$ of pathways you chose to inhibit. Then, print $c$ lines, each containing two integers $u$ and $v$ representing an inhibited pathway. 
If it is not possible, print `NO`.

## Example

**Input:**
```
5 5 3 15
1 3 5
1 2 4
2 3 5
2 4 3
4 5 4
1 5 8
```

**Output:**
```
YES
3
1 2
2 4
1 5
```
