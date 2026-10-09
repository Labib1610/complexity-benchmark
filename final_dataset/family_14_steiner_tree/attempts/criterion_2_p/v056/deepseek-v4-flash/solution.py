import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    terminals = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # If only one terminal, cost is 0
    if t == 1:
        print(0)
        return
    
    # DFS to count terminals in subtree
    parent = [0] * (n + 1)
    parent_edge_cost = [0] * (n + 1)
    order = []
    stack = [next(iter(terminals))]
    parent[next(iter(terminals))] = -1
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_edge_cost[v] = w
                stack.append(v)
    
    term_count = [0] * (n + 1)
    for term in terminals:
        term_count[term] = 1
    
    total_cost = 0
    for u in reversed(order):
        if u != next(iter(terminals)):
            if term_count[u] > 0:
                total_cost += parent_edge_cost[u]
            term_count[parent[u]] += term_count[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()