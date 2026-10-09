import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    vital = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    visited = [False] * (n + 1)
    total = 0
    
    def dfs(u, parent):
        nonlocal total
        cnt = 1 if u in vital else 0
        for v, w in adj[u]:
            if v == parent:
                continue
            sub_cnt = dfs(v, u)
            if sub_cnt > 0 and sub_cnt < t:
                total += w
            cnt += sub_cnt
        return cnt
    
    # start from any node
    start = next(iter(vital))
    dfs(start, -1)
    print(total)

if __name__ == "__main__":
    solve()