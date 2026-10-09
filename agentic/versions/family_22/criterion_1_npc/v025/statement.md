# Problem A — Arcane Synchronisation

Time limit: 5 s   Memory limit: 256 MB

## Description
The Grand Coven is preparing for a celestial alignment. They must perform a sequence of $n$ distinct arcane rituals before the alignment ends. The alignment lasts for exactly $T$ moon phases. 

The Coven has $M$ High Mystics available. During any single moon phase, each Mystic can perform at most one ritual. Consequently, the total number of rituals that can be conducted in a single moon phase is capped by the number of Mystics; there is no benefit to leaving a Mystic idle, but there is also no penalty beyond the $T$ moon phases deadline.

The rituals are bound by magical resonance. There are $m$ resonance rules dictating the order of execution. Each rule specifies that a certain ritual generates a spiritual residue required by another ritual. If ritual $a$ must precede ritual $b$, then ritual $a$ must be performed in a strictly earlier moon phase than ritual $b$ — being performed in the same moon phase is insufficient, as the spiritual residue only stabilizes at the end of the phase. Mystics do not possess individual specialties; any Mystic can perform any ritual, and only the moon phase in which a ritual takes place matters.

To ensure the stability of the alignment, it is guaranteed that the maximum number of times any single ritual acts as a prerequisite across all rules is at most $m$. Furthermore, the sum of all ritual identifiers across all $m$ rules (summing both $a$ and $b$ for all rules) will not exceed $2 \cdot m \cdot n$.

Assign every ritual a moon phase within the $T$ phases so that all resonance rules hold and no moon phase is assigned more rituals than there are Mystics, or report that the sequence cannot be finished in time. (With few Mystics, the per-phase capacity and the resonance chains pull against each other, so a sequence that respects resonance may still overflow the capacity and vice versa.)

## Input
First line: four integers $n$, $M$, $T$, $m$. 
Each of the next $m$ lines: two integers $a$ and $b$ — ritual $a$ must finish before ritual $b$ starts.

## Output
Print `YES` followed by $n$ integers (the moon phase of each ritual, from $1$ to $T$); otherwise print `NO`.

## Example

### Input
```
5 2 3 4
1 3
2 3
3 4
3 5
```

### Output
```
YES
1 1 2 3 3
```
