import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        t = int(next(iterator))
    except StopIteration:
        return

    is_organic = [False] * (n + 1)
    for _ in range(t):
        node = int(next(iterator))
        is_organic[node] = True

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        adj[u].append((v, w))
        adj[v].append((u, w))

    parent = [0] * (n + 1)
    p_edge = [0] * (n + 1)
    depth = [0] * (n + 1)
    
    # BFS to build rooted tree structure
    q = deque()
    root = 1
    q.append(root)
    parent[root] = 0
    depth[root] = 0
    
    while q:
        u = q.popleft()
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                p_edge[v] = w
                depth[v] = depth[u] + 1
                q.append(v)

    # If only one organic chamber, no edges needed
    if t <= 1:
        print(0)
        return

    # Sort organic chambers by DFS order (using depth-first numbering)
    # We perform a DFS to get entry times
    entry_time = [0] * (n + 1)
    exit_time = [0] * (n + 1)
    timer = 0
    
    stack = [(root, 0, False)] # (node, edge_weight, visited_flag)
    
    while stack:
        u, w, visited = stack.pop()
        if not visited:
            timer += 1
            entry_time[u] = timer
            stack.append((u, w, True))
            # Push children in reverse order to process them in order
            for v, w_val in adj[u]:
                if v != parent[u]:
                    stack.append((v, w_val, False))
        else:
            exit_time[u] = timer

    organic_nodes = [i for i in range(1, n + 1) if is_organic[i]]
    # Sort by entry time
    organic_nodes.sort(key=lambda x: entry_time[x])

    total_labor = 0
    
    # Function to calculate distance between two nodes
    def get_dist(u, v):
        dist = 0
        # Bring u and v to same depth
        while depth[u] > depth[v]:
            dist += p_edge[u]
            u = parent[u]
        while depth[v] > depth[u]:
            dist += p_edge[v]
            v = parent[v]
        # Find LCA
        while u != v:
            dist += p_edge[u] + p_edge[v]
            u = parent[u]
            v = parent[v]
        return dist

    # Sum distances between consecutive organic nodes in circular order
    for i in range(t):
        u = organic_nodes[i]
        v = organic_nodes[(i + 1) % t]
        total_labor += get_dist(u, v)

    print(total_labor // 2)

if __name__ == '__main__':
    solve()