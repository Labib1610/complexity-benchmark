import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    priority = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    parent = [0] * (n + 1)
    parent_w = [0] * (n + 1)
    order = [1]
    parent[1] = -1
    # BFS/DFS to build parent info
    stack = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_w[v] = w
                stack.append(v)
    
    cnt = [0] * (n + 1)
    for node in priority:
        cnt[node] = 1
    
    total = 0
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u == 1:
            continue
        p = parent[u]
        cnt[p] += cnt[u]
        if cnt[u] > 0 and cnt[u] < t:
            total += parent_w[u]
    
    print(total)

if __name__ == "__main__":
    solve()