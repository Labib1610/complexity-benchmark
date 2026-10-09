# Problem B — Resonance Suppression

Time limit: 2 s
Memory limit: 256 MB

## Description
An archaeological expedition is analyzing an array of $n$ ancient monoliths. The site is characterized by $m$ bidirectional harmonic resonances, each linking a specific pair of monoliths. When a resonance is active, it acts as a conduit, allowing energetic fluctuations to oscillate freely between the two linked monoliths. These fluctuations can propagate through any succession of active conduits to transfer between monoliths that are not directly linked.

To secure the site, the expedition can neutralize these conduits. Neutralizing a given resonance completely severs the energetic link between the two monoliths it connects. However, this process consumes suppression wards, and the exact quantity of wards needed to neutralize a conduit depends on its inherent strength.

The expedition has been allocated a strict inventory of $B$ suppression wards. A valid security protocol involves selecting a subset of conduits to neutralize such that the total number of wards consumed across all selected conduits is at most $B$.

A critical hazard exists involving two particular monoliths, identified by the indices $s$ and $t$. Should energetic fluctuations find any succession of active conduits to travel between $s$ and $t$, an uncontrollable feedback loop will trigger. The security protocol must ensure that absolutely no succession of active conduits remains that could allow energy to transfer between these two specific monoliths. Whether energy can transfer between any other monoliths is of no consequence. Your task is to find a set of conduits to neutralize that fulfills this safety mandate without exceeding the ward inventory, or to determine that the site cannot be secured with the available resources.

## Input
The first line contains five integers: $n$, $m$, $s$, $t$, and $B$.
Each of the subsequent $m$ lines contains three integers $u$, $v$, and $w$. This indicates a bidirectional resonance linking monolith $u$ and monolith $v$, which requires exactly $w$ suppression wards to neutralize.

## Output
If a security protocol can be established, print `YES` on the first line. On the second line, print an integer $c$, representing the number of conduits to neutralize. On each of the following $c$ lines, print two integers $u$ and $v$ to specify a neutralized resonance. If multiple valid protocols exist that require at most $B$ wards in total, any of them is acceptable.
If it is impossible to secure the site within the $B$ ward inventory, print `NO`.

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
