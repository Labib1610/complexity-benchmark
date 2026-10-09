import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    keys = set(map(int, input().split()))
    
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    parent = [-1] * n
    parent_edge_weight = [0] * n
    order = [0]
    for u in order:
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            parent_edge_weight[v] = w
            order.append(v)
    
    subtree_key_count = [0] * n
    for u in reversed(order):
        if u in keys:
            subtree_key_count[u] += 1
        if parent[u] != -1:
            subtree_key_count[parent[u]] += subtree_key_count[u]
    
    total_cost = 0
    for u in range(1, n):
        cnt = subtree_key_count[u]
        if 0 < cnt < t:
            total_cost += parent_edge_weight[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()