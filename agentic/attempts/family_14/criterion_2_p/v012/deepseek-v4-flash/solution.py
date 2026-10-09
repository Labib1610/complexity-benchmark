import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    priority = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    visited = [False] * (n + 1)
    total_cost = 0
    
    def dfs(u):
        visited[u] = True
        cnt = 1 if u in priority else 0
        for v, w in adj[u]:
            if not visited[v]:
                sub = dfs(v)
                if sub > 0 and sub < t:
                    total_cost += w
                cnt += sub
        return cnt
    
    # start from any priority node
    start = next(iter(priority))
    dfs(start)
    
    print(total_cost)

if __name__ == "__main__":
    solve()