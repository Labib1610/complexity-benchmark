import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx+=1
    m = int(input_data[idx]); idx+=1
    
    # node for literal: positive v -> 2*(v-1)+1, negative v -> 2*(|v|-1)
    # edges: for clause (a, b): add edge not(a) -> b, not(b) -> a
    N = 2*n
    # Build adjacency using arrays (CSR) for speed
    # First count edges
    ea = [0]*m  # edge sources
    eb = [0]*m  # edge dests
    head = [0]*(N+1)
    
    def node(l):
        if l > 0:
            return 2*(l-1)+1
        else:
            return 2*(-l-1)
    
    def neg(u):
        return u ^ 1
    
    edges_src = [0]*(2*m)
    edges_dst = [0]*(2*m)
    for i in range(m):
        l1 = int(input_data[idx]); idx+=1
        l2 = int(input_data[idx]); idx+=1
        a = node(l1); b = node(l2)
        # not a -> b, not b -> a
        edges_src[2*i] = a^1
        edges_dst[2*i] = b
        edges_src[2*i+1] = b^1
        edges_dst[2*i+1] = a
    
    # Build CSR
    deg = [0]*(N)
    for s in edges_src:
        deg[s]+=1
    start = [0]*(N+1)
    for u in range(N):
        start[u+1] = start[u] + deg[u]
    pos = start[:]  # copy, but we need start[u]..start[u+1] range; use a moving pointer
    adj = [0]*(2*m)
    fill = start[:N]  # fill[u] current position... hmm, need list of size N
    for i in range(2*m):
        u = edges_src[i]
        adj[fill[u]] = edges_dst[i]
        fill[u]+=1