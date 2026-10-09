b = number of vertices in B
full = (1 << b) - 1
g = np.zeros(1 << b, dtype=np.int8)  # g[full] = 0; others filled
# adjacency within B: adjB[v] = bitmask over B vertices (neighbors of B-vertex v within B)
for v in range(b-1, -1, -1):
    bit = 1 << v
    closed = bit | adjB[v]   # closed neighborhood within B
    # T with lowest missing bit v: T = (2^v - 1) + 2^{v+1} * h, h in [0, 2^{b-v-1})
    cnt = 1 << (b - v - 1)
    base = (1 << v) - 1
    stride = 1 << (v + 1)
    # U = T | bit = (2^{v+1} - 1) + stride * h
    U = np.arange(cnt, dtype=np.int64) * stride + ((1 << (v+1)) - 1)
    # hmm, U as index array
    g[base::stride]??