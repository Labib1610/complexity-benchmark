# Problem B — State Space Intervention

Time limit: 2 s   Memory limit: 256 MB

## Description
A quantum computing system operates by transitioning between $n$ distinct quantum states. There are $m$ allowed phase shifts, each allowing the system to oscillate symmetrically between two specific states. To stabilize the system, we can apply localized dampening fields to suppress certain phase shifts. Suppressing a phase shift requires a specific amount of energy.

The configuration space of possible dampening strategies is vast. For $m$ phase shifts, there are $2^m$ possible subsets of shifts that could be suppressed. Evaluating a given subset typically involves determining the transitive closure of the remaining allowed transitions to see how the state space partitions. Finding an optimal global partition of the states into arbitrary isolated groups is a complex combinatorial optimization problem. 

Your task is to explore this space of $2^m$ possible interventions and identify a subset of phase shifts to suppress. A valid subset must satisfy two conditions: its total required energy must not exceed a strict threshold $B$, and it must successfully prevent state $s$ from transitioning to state $t$ through any sequence of unsuppressed phase shifts. The states $s$ and $t$ must end up completely isolated from one another.

If there is a valid subset of phase shifts whose total dampening energy is at most $B$ and which prevents any transition sequence between $s$ and $t$, you must output it. If no such subset exists within the energy threshold, report that it is impossible.

## Input
Line 1: five integers $n$, $m$, $s$, $t$, $B$. 
Next $m$ lines: three integers $u$ $v$ $w$ — representing a phase shift that allows symmetric oscillation between state $u$ and state $v$, requiring $w$ units of energy to suppress.

## Output
`YES`, then a line with the number $c$ of suppressed phase shifts, then $c$ lines each containing the two states $u$ and $v$ of a suppressed phase shift; or `NO`. If multiple valid strategies exist, any one that meets the conditions is acceptable.

## Example

### Input
```text
4 4 1 4 10
1 2 4
1 3 5
2 4 6
3 4 3
```

### Output
```text
YES
2
1 2
3 4
```
