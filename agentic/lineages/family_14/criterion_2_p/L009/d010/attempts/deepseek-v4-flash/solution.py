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
    
    if F == 1:
        print(0)
        return
    
    visited = [False] * (N+1)
    
    def dfs(u):
        visited[u] = True
        has_target = u in targets
        total_cost = 0
        for v, w in adj[u]:
            if not visited[v]:
                child_has_target, cost = dfs(v)
                if child_has_target:
                    total_cost += w + cost
                    has_target = True
                else:
                    total_cost += cost
        return has_target, total_cost
    
    _, ans = dfs(1)
    print(ans)

if __name__ == "__main__":
    solve()