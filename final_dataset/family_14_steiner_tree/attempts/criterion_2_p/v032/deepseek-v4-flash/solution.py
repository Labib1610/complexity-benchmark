import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    parent = [0] * (n + 1)
    parent_w = [0] * (n + 1)
    order = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    for node in order:
        for nei, w in adj[node]:
            if not visited[nei]:
                visited[nei] = True
                parent[nei] = node
                parent_w[nei] = w
                order.append(nei)
    
    cnt = [0] * (n + 1)
    for node in range(1, n + 1):
        if node in critical:
            cnt[node] = 1
    
    total = 0
    for node in reversed(order):
        if node != 1:
            if cnt[node] > 0 and (t - cnt[node]) > 0:
                total += parent_w[node]
            cnt[parent[node]] += cnt[node]
    
    print(total)

if __name__ == "__main__":
    solve()