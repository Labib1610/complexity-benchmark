# Problem B — Resonance Suppression

Time limit: 2 s
Memory limit: 256 MB

## Description
A planetary archaeology team is studying $n$ ancient monoliths. Between certain pairs of monoliths, there exist bi-directional harmonic resonances. There are $m$ such resonances in total. Energy can transfer freely back and forth between any two monoliths that share an active resonance, and this energy can cascade through any sequence of active resonances to reach other monoliths.

The team has the technology to permanently deactivate these resonances. Deactivating a specific resonance requires deploying a certain number of dampening fields, which completely stops any energy transfer across it. The exact number of dampening fields required varies for each resonance.

The expedition's supply ship has delivered a total of $B$ dampening fields. The total cost of any deployment plan is the sum of the dampening fields required for the specifically deactivated resonances. This total must not exceed the limit of $B$ fields.

The primary safety directive concerns two specific monoliths, designated $s$ and $t$. If energy were to cascade between these two monoliths, the resulting feedback loop would be catastrophic. The team must formulate a deployment plan that guarantees no sequence of active resonances exists that could carry energy between monolith $s$ and monolith $t$. The connectivity of all other monoliths is irrelevant. Determine a valid set of resonances to deactivate, or conclude that the safety directive cannot be met with the current supplies.

## Input
The first line contains five integers: $n$, $m$, $s$, $t$, and $B$.
The next $m$ lines each contain three integers $u$, $v$, and $w$, indicating a bi-directional resonance between monolith $u$ and monolith $v$ that requires $w$ dampening fields to deactivate.

## Output
If a valid deployment plan exists, print `YES` on the first line. On the second line, print an integer $c$, the number of resonances to deactivate. On each of the next $c$ lines, print two integers $u$ and $v$ representing a deactivated resonance. If there are multiple valid plans, any one that uses at most $B$ fields is acceptable.
If no such plan exists within the limit of $B$ fields, print `NO`.

## Example

### Input
```
4 4 1 4 10
1 2 4
1 3 8
2 4 5
3 4 2
```

### Output
```
YES
2
1 2
3 4
```
