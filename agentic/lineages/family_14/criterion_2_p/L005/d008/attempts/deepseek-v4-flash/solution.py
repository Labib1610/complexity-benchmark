import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    focus = set(map(int, input().split()))
    
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
    
    parent = [0] * (n + 1)
    parent_edge_cost = [0] * (n + 1)
    order = []
    stack = [next(iter(focus))]
    parent[next(iter(focus))] = -1
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_edge_cost[v] = w
                stack.append(v)
    
    focus_count = [0] * (n + 1)
    for f in focus:
        focus_count[f] = 1
    
    total_cost = 0
    for u in reversed(order):
        if u != next(iter(focus)):
            if focus_count[u] > 0 and focus_count[u] < t:
                total_cost += parent_edge_cost[u]
            if parent[u] != -1:
                focus_count[parent[u]] += focus_count[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()