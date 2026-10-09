import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    marked = set(map(int, input().split()))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # DFS to count marked nodes in subtree and sum needed edges
    visited = [False] * n
    total = 0
    
    def dfs(u, parent):
        nonlocal total
        visited[u] = True
        cnt = 1 if u in marked else 0
        for v, w in adj[u]:
            if v == parent:
                continue
            child_cnt = dfs(v, u)
            if child_cnt > 0 and (t - child_cnt) > 0:
                total += w
            cnt += child_cnt
        return cnt
    
    start = next(iter(marked))
    dfs(start, -1)
    print(total)

if __name__ == "__main__":
    solve()