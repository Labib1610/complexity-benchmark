import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    essential = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to count essential sites in each subtree
    visited = [False] * (n + 1)
    essential_count = [0] * (n + 1)
    
    # Start from any essential site
    start = next(iter(essential))
    
    stack = [(start, -1)]
    order = []
    parent = [0] * (n + 1)
    parent_edge_cost = [0] * (n + 1)
    
    while stack:
        node, par = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        parent[node] = par
        order.append(node)
        for nei, w in adj[node]:
            if nei != par and not visited[nei]:
                parent_edge_cost[nei] = w
                stack.append((nei, node))
    
    # Process in reverse order to accumulate counts
    for node in reversed(order):
        if node in essential:
            essential_count[node] += 1
        if parent[node] != -1:
            essential_count[parent[node]] += essential_count[node]
    
    total_cost = 0
    for node in range(1, n + 1):
        if node == start:
            continue
        # Edge between node and parent[node] is needed if both sides have essential sites
        if essential_count[node] > 0 and (t - essential_count[node]) > 0:
            total_cost += parent_edge_cost[node]
    
    print(total_cost)

if __name__ == "__main__":
    solve()