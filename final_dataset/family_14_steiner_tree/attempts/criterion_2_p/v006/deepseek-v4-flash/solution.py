import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    hubs = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to mark nodes that are in the minimal subtree connecting all hubs
    visited = [False] * (n + 1)
    has_hub = [False] * (n + 1)
    
    def dfs(u, parent):
        visited[u] = True
        if u in hubs:
            has_hub[u] = True
        for v, w in adj[u]:
            if v != parent and not visited[v]:
                dfs(v, u)
                if has_hub[v]:
                    has_hub[u] = True
    
    # Start DFS from any hub
    start = next(iter(hubs))
    dfs(start, -1)
    
    total_cost = 0
    for u, v, w in edges:
        if has_hub[u] and has_hub[v]:
            total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    solve()