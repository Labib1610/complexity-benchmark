import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    n_in, n_out, m = map(int, input_data[:3])
    edges = []
    adj_in = [[] for _ in range(n_in + 1)]
    adj_out = [[] for _ in range(n_out + 1)]
    
    idx = 3
    for i in range(m):
        u = int(input_data[idx]); v = int(input_data[idx+1])
        idx += 2
        edges.append((u, v))
        adj_in[u].append((v, i))
        adj_out[v].append((u, i))
    
    # Compute D
    D = 0
    for u in range(1, n_in + 1):
        D = max(D, len(adj_in[u]))
    for v in range(1, n_out + 1):
        D = max(D, len(adj_out[v]))
    
    color = [0] * m
    
    # Greedy edge coloring for bipartite graph
    # We'll use a simple algorithm: for each edge, find smallest available color
    # that is not used by any adjacent edge.
    # To do this efficiently, we maintain used colors per vertex.
    
    used_in = [set() for _ in range(n_in + 1)]
    used_out = [set() for _ in range(n_out + 1)]
    
    for i, (u, v) in enumerate(edges):
        # Find smallest color not used by u or v
        c = 1
        while c in used_in[u] or c in used_out[v]:
            c += 1
        color[i] = c
        used_in[u].add(c)
        used_out[v].add(c)
    
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color)) + "\n")

if __name__ == "__main__":
    solve()