import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    db = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    visited = [False] * (n + 1)
    
    def dfs(u):
        visited[u] = True
        cnt = 1 if u in db else 0
        total_cost = 0
        for v, w in adj[u]:
            if not visited[v]:
                sub_cnt, sub_cost = dfs(v)
                if sub_cnt > 0:
                    total_cost += sub_cost + w
                    cnt += sub_cnt
        return cnt, total_cost
    
    # Start from any database node if exists, else any node
    start = next(iter(db)) if db else 1
    _, ans = dfs(start)
    print(ans)

if __name__ == "__main__":
    solve()