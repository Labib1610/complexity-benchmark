# Emergency Egg Relocation

Time limit: 2 s   Memory limit: 256 MB

## Description
A sudden flood threatens an ant colony's nursery chamber. The worker ants must relocate a specific number of eggs from the flooded nursery to a safe surface chamber in a single, coordinated evacuation dash.

The colony is a network of chambers connected by one-way tunnels. Because the tunnels are narrow and structurally fragile, each tunnel has a strict upper limit on the number of eggs that can be safely carried through it during the dash. A tunnel cannot be widened or augmented during the evacuation.

On every tunnel, the assigned number of eggs must be a non-negative whole number that does not exceed that tunnel's limit. At every chamber other than the nursery and the surface, the eggs are conserved: the number of eggs carried into an intermediate chamber must exactly equal the number carried out, so no eggs accumulate or vanish in transit. At the nursery, the net departure of eggs into the tunnels must exactly equal the required relocation target, and at the surface chamber, the net arrival must match it.

The time it takes to crawl, the length of the tunnels, and the exact sequence of ants are not part of this calculation and must be ignored — only the tunnel limits, the strict in-and-out balance at intermediate chambers, and the total number of eggs that must be evacuated bind the answer.

Determine a valid assignment of how many eggs should pass through each tunnel to successfully relocate the target number of eggs, or report that this volume cannot be evacuated in a single dash. (Myrmecologists sometimes look for complex multi-caste behaviors here; with only one type of egg to move, the shared-tunnel contention that makes the general problem hard simply does not arise.)

## Input
Line 1: `n m 1`. (Where `n` is the number of chambers, `m` is the number of tunnels, and `1` indicates a single type of egg).
Next line: `s t d`. (Where `s` is the nursery chamber ID, `t` is the surface chamber ID, and `d` is the target number of eggs).
Next `m` lines: `u v cap`. (Representing a one-way tunnel from chamber `u` to chamber `v` with an upper limit of `cap` eggs).

## Output
`YES` then one line with `m` integers — the number of eggs routed through tunnel `j` (in input order); or `NO`.

## Example
**Input**
```
4 5 1
1 4 3
1 2 2
1 3 2
2 3 1
2 4 1
3 4 2
```

**Output**
```
YES
1 2 0 1 2
```
