def search(U, F):  # U: candidates for I (undecided, and independent-compatible), F: excluded from I
    # G[F] must be bipartite (checked incrementally)
    if not bipartite(G[F]): return None
    if U empty: return I if bipartite(G[F]) else None
    pick v in U (smart choice)
    # branch 1: v in I
    result = search(U - {v} - N(v), F ∪ N(v)) with I += v
    # branch 2: v not in I
    result = search(U - {v}, F ∪ {v})