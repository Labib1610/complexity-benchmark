import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    N_in = int(next(it))
    N_out = int(next(it))
    M = int(next(it))
    
    edges = []
    for _ in range(M):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
    
    # Degrees for transmitters (1..N_in) and receivers (1..N_out)
    deg_in = [0] * (N_in + 1)
    deg_out = [0] * (N_out + 1)
    
    for u, v in edges:
        deg_in[u] += 1
        deg_out[v] += 1
    
    D = max(max(deg_in[1:]), max(deg_out[1:])) if M > 0 else 0
    
    # Build bipartite graph with edge indices
    adj_in = [[] for _ in range(N_in + 1)]
    adj_out = [[] for _ in range(N_out + 1)]
    for i, (u, v) in enumerate(edges):
        adj_in[u].append((v, i))
        adj_out[v].append((u, i))
    
    # Find Eulerian trails in the directed graph
    # Graph: in_nodes 1..N_in, out_nodes N_in+1..N_in+N_out
    # Edge i: u -> v+N_in
    total_nodes = N_in + N_out + 1
    adj = [[] for _ in range(total_nodes)]
    deg = [0] * total_nodes
    
    for i, (u, v) in enumerate(edges):
        v_node = v + N_in
        adj[u].append((v_node, i))
        deg[u] += 1
        deg[v_node] -= 1
    
    # Find starting nodes for trails (out-degree > in-degree)
    start_nodes = []
    for u in range(1, N_in + 1):
        if deg[u] > 0:
            for _ in range(deg[u]):
                start_nodes.append(u)
    
    # If no imbalance, start from any node with edges
    if not start_nodes and M > 0:
        for u in range(1, N_in + 1):
            if adj_in[u]:
                start_nodes.append(u)
                break
    
    edge_used = [False] * M
    answer = [0] * M
    
    # Iterative Hierholzer's algorithm
    for start in start_nodes:
        if edge_used.count(False) == 0:
            break
        
        stack = [start]
        path = []
        ptr = [0] * total_nodes
        
        while stack:
            u = stack[-1]
            while ptr[u] < len(adj[u]) and edge_used[adj[u][ptr[u]][1]]:
                ptr[u] += 1
            if ptr[u] < len(adj[u]):
                v, e_idx = adj[u][ptr[u]]
                edge_used[e_idx] = True
                stack.append(v)
                u = v
            else:
                path.append(stack.pop())
        
        # Assign phases along the trail
        phase = 1
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            # Find the edge index for u -> v
            for j in range(len(adj[u])):
                v2, e_idx = adj[u][j]
                if v2 == v and answer[e_idx] == 0:
                    answer[e_idx] = phase
                    phase = 3 - phase
                    break
    
    # Handle any remaining edges (shouldn't happen if graph is Eulerian)
    for i in range(M):
        if answer[i] == 0:
            answer[i] = 1
    
    print("YES")
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    solve()