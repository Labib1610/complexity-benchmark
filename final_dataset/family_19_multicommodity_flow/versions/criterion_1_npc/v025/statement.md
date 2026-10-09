# Problem A — Concurrent Mana Channeling over a Shared Leyline Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
The Grand Magus needs to execute several complex rituals simultaneously. The realm consists of $n$ magical nexuses connected by $m$ one-way leylines. Each leyline has a strict resonance threshold—a maximum amount of total mana it can safely channel per second.

There are $k$ distinct rituals to be performed. Each ritual requires channeling a specific, indivisible quantity of its own unique aspect of mana from an invocation nexus to a target nexus. Because all rituals are performed concurrently, their mana currents must share the same leylines. The resonance threshold of a leyline applies to the combined sum of all mana aspects passing through it; the rituals compete for the shared threshold even though their mana aspects remain distinct. The amount of mana of any aspect channeled through any leyline must be a non-negative integer.

Mana of each aspect must be independently conserved. For any given ritual, at any nexus that is neither its invocation nor its target, the amount of that ritual's mana entering the nexus must exactly equal the amount leaving it. At a ritual's invocation nexus, the net outward mana (the amount leaving minus the amount entering) of that ritual's aspect must exactly match its required quantity. At its target nexus, the net inward mana (the amount entering minus the amount leaving) of that aspect must exactly match the required quantity.

To ensure the leylines do not fracture, any proposed channeling plan must strictly adhere to the following safety protocols:
- **Aggregate Resonance Limit**: On any given leyline, the combined sum of mana for all rituals must not exceed the leyline's resonance threshold.
- **Single-Aspect Limit**: On any given leyline, the amount of mana for any single ritual's aspect must not exceed the leyline's resonance threshold.
- **Non-Negative Aggregate**: On any given leyline, the combined total of mana across all rituals must not be less than zero.

Determine if there exists a valid channeling plan that satisfies all requirements and protocols, allowing all rituals to be executed in a single second. If so, provide the plan. Otherwise, declare it impossible.

## Input
Line 1 contains three integers: $n$ (nexuses), $m$ (leylines), and $k$ (rituals).
The next $k$ lines each contain three integers: $s_i$ (invocation nexus), $t_i$ (target nexus), and $d_i$ (required mana quantity for ritual $i$).
The next $m$ lines each contain three integers: $u$, $v$, and $cap$, representing a one-way leyline from nexus $u$ to nexus $v$ with a resonance threshold of $cap$.

## Output
If a valid plan exists, print `YES` on the first line. Then, print $k$ lines. The $i$-th of these lines should contain $m$ integers, representing the amount of mana for ritual $i$ channeled through each of the $m$ leylines, in the exact order the leylines were given in the input.
If no valid plan exists, print `NO`.

## Example

**Input**
```text
4 5 2
1 4 15
2 3 5
1 2 10
2 4 10
1 3 10
3 4 10
2 3 5
```

**Output**
```text
YES
10 10 5 5 0
0 0 0 0 5
```
