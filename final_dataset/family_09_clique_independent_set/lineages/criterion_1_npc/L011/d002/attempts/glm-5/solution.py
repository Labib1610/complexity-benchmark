size = 1 << h2
g = np.zeros(size, dtype=np.int8)
full = size - 1
for j in range(h2 - 1, -1, -1):
    cnt = 1 << (h2 - 1 - j)
    S = np.arange(cnt, dtype=np.int32) << (j + 1)
    np.bitwise_and(S, inv_j, out=tmp)  # tmp = S & inv_j, need buffer
    a = g[S]          # gather
    b = g[tmp]         # gather
    b += 1
    np.maximum(a, b, out=b)
    g[(1 << j) + S] = b   # scatter