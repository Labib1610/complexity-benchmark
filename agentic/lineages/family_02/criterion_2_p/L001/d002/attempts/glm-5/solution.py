import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    # nodes: 2n total. node 2i = x_i true, 2i+1 = x_i false
    N = 2 * n
    # Build adjacency using arrays (CSR format) for speed
    # First count out-degrees
    head = [0] * (N + 1)  # will use CSR
    
    # literals
    # For each clause (a, b): edges: neg(a) -> b, neg(b) -> a
    # neg of node v is v^1
    # literal l: if l>0: node 2*(l-1); if l<0: node 2*(-l-1)+1
    
    edges = []
    # We'll store edges as list of (u, v) then build CSR.
    # To be fast, compute node indices directly.
    
    us = [0] * (2 * m)
    vs = [0] * (2 * m)
    
    for j in range(m):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        # node for a
        if a > 0:
            na = 2 * (a - 1)
        else:
            na = 2 * (-a - 1) + 1
        if b > 0:
            nb = 2 * (b - 1)
        else:
            nb = 2 * (-b - 1) + 1
        # edge na^1 -> nb, nb^1 -> na
        us[2*j] = na ^ 1
        vs[2*j] = nb
        us[2*j+1] = nb ^ 1
        vs[2*j+1] = na
    
    # Build CSR
    deg = [0] * N
    for u in us:
        deg[u] += 1
    # prefix sums
    start = [0] * (N + 1)
    for i in range(N):
        start[i+1] = start[i] + deg[i]
    adj = [0] * (2 * m)
    pos = start[:]  # copy of start[0..N-1]
    for i in range(2 * m):
        u = us[i]
        adj[pos[u]] = vs[i]
        pos[u] += 1
    
    # Iterative Tarjan
    # ...