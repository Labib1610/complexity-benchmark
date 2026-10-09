import sys
import numpy as np

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1]); k = int(data[2])
    adj = [0] * n
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1; v = int(data[idx+1]) - 1; idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    b = n // 2
    a = n - b
    A_MASK = (1 << a) - 1
    B_MASK = (1 << b) - 1  # local bits for B
    
    # local adjacency
    # A vertices: 0..a-1 (absolute same as local)
    # B vertices: absolute a+v, local bit v
    cnbA = [0]*a   # closed neighborhood within A (local bits)
    comp_cnbA = np.empty(a, dtype=np.uint32)
    for i in range(a):
        cnb = (adj[i] & A_MASK) | (1 << i)
        cnbA[i] = cnb
        comp_cnbA[i] = B_MASK...