import numpy as np

n, m given. Edges list (0-indexed).

N = 1 << n

# adjacency degrees
deg = [0]*n
adjmask = [0]*n
for a,b in edges: adjmask[a] |= 1<<b; adjmask[b] |= 1<<a; deg[a]+=1; deg[b]+=1

# w[S] for all S
w = np.zeros(N, dtype=np.int64)
# degsum part:
for v in range(n):
    if deg[v]:
        w.reshape(-1, 2, 1 << v)[:, 1, :] += deg[v]
# subtract 2*E[S]:
for a, b in edges:
    if a > b: a, b = b, a
    # bits a < b
    shape = (1 << (n-1-b), 2, 1 << (b-a-1), 2, 1 << a)
    w.reshape(shape)[:, 1, :, 1, :] -= 2