import sys
import numpy as np

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1]); k = int(data[2])
    # adjacency bitmasks
    adj = [0] * n
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1; v = int(data[idx+1]) - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    # Quick check: if k <= ... hmm, also if k > n: impossible (but k <= n given).
    
    n1 = (n + 1) // 2  # A: vertices 0..n1-1
    n2 = n - n1       # B: vertices n1..n-1
    
    FULL_A = (1 << n1) - 1
    
    # f DP over subsets of A
    # f[T] = max IS in induced subgraph on T (T subset of A)
    f = np.zeros(1 << n1, dtype=np.int8)  # f[0] = 0
    # base arange for index computation
    # We'll compute idx arrays per step.
    for j in range(n1):
        size = 1 << j
        # N_j = adj[j] & (bits < j) = adj[j] & (size - 1)... adj[j] restricted to A vertices < j
        Nj = adj[j] & ((1 << j) - 1)  # neighbors of vertex j among A vertices 0..j-1
        # idx = R & ~Nj for R in [0, size)
        # compute arange & mask
        r = np.arange(size, dtype=np.int64)  # hmm, recomputed each step: total sum 2^23 int64 = 67MB total alloc over time; fine
        idxs = r & (~Nj)  # careful: ~Nj on Python int is negative; use r & (FULL_low ^ Nj)
        ...
    ...