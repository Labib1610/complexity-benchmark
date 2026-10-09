import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    # nodes: 2*(v) for x_v true, 2*v+1 for x_v false, v in [0, n)
    N = 2 * n
    
    # Build edges
    # For each clause (a, b): edge (a^1 -> b), (b^1 -> a)
    # We'll count degrees then build CSR.
    
    # First, parse clauses into arrays la, lb (literal node indices)
    # literal node: l > 0 -> 2*(l-1); l < 0 -> 2*(-l-1)+1
    
    # Let's collect edges as pairs.
    num_edges = 2 * m
    # Parse
    # We can compute edge endpoints directly.
    
    # Build CSR
    deg = [0] * (N + 1)
    edges_u = [0] * num_edges
    edges_v = [0] * num_edges
    e = 0
    for _ in range(m):
        l1 = int(data[idx]); idx += 1
        l2 = int(data[idx]); idx += 1
        if l1 > 0:
            a = 2 * (l1 - 1)
        else:
            a = 2 * (-l1 - 1) + 1
        if l2 > 0:
            b = 2 * (l2 - 1)
        else:
            b = 2 * (-l2 - 1) + 1
        # edges: a^1 -> b, b^1 -> a
        u1 = a ^ 1; v1 = b
        u2 = b ^ 1; v2 = a
        edges_u[e] = u1; edges_v[e] = v1; e += 1
        edges_u[e] = u2; edges_v[e] = v2; e += 1
    
    for i in range(num_edges):
        deg[edges_u[i] + 1] += 1
    # prefix sum
    for i in range(N):
        deg[i+1] += deg[i]
    # deg[i] now = start index for node i... wait, deg has size N+1, deg[u+1] counts. After prefix, deg[u] = start of node u's edges, deg[u+1] = end.
    adj = [0] * num_edges
    pos = deg[:]  # copy for filling — but careful, we need deg intact for start positions. Actually we can fill using a temp pointer array.
    ...