import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    R, S, P = map(int, input().split())
    priority = set(map(int, input().split()))
    
    adj = [[] for _ in range(R + 1)]
    for _ in range(S):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    visited = [False] * (R + 1)
    
    def dfs(u):
        visited[u] = True
        has_priority = u in priority
        total_cost = 0
        for v, w in adj[u]:
            if not visited[v]:
                child_has, child_cost = dfs(v)
                if child_has:
                    total_cost += w + child_cost
                    has_priority = True
        return has_priority, total_cost
    
    # Start from any priority node
    start = next(iter(priority))
    _, cost = dfs(start)
    print(cost)

if __name__ == "__main__":
    solve()