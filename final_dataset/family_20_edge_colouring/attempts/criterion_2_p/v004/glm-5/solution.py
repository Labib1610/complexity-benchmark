color(E, k):  # Δ(E) ≤ k, colors available: 1..k
  if k == 1: assign color 1 to all edges (Δ(E) ≤ 1)
  else:
    # make all degrees even by adding dummy edges (to new dummy vertices, or between existing? dummy edges must keep bipartiteness; add dummy vertices dL, dR and dummy edges as needed)
    E' = E + dummy edges making every original vertex have even degree
    (E1', E2') = Euler split of E'
    E1 = E1' minus dummy edges, E2 = E2' minus dummy edges
    # now Δ(E1), Δ(E2) ≤ ceil(Δ(E)/2) ≤ ceil(k/2)
    color(E1, ceil(k/2)) with colors 1..ceil(k/2)
    color(E2, floor(k/2)) with colors ceil(k/2)+1..k