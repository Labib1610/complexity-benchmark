import sys
sys.setrecursionlimit(300000)

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    required = set(map(int, sys.stdin.readline().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to count required nodes in each subtree
    visited = [False] * (n + 1)
    count = [0] * (n + 1)
    
    def dfs(u):
        visited[u] = True
        cnt = 1 if u in required else 0
        for v, w in adj[u]:
            if not visited[v]:
                cnt += dfs(v)
        count[u] = cnt
        return cnt
    
    # Start DFS from any required node (or 1 if none)
    start = next(iter(required)) if required else 1
    dfs(start)
    
    total_cost = 0
    for u, v, w in edges:
        # Edge is needed if one side has at least one required node and the other side also has at least one
        if count[u] > 0 and count[v] > 0:
            # But we must check if this edge separates required nodes
            # In a tree, if both endpoints have required nodes in their subtrees, the edge is needed
            # We can check: if count[u] != 0 and count[v] != 0 and count[u] != t and count[v] != t
            # Actually simpler: if removing edge splits required nodes into two non-empty sets
            if count[u] != 0 and count[v] != 0 and count[u] != t and count[v] != t:
                total_cost += w
            elif count[u] == t or count[v] == t:
                # If one side contains all required nodes, the other side has none, so not needed
                pass
            else:
                # Both sides have some required nodes
                total_cost += w
    
    # The above logic can be simplified:
    # Edge is needed if count[u] > 0 and count[v] > 0 and (count[u] != t and count[v] != t)
    # But if count[u] == t, then count[v] == 0, so not needed.
    # So condition: count[u] > 0 and count[v] > 0
    
    # Let's redo cleanly:
    total_cost = 0
    for u, v, w in edges:
        if count[u] > 0 and count[v] > 0:
            total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    solve()