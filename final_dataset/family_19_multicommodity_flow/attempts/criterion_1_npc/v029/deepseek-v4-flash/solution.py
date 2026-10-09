import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    items = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        items.append((s, t, d))
    
    edges = []
    adj = [[] for _ in range(n)]
    for j in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
        adj[u].append((v, j))
    
    # We'll do DFS over commodities, assigning flows on edges.
    # For each commodity, we need to send d units from s to t.
    # We'll try all possible flow decompositions (paths) respecting remaining capacities.
    
    # To keep it simple, we'll use a recursive search that tries to send flow along paths.
    # We'll maintain remaining capacity for each edge.
    
    rem = [cap for _,_,cap in edges]
    flow_assign = [[0]*m for _ in range(k)]
    
    # Precompute all simple paths for each commodity? That could be huge.
    # Instead, we'll do a DFS that tries to push flow along any path from s to t,
    # using remaining capacities, and backtrack if fails.
    
    def dfs_commodity(idx):
        if idx == k:
            return True
        s, t, d = items[idx]
        # Try to send d units from s to t using current rem capacities
        # We'll use a max flow from s to t with current rem capacities,
        # but we need integer flows. We'll use DFS path augmentation.
        # Since d is small, we can send unit by unit.
        # But we need to assign flows to edges for this commodity.
        # We'll do a recursive path search.
        
        # We'll try to find d paths (or a flow) from s to t.
        # Use a simple DFS to find a path with positive remaining capacity,
        # push 1 unit, record, and repeat.
        # If at any point we can't send all d, backtrack.
        
        # We'll store the edges used for this commodity temporarily.
        temp_flow = [0]*m
        
        def send_units(remaining):
            if remaining == 0:
                return True
            # find a path from s to t with all edges having rem > 0
            # BFS/DFS
            parent = [-1]*n
            parent_edge = [-1]*n
            stack = [s]
            visited = [False]*n
            visited[s] = True
            while stack:
                u = stack.pop()
                if u == t:
                    break
                for v, eidx in adj[u]:
                    if not visited[v] and rem[eidx] > 0:
                        visited[v] = True
                        parent[v] = u
                        parent_edge[v] = eidx
                        stack.append(v)
            if not visited[t]:
                return False
            # reconstruct path
            path_edges = []
            cur = t
            while cur != s:
                eidx = parent_edge[cur]
                path_edges.append(eidx)
                cur = parent[cur]
            # push 1 unit along path
            for eidx in path_edges:
                rem[eidx] -= 1
                temp_flow[eidx] += 1
            if send_units(remaining - 1):
                return True
            # backtrack
            for eidx in path_edges:
                rem[eidx] += 1
                temp_flow[eidx] -= 1
            return False
        
        if send_units(d):
            # success for this commodity
            for j in range(m):
                flow_assign[idx][j] = temp_flow[j]
            if dfs_commodity(idx + 1):
                return True
            # backtrack: restore rem
            for j in range(m):
                rem[j] += temp_flow[j]
            return False
        else:
            return False
    
    if dfs_commodity(0):
        print("YES")
        for i in range(k):
            print(' '.join(str(flow_assign[i][j]) for j in range(m)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()