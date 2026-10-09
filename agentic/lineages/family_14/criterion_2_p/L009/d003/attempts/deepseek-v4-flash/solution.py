import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    N, E, F = map(int, input().split())
    flagged = set(map(int, input().split()))
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if F == 1:
        print(0)
        return
    
    visited = [False] * (N + 1)
    total_cost = 0
    
    def dfs(u):
        nonlocal total_cost
        visited[u] = True
        has_flagged = u in flagged
        for v, w in adj[u]:
            if not visited[v]:
                child_has_flagged = dfs(v)
                if child_has_flagged:
                    total_cost += w
                    has_flagged = True
        return has_flagged
    
    # Start from any flagged node
    start = next(iter(flagged))
    dfs(start)
    print(total_cost)

if __name__ == "__main__":
    solve()