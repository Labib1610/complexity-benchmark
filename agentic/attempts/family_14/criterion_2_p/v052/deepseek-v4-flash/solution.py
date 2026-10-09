import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    terminals = set(map(int, input().split()))
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    visited = [False] * (n + 1)
    total_cost = 0
    
    def dfs(u):
        nonlocal total_cost
        visited[u] = True
        cnt = 1 if u in terminals else 0
        for v, w in adj[u]:
            if not visited[v]:
                sub_cnt = dfs(v)
                if 0 < sub_cnt < t:
                    total_cost += w
                cnt += sub_cnt
        return cnt
    
    dfs(1)
    print(total_cost)

if __name__ == "__main__":
    solve()