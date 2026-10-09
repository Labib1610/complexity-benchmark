import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    # Node encoding: variable i (1-based) -> nodes 2*(i-1) for x_i true, 2*(i-1)+1 for x_i false
    # For value v: if v > 0: node 2*(v-1); if v < 0: node 2*(-v-1)+1
    # Clause (a or b): edges neg(a) -> b, neg(b) -> a. neg(node) = node ^ 1.
    
    N = 2 * n
    # Build adjacency lists using arrays (CSR format) for speed
    # First count degrees
    ea = [0] * (2 * m)  # edge sources
    eb = [0] * (2 * m)  # edge destinations
    
    def lit_node(v):
        if v > 0:
            return 2 * (v - 1)
        else:
            return 2 * (-v - 1) + 1
    
    ecnt = 0
    for _ in range(m):
        l1 = int(data[idx]); idx += 1
        l2 = int(data[idx]); idx += 1
        a = lit_node(l1)
        b = lit_node(l2)
        # edge a^1 -> b, b^1 -> a
        ea[ecnt] = a ^ 1; eb[ecnt] = b; ecnt += 1
        ea[ecnt] = b ^ 1; eb[ecnt] = a; ecnt += 1
    
    # Build CSR
    deg = [0] * (N + 1)
    for i in range(ecnt):
        deg[ea[i]] += 1
    # prefix sums
    start = [0] * (N + 1)
    for i in range(N):
        start[i+1] = start[i] + deg[i]
    adj = [0] * ecnt
    pos = start[:]  # copy of start[0..N-1]
    # Actually pos should be per-node fill pointer
    fill = list(start[:N])  # fill[i] = current fill position for node i
    for i in range(ecnt):
        u = ea[i]
        adj[fill[u]] = eb[i]
        fill[u] += 1
    
    # ... then SCC