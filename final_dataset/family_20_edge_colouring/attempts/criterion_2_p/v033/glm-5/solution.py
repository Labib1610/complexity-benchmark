color(E, k):  # color edges of subgraph with max degree ≤ k, using colors 1..k (k a power of 2 conceptually)
  if k == 1: assign color 1 to all edges in E (they form a matching)
  else:
    split E into E1, E2 such that max degree of each ≤ ceil(k/2)
    color(E1, ceil(k/2)) with colors 1..ceil(k/2)
    color(E2, ceil(k/2)) with colors ceil(k/2)+1..k