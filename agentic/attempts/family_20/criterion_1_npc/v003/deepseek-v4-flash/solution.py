import sys
sys.setrecursionlimit(1000000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Find bridges using Tarjan's algorithm
    tin = [-1] * n
    low = [-1] * n
    timer = 0
    is_bridge = [False] * m
    
    def dfs_bridge(v, p_edge):
        nonlocal timer
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in adj[v]:
            if eid == p_edge:
                continue
            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                dfs_bridge(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    is_bridge[eid] = True
    
    for i in range(n):
        if tin[i] == -1:
            dfs_bridge(i, -1)
    
    if any(is_bridge):
        print("NO")
        return
    
    # The graph is bridgeless cubic → 3-edge-coloring exists.
    # We'll find it by backtracking with MRV heuristic.
    
    color = [0] * m
    used_mask = [0] * n  # bit 0 for color 1, bit 1 for color 2, bit 2 for color 3
    
    # Precompute for each edge its endpoints
    edge_u = [e[0] for e in edges]
    edge_v = [e[1] for e in edges]
    
    # To speed up, maintain a list of uncolored edges
    uncolored = list(range(m))
    
    def backtrack():
        if not uncolored:
            return True
        
        # Find edge with minimal legal options
        best_idx = -1
        best_options = 0
        best_mask = 0
        for idx in uncolored:
            u = edge_u[idx]
            v = edge_v[idx]
            mask = used_mask[u] | used_mask[v]
            legal = (~mask) & 0b111
            if legal == 0:
                return False
            opt_count = bin(legal).count("1")
            if best_idx == -1 or opt_count < best_options:
                best_idx = idx
                best_options = opt_count
                best_mask = legal
                if opt_count == 1:
                    break
        
        # Remove best_idx from uncolored
        uncolored.remove(best_idx)
        u = edge_u[best_idx]
        v = edge_v[best_idx]
        
        # Try each legal color
        for c in range(3):
            bit = 1 << c
            if best_mask & bit:
                color[best_idx] = c + 1
                used_mask[u] |= bit
                used_mask[v] |= bit
                if backtrack():
                    return True
                used_mask[u] ^= bit
                used_mask[v] ^= bit
                color[best_idx] = 0
        
        uncolored.append(best_idx)
        return False
    
    if backtrack():
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()