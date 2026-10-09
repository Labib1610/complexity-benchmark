# Phase 3: Resonance Triad Extraction

Time limit: 2 s   Memory limit: 256 MB

The automated particle categorization pipeline consists of four phases:

1. **Observation:** A sensor array monitors $n$ particles and logs $m$ instances of mutual quantum entanglement between pairs of particles.
2. **Spin Assignment:** A heuristic attempts to assign every particle a basic spin state (either Up or Down) such that no two entangled particles share the same spin state.
3. **Anomaly Extraction:** If Phase 2 fails, the system must generate a proof of failure. A fundamental proof of failure is a "resonance triad"—a group of exactly three particles where every particle in the group is entangled with the other two. Because they are mutually entangled, two spin states are never enough.
4. **Stabilization:** The extracted triad is sent to the containment hardware for isolation.

Your task is to implement Phase 3. The Phase 2 heuristic has already determined that the system is unstable, and it is guaranteed that at least one resonance triad exists in the Phase 1 logs. You must identify one such triad.

To ensure deterministic behavior for the containment hardware in Phase 4, your extraction module must format the triad as three particle IDs $a, b,$ and $c$ sorted in ascending order ($a < b < c$). If there are multiple valid triads in the data, you must output the one that is lexicographically first (smallest $a$; in case of a tie, smallest $b$; and if still tied, smallest $c$).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of particles and the number of entangled pairs. Particles are identified by integers from 1 to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that particle $u$ and particle $v$ are entangled. Each entangled pair is logged at most once.
It is guaranteed that at least one resonance triad exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are entangled. Output the lexicographically smallest such triad.

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
