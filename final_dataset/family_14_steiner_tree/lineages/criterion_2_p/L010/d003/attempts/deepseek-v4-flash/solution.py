import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    specials = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # DFS to count special nodes in subtree and total weight
    visited = [False] * (n+1)
    total_weight = 0
    
    def dfs(u, parent):
        nonlocal total_weight
        visited[u] = True
        cnt = 1 if u in specials else 0
        for v, w in adj[u]:
            if v == parent:
                continue
            child_cnt = dfs(v, u)
            if child_cnt > 0:
                total_weight += w
            cnt += child_cnt
        return cnt
    
    # Start from any special node
    start = next(iter(specials))
    dfs(start, -1)
    
    print(total_weight)

if __name__ == "__main__":
    solve()