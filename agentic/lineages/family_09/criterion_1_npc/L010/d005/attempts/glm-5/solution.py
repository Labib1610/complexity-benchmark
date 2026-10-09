import sys
import numpy as np

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1]); k = int(data[2])
    adj = [0] * n
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1; v = int(data[idx+1]) - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    # Quick greedy attempts to find independent set of size >= k (optional speedup)
    # ... maybe skip or simple.
    
    h = n // 2
    r = n - h
    # L = vertices 0..h-1 (bit i), R = vertices h..n-1 (bit j = v-h)
    
    # adjacency within L (bits 0..h-1), from L to R (bits 0..r-1), within R (bits 0..r-1)
    adjL = [0]*h
    adjLR = [0]*h   # neighbors in R, reindexed
    adjR = [0]*r
    for i in range(h):
        adjL[i] = adj[i] & ((1 << h) - 1)
        adjLR[i] = adj[i] >> h
    for j in range(r):
        adjR[j] = (adj[h + j] >> h)  # neighbors within R
    
    sizeL = 1 << h
    sizeR = 1 << r
    
    # misR table
    misR = np.zeros(sizeR, dtype=np.uint8)
    fullR = sizeR - 1
    for v in range(r-1, -1, -1):
        base = 1 << v
        step = base << 1
        mask_v = fullR ^ adjR[v]
        # dst = base::step ; src indices = 0, step, 2step, ...
        nsrc = (sizeR - base + step - 1) // step  # = 2^{r-1-v}
        src = np.arange(0, sizeR - base, step, dtype=np.int64)
        excl = misR[:sizeR-base:step]           # view: misR[src]
        incl = misR[src & mask_v] + 1
        misR[base::step] = np.maximum(excl, incl)
    ...