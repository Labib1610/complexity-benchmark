import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    centers = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to count centers in subtree and total cost
    visited = [False] * (n + 1)
    center_count = [0] * (n + 1)
    total_cost = 0
    
    stack = [(1, -1)]
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = []
    
    # iterative DFS to get order
    stack = [1]
    visited[1] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_weight[v] = w
                stack.append(v)
    
    # process in reverse order
    for u in reversed(order):
        if u in centers:
            center_count[u] += 1
        if parent[u] != 0:
            center_count[parent[u]] += center_count[u]
            if center_count[u] > 0 and (t - center_count[u]) > 0:
                total_cost += parent_weight[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()