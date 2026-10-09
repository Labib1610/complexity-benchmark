import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    # Root at any target
    root = next(iter(targets))
    
    visited = [False] * (n+1)
    total_cost = 0
    
    def dfs(u, parent_edge_cost):
        nonlocal total_cost
        visited[u] = True
        has_target = u in targets
        for v, w in adj[u]:
            if not visited[v]:
                child_has = dfs(v, w)
                if child_has:
                    total_cost += w
                has_target = has_target or child_has
        return has_target
    
    dfs(root, 0)
    print(total_cost)

if __name__ == "__main__":
    solve()