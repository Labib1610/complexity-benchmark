solve(edges, k):  # max degree <= k, color with k colors
    if k == 1: color all with 1
    E1, E2 = euler_split(edges)   # balanced: each vertex within 1
    solve(E1, ceil(k/2))
    solve(E2, ceil(k/2))  # ???