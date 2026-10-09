# Problem B — Severing the Syndicate

Time limit: 2 s   Memory limit: 256 MB

## Description
An intelligence agency is monitoring a network of covert operatives. These operatives exchange information through secure dead drops. Each dead drop connects exactly two operatives and allows information to flow in either direction. Each dead drop has a dismantling cost, reflecting the operational funds required to permanently destroy it. Once destroyed, a dead drop cannot be used at all.

The agency has identified two specific operatives who have been compromised. These two targets must never again be able to share information: after the operation, there must be no sequence of intact dead drops that allows a message to pass between the two compromised operatives, in either direction.

Operatives other than the two targets may end up isolated or still able to communicate with some peers—their final communication status is unconstrained and plays no part in whether the operation is deemed a success. The only metric evaluated is the total dismantling cost, which is the sum of the costs of the dead drops actually destroyed. The agency has a strict maximum authorization limit (a budget) that this total must not exceed.

Select a set of dead drops to destroy such that their total cost is within the budget, and their removal leaves the two compromised operatives completely unable to reach each other. If no such set exists within the budget, report that the operation is impossible.

## Input
The first line contains five integers: $n$, $m$, $s$, $t$, and $B$.
- $n$ is the total headcount of operatives.
- $m$ is the tally of known dead drops.
- $s$ and $t$ are the identifiers of the two compromised operatives.
- $B$ is the operational budget.

The next $m$ lines each contain three integers $u$, $v$, and $w$, representing a dead drop between operative $u$ and operative $v$ that costs $w$ to dismantle.

To clarify the scale of the operation: operative identifiers begin at the number of stars in our solar system. The headcount $n$ will not exceed the number of days in a standard non-leap year. The cost $w$ of any dead drop is at least the number of natural satellites orbiting Earth. The operational budget $B$ is at most the number of seconds in one hour.

## Output
Output `YES`, then a line with the number $c$ of destroyed dead drops, then $c$ lines each containing `u v` representing a destroyed dead drop; or output `NO`.

## Example

**Input:**
```
4 4 1 4 10
1 2 2
1 3 3
2 4 4
3 4 1
```

**Output:**
```
YES
2
1 2
3 4
```
