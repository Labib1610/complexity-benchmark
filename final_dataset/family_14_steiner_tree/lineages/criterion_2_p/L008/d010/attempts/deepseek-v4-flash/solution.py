import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    R, S, P = map(int, input().split())
    mandated = set(map(int, input().split()))
    
    adj = [[] for _ in range(R + 1)]
    edges = []
    for _ in range(S):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to find necessary edges
    parent = [0] * (R + 1)
    parent_weight = [0] * (R + 1)
    visited = [False] * (R + 1)
    stack = [1]
    visited[1] = True
    order = []
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_weight[v] = w
                stack.append(v)
    
    # Count mandated nodes in each subtree
    cnt = [0] * (R + 1)
    for node in mandated:
        cnt[node] = 1
    
    total_cost = 0
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u != 1:
            p = parent[u]
            cnt[p] += cnt[u]
            if cnt[u] > 0 and cnt[u] < P:
                total_cost += parent_weight[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()