import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to find needed edges
    visited = [False] * (n+1)
    needed = [False] * (n+1)  # whether node is in the minimal subtree
    
    def dfs(u):
        visited[u] = True
        has_target = u in targets
        for v, w in adj[u]:
            if not visited[v]:
                child_has = dfs(v)
                if child_has:
                    needed[v] = True
                has_target = has_target or child_has
        return has_target
    
    # Start from any target
    start = next(iter(targets))
    dfs(start)
    
    total_cost = 0
    for u, v, w in edges:
        if needed[u] or needed[v]:
            total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    solve()