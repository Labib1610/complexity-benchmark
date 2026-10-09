import sys
from collections import defaultdict, deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    edges = []
    adj = defaultdict(list)
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Check 3-regular
    for v in range(1, n+1):
        if len(adj[v]) != 3:
            print("NO")
            return
    
    if n == 2:
        print("YES")
        print("1 2 3")
        return
    
    if n == 4:
        # K4 case: not 3-edge-colorable
        print("NO")
        return
    
    # Find perfect matching using alternating paths
    matched = [False] * m
    vertex_match = [None] * (n + 1)
    
    def augment(start):
        visited = [False] * (n + 1)
        parent = [None] * (n + 1)
        parent_edge = [None] * (n + 1)
        visited[start] = True
        queue = deque([start])
        found = None
        while queue:
            u = queue.popleft()
            if vertex_match[u] is None and u != start:
                found = u
                break
            for v, eid in adj[u]:
                if visited[v]:
                    continue
                visited[v] = True
                parent[v] = u
                parent_edge[v] = eid
                queue.append(v)
        if found is None:
            return False
        v = found
        while parent[v] is not None:
            eid = parent_edge[v]
            matched[eid] = not matched[eid]
            v = parent[v]
        for eid in range(m):
            if matched[eid]:
                u, v = edges[eid]
                vertex_match[u] = eid
                vertex_match[v] = eid
            else:
                u, v = edges[eid]
                if vertex_match[u] == eid:
                    vertex_match[u] = None
                if vertex_match[v] == eid:
                    vertex_match[v] = None
        return True
    
    for v in range(1, n + 1):
        if vertex_match[v] is None:
            if not augment(v):
                print("NO")
                return
    
    # Build residual graph (edges not in matching)
    res_adj = defaultdict(list)
    for i in range(m):
        if not matched[i]:
            u, v = edges[i]
            res_adj[u].append((v, i))
            res_adj[v].append((u, i))
    
    # Find Eulerian circuit using Hierholzer
    circuit = []
    used = [False] * m
    stack = [1]
    local_adj = {v: list(res_adj[v]) for v in range(1, n+1)}
    ptr = {v: 0 for v in range(1, n+1)}
    
    while stack:
        u = stack[-1]
        while ptr[u] < len(local_adj[u]):
            v, eid = local_adj[u][ptr[u]]
            ptr[u] += 1
            if not used[eid]:
                used[eid] = True
                stack.append(v)
                u = v
        if stack:
            circuit.append(stack.pop())
    
    # Assign colors
    ans = [0] * m
    for i in range(m):
        if matched[i]:
            ans[i] = 3
    
    for i in range(len(circuit) - 1):
        u = circuit[i]
        v = circuit[i + 1]
        for w, eid in res_adj[u]:
            if w == v and not matched[eid] and ans[eid] == 0:
                ans[eid] = 1 if i % 2 == 0 else 2
                break
    
    print("YES")
    print(' '.join(map(str, ans)))

solve()