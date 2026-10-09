import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    active = set(map(int, input().split()))
    
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
    
    # DFS to count active nodes in subtree and compute cost
    visited = [False] * (n + 1)
    total_cost = 0
    
    def dfs(u, parent):
        nonlocal total_cost
        visited[u] = True
        cnt = 1 if u in active else 0
        for v, w in adj[u]:
            if v == parent:
                continue
            child_cnt = dfs(v, u)
            if child_cnt > 0 and child_cnt < t:
                total_cost += w
            cnt += child_cnt
        return cnt
    
    # Start DFS from any active node
    start = next(iter(active))
    dfs(start, -1)
    
    print(total_cost)

if __name__ == "__main__":
    solve()