import sys
from sys import stdin
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    critical = set()
    for i in range(t):
        critical.add(int(input_data[idx])); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # BFS to compute parent, depth, and min edge to parent
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    depth = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    from collections import deque
    queue = deque([1])
    visited[1] = True
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                parent_weight[v] = w
                depth[v] = depth[u] + 1
                queue.append(v)
    
    # Find LCA of all critical nodes
    crit_list = list(critical)
    lca = crit_list[0]
    for node in crit_list[1:]:
        a, b = lca, node
        while depth[a] > depth[b]:
            a = parent[a]
        while depth[b] > depth[a]:
            b = parent[b]
        while a != b:
            a = parent[a]
            b = parent[b]
        lca = a
    
    # For each critical node, walk up to lca, summing min edge weights
    # Use visited set to avoid double counting
    in_tree = set()
    in_tree.add(lca)
    
    total_cost = 0
    for node in crit_list:
        curr = node
        while curr != lca and curr not in in_tree:
            in_tree.add(curr)
            total_cost += parent_weight[curr]
            curr = parent[curr]
    
    print(total_cost)

solve()