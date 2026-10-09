import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Check degree condition
    for u in range(1, n + 1):
        if len(adj[u]) != 3:
            print("NO")
            return
    
    # Find a cycle
    start = 1
    parent = [-1] * (n + 1)
    parent_edge = [-1] * (n + 1)
    stack = [start]
    parent[start] = 0
    cycle_nodes = []
    found = False
    
    while stack and not found:
        u = stack.pop()
        for v, eid in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                parent_edge[v] = eid
                stack.append(v)
            elif v != parent[u]:
                # Found cycle
                cycle_nodes.append(v)
                cur = u
                while cur != v:
                    cycle_nodes.append(cur)
                    cur = parent[cur]
                cycle_nodes.append(v)
                found = True
                break
    
    # Assign colors to cycle edges
    color = [0] * m
    cycle_edges = set()
    for i in range(len(cycle_nodes) - 1):
        u = cycle_nodes[i]
        v = cycle_nodes[i + 1]
        for w, eid in adj[u]:
            if w == v:
                color[eid] = 1 if i % 2 == 0 else 2
                cycle_edges.add(eid)
                break
    
    # BFS from cycle nodes
    from collections import deque
    queue = deque()
    in_queue = [False] * (n + 1)
    for node in cycle_nodes:
        if not in_queue[node]:
            queue.append(node)
            in_queue[node] = True
    
    while queue:
        u = queue.popleft()
        # Find used colors at u
        used = set()
        for v, eid in adj[u]:
            if color[eid] != 0:
                used.add(color[eid])
        avail = {1, 2, 3} - used
        
        for v, eid in adj[u]:
            if color[eid] == 0:
                if avail:
                    c = avail.pop()
                    color[eid] = c
                    if not in_queue[v]:
                        queue.append(v)
                        in_queue[v] = True
                else:
                    print("NO")
                    return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()