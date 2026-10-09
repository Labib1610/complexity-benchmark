import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    N, E, F = map(int, input().split())
    targets = set(map(int, input().split()))
    
    adj = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if F <= 1:
        print(0)
        return
    
    # DFS to find minimal subtree connecting all targets
    visited = [False] * (N+1)
    total_cost = 0
    
    def dfs(u, parent):
        nonlocal total_cost
        visited[u] = True
        has_target = u in targets
        for v, w in adj[u]:
            if v == parent:
                continue
            if not visited[v]:
                child_has_target = dfs(v, u)
                if child_has_target:
                    total_cost += w
                has_target = has_target or child_has_target
        return has_target
    
    # Start from any target
    start = next(iter(targets))
    dfs(start, -1)
    
    print(total_cost)

if __name__ == "__main__":
    solve()