# Phase C: Collision Isolation

Time limit: 2 s
Memory limit: 256 MB

The facility's automated resonator stabilization procedure runs in four distinct phases:

- **Phase A (Logging):** The diagnostic array monitors $n$ resonators and identifies $m$ active bidirectional resonance channels between pairs of them.
- **Phase B (Polarization):** The controller tries to apply either a positive or negative polarity to each resonator. For stability, no two resonators connected by a resonance channel can hold the same polarity.
- **Phase C (Isolation):** If the array cannot be safely polarized, the controller interrupts the process to find a localized failure. The simplest unpolarizable structure is a "closed feedback loop" consisting of exactly three resonators, where every resonator in the loop shares an active channel with both of the others. Because all three mutually interact, two polarities are insufficient.
- **Phase D (Purge):** The isolated feedback loop is physically decoupled from the main array.

Your task is to implement the software for Phase C. The controller has already failed Phase B and aborted. It is guaranteed that at least one closed feedback loop exists in the Phase A logs. You must locate one.

To guarantee predictable behavior during Phase D, your isolation module must format the loop as a sequence of three resonator IDs $a, b,$ and $c$ in strictly increasing order ($a < b < c$). Should the logs contain more than one valid feedback loop, you must return the one that comes first lexicographically (the loop with the lowest value for $a$; in the event of a tie, the lowest $b$; and if still tied, the lowest $c$).

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the total number of resonators and the number of active resonance channels. Resonators are numbered from 1 to $n$.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that an active resonance channel exists between resonator $u$ and resonator $v$. Each channel is recorded at most once.
It is guaranteed that the logs contain at least one closed feedback loop of three resonators.

## Output
Output three integers $a$, $b$, and $c$, separated by spaces, on a single line such that $a < b < c$. These three resonators must all share active channels with one another (i.e., $a$ interacts with $b$, $a$ interacts with $c$, and $b$ interacts with $c$). Output the lexicographically first valid loop.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
