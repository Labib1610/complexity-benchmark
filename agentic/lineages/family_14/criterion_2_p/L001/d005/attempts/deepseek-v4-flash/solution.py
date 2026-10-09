import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    primary = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to count primary nodes in subtree
    parent = [0]*(n+1)
    pweight = [0]*(n+1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                pweight[v] = w
                stack.append(v)
    
    cnt = [0]*(n+1)
    for u in primary:
        cnt[u] = 1
    
    total_cost = 0
    for u in reversed(order):
        if u == 1:
            continue
        if cnt[u] > 0:
            total_cost += pweight[u]
        cnt[parent[u]] += cnt[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()