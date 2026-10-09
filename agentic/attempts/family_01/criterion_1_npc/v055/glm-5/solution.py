def solve(assigned_count, domains, assignment, k_used):  # k_used = number of colors used so far (prefix invariant)
    if assigned_count == n: return assignment
    # find unassigned vertex with min domain size, tie-break by degree
    ...
    if min domain size == 0: return None
    if min domain size == 1: assign that color (no branching) — actually just loop over the single color.
    if all unassigned have domain ≤ 2: run 2-SAT; if sat, return full assignment; else return None.
    for color in colors(v) ∩ {1..k+1} (as bits, ordered maybe by least used?):
        assign, propagate (reduce neighbors' domains; if any becomes 0 → fail)
        recurse
        undo