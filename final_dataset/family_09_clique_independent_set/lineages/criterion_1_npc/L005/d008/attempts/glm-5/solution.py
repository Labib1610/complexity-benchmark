g = [0] * (1 << n1)
for S in range(1, 1 << n1):
    v = (S & -S).bit_length() - 1  # lowest bit index
    g[S] = max(g[S ^ (1 << v)], 1 + g[S & ~adjA[v]])