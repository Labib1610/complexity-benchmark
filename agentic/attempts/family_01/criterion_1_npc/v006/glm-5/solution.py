import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Check if graph is bipartite
    color = [-1] * n
    is_bipartite = True
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            stack = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break
    
    if is_bipartite:
        print("YES")
        result = [str(c + 1) for c in color]
        # Fill remaining with 3 (though all should be colored)
        for i in range(n):
            if color[i] == -1:
                result[i] = '3'
        print(' '.join(result))
        return
    
    # Graph is not bipartite, need to find odd cycle
    parent = [-1] * n
    depth = [-1] * n
    cycle = []
    
    for start in range(n):
        if depth[start] != -1:
            continue
        stack = [(start, 0)]
        depth[start] = 0
        found = False
        while stack and not found:
            u, idx = stack[-1]
            if idx < len(adj[u]):
                v = adj[u][idx]
                stack[-1] = (u, idx + 1)
                if depth[v] == -1:
                    depth[v] = depth[u] + 1
                    parent[v] = u
                    stack.append((v, 0))
                elif v != parent[u]:
                    # Found cycle
                    # Reconstruct cycle
                    cycle = []
                    a, b = u, v
                    while a != b and a != -1 and b != -1:
                        if depth[a] > depth[b]:
                            cycle.append(a)
                            a = parent[a]
                        elif depth[b] > depth[a]:
                            cycle.append(b)
                            b = parent[b]
                        else:
                            cycle.append(a)
                            cycle.append(b)
                            a = parent[a]
                            b = parent[b]
                    if a != -1:
                        cycle.append(a)
                    found = True
                    break
            else:
                stack.pop()
        if found:
            break
    
    if not cycle:
        print("YES")
        print(' '.join(['1'] * n))
        return
    
    # Remove duplicates from cycle
    seen = set()
    unique_cycle = []
    for node in cycle:
        if node not in seen:
            seen.add(node)
            unique_cycle.append(node)
    cycle = unique_cycle
    
    # Build adjacency set
    adj_set = [set() for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            adj_set[u].add(v)
    
    # Check if cycle is chordless
    is_chordless = True
    L = len(cycle)
    for i in range(L):
        for j in range(i + 2, L):
            if j == i + L - 1:
                continue
            if cycle[j] in adj_set[cycle[i]]:
                is_chordless = False
                break
        if not is_chordless:
            break
    
    if not is_chordless:
        # Find chordless odd cycle
        # Use BFS from each node
        for start in range(n):
            if found:
                break
            p = [-1] * n
            d = [-1] * n
            d[start] = 0
            q = [start]
            head = 0
            while head < len(q) and not found:
                u = q[head]
                head += 1
                for v in adj[u]:
                    if d[v] == -1:
                        d[v] = d[u] + 1
                        p[v] = u
                        q.append(v)
                    elif v != p[u]:
                        # Found cycle
                        cyc = []
                        a, b = u, v
                        while a != b:
                            if d[a] > d[b]:
                                cyc.append(a)
                                a = p[a]
                            elif d[b] > d[a]:
                                cyc.append(b)
                                b = p[b]
                            else:
                                cyc.append(a)
                                cyc.append(b)
                                a = p[a]
                                b = p[b]
                        cyc.append(a)
                        # Check if odd
                        if len(cyc) % 2 == 1:
                            # Check if chordless
                            seen_c = set()
                            unique_c = []
                            for node in cyc:
                                if node not in seen_c:
                                    seen_c.add(node)
                                    unique_c.append(node)
                            cyc = unique_c
                            Lc = len(cyc)
                            chordless = True
                            for ii in range(Lc):
                                for jj in range(ii + 2, Lc):
                                    if jj == ii + Lc - 1:
                                        continue
                                    if cyc[jj] in adj_set[cyc[ii]]:
                                        chordless = False
                                        break
                                if not chordless:
                                    break
                            if chordless:
                                cycle = cyc
                                found = True
                                break
    
    # Assign cycle nodes to shifts 1 and 2 alternating
    assignment = [0] * n
    L = len(cycle)
    for i, node in enumerate(cycle):
        assignment[node] = 1 if i % 2 == 0 else 2
    
    # BFS to assign remaining nodes
    queue = list(cycle)
    in_queue = [False] * n
    for node in cycle:
        in_queue[node] = True
    
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        for v in adj[u]:
            if assignment[v] == 0:
                # Find available shift
                forbidden = set()
                for w in adj[v]:
                    if assignment[w] != 0:
                        forbidden.add(assignment[w])
                for s in [1, 2, 3]:
                    if s not in forbidden:
                        assignment[v] = s
                        break
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
    
    # Assign any remaining unassigned nodes
    for i in range(n):
        if assignment[i] == 0:
            assignment[i] = 1
    
    # Verify assignment
    for u in range(n):
        for v in adj[u]:
            if assignment[u] == assignment[v]:
                print("NO")
                return
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()