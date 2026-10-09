import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Root at any critical node
    root = next(iter(critical))
    
    parent = [0]*(n+1)
    parent_edge_weight = [0]*(n+1)
    order = []
    stack = [root]
    parent[root] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_edge_weight[v] = w
                stack.append(v)
    
    # Count critical nodes in subtree
    sub_crit = [0]*(n+1)
    for u in order[::-1]:
        if u in critical:
            sub_crit[u] += 1
        if parent[u] > 0:
            sub_crit[parent[u]] += sub_crit[u]
    
    total_cost = 0
    for u in range(2, n+1):
        if sub_crit[u] > 0 and sub_crit[u] < t:
            total_cost += parent_edge_weight[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()