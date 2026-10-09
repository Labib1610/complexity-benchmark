import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # Find the minimal subtree connecting all critical nodes
    # We'll do DFS from any critical node, and mark nodes that are in the subtree
    # A node is in the subtree if it is critical or has a child in the subtree.
    
    parent = [-1] * n
    parent_w = [0] * n
    order = []
    stack = [next(iter(critical))]
    parent[next(iter(critical))] = -2  # root marker
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                parent_w[v] = w
                stack.append(v)
    
    in_subtree = [False] * n
    for c in critical:
        in_subtree[c] = True
    
    # Process in reverse order to propagate "needed" status
    for u in reversed(order):
        if in_subtree[u]:
            p = parent[u]
            if p >= 0:
                in_subtree[p] = True
    
    total_cost = 0
    for u in range(n):
        if u != next(iter(critical)) and in_subtree[u] and parent[u] >= 0:
            total_cost += parent_w[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()