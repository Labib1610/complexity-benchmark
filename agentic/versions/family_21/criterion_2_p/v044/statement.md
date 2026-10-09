# Problem B — Decoherence Intervention

Time limit: 2 s   Memory limit: 256 MB

## Description
A quantum processor's behavior is modeled as a system of $n$ eigenstates. Its evolution is governed by $m$ resonant couplings, each permitting bidirectional oscillation between a specific pair of eigenstates. Left unchecked, these couplings can propagate errors across the system. We can intervene by applying localized dampening fields to suppress specific couplings.

Finding a safe configuration requires searching the boolean hypercube $\{0,1\}^m$ of all possible dampening strategies. A single point in this $2^m$-size intervention space defines exactly which couplings are suppressed and which remain active. To evaluate the safety of a given intervention, one must compute the transitive closure of the active couplings to determine the resulting connected components of the eigenstate space. Designing a global partition of the eigenstates into arbitrary isolated clusters requires evaluating the reachability matrix across these $2^m$ configurations.

Your objective is to locate a valid intervention in this $2^m$-dimensional space. An intervention is considered valid if it satisfies two conditions:
1. The total energy required to apply the dampening fields for the suppressed couplings must not exceed a strict budget $B$.
2. The intervention must strictly isolate the initialization eigenstate $s$ from the failure eigenstate $t$. That is, in the resulting transitive closure, there must be no valid sequence of active couplings connecting $s$ and $t$.

Determine if a valid intervention exists. If one does, output it. If no such point in the configuration space satisfies both constraints, report that it is impossible.

## Input
Line 1: five integers $n$, $m$, $s$, $t$, and $B$.
Next $m$ lines: three integers $u$, $v$, and $w$, indicating a resonant coupling that allows bidirectional oscillation between eigenstate $u$ and eigenstate $v$, requiring $w$ units of energy to suppress.

## Output
If a valid intervention exists, output `YES` on the first line. On the second line, output the number of suppressed couplings $c$. On the next $c$ lines, output the two eigenstates $u$ and $v$ for each suppressed coupling. If multiple valid interventions exist, any one is acceptable.
If no valid intervention exists, output `NO`.

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
