import sys
import numpy as np

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1]); k = int(data[2])
    # adjacency bitmasks (global 0-indexed)
    adj = [0] * n
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1; v = int(data[idx+1]) - 1; idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    n1 = n // 2
    n2 = n - n1
    fullR = (1 << n2) - 1
    fullL = (1 << n1) - 1
    
    # local adjacency for R
    adjR = [0] * n2   # adjR[j] = mask over R-local of neighbors of global vertex n1+j within R
    for j in range(n2):
        g = n1 + j
        adjR[j] = adj[g] >> n1   # neighbors in R: global bits n1..n-1 → shift; but adj[g] may include L bits — shifting right by n1 drops them. ✓
    # local adjacency for L
    adjL = [0] * n1
    for i in range(n1):
        adjL[i] = adj[i] & fullL
    # cross adjacency: for L vertex i, mask over R-local of neighbors in R
    crossR = [0] * n1
    for i in range(n1):
        crossR[i] = adj[i] >> n1
    
    # ---- best[] over R ----
    sizeR = 1 << n2
    best = np.zeros(sizeR, dtype=np.uint8)
    for v in range(n2 - 1, -1, -1):
        U = n2 - 1 - v
        cnt = 1 << U
        step = 1 << (v + 1)
        s_arr = np.arange(cnt, dtype=np.uint32)
        av = adjR[v] >> (v + 1)
        b_idx = (s_arr & np.uint32(~av & 0xFFFFFFFF)) << np.uint32(v + 1)
        # hmm, careful with numpy uint32 bitwise not and shifts
        B = best[b_idx]
        A = best[::step]
        best[(1 << v)::step] = np.maximum(A, B + np.uint8(1))
    ...