import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    total_critical = t
    visited = [False] * (n+1)
    ans = 0
    
    def dfs(u, parent):
        nonlocal ans
        visited[u] = True
        cnt = 1 if u in critical else 0
        for v, w in adj[u]:
            if v == parent:
                continue
            if not visited[v]:
                sub = dfs(v, u)
                if sub > 0 and sub < total_critical:
                    ans += w
                cnt += sub
        return cnt
    
    # start from any critical node
    start = next(iter(critical))
    dfs(start, -1)
    
    print(ans)

if __name__ == "__main__":
    solve()