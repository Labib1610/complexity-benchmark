read n, m, k
read edges
build CSR adjacency (both directions)
BFS coloring: color[v] ∈ {0,1}, component id comp[v], per-component counts cnt[comp][color]
S = Σ_comp max(cnt0, cnt1)
if S >= k:
    # pick from larger side of each component
    collect vertices: for each component, the side with more vertices (ties → either)
    take first k → output YES + them
else:
    run Hopcroft-Karp (A = color 0 as left, B = color 1 as right) with early abort if matching > n - k
    if aborted: print NO
    else:
        M = matching size
        # M <= n - k, so IS size n - M >= k
        König construction → IS
        output YES + first k of IS