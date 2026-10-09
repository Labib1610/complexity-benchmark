import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0]); m = int(data[1]); B = int(data[2])
    edges = []
    idx = 3
    deg = [0]*(n+1)
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        edges.append((u,v))
        adj[u].append(v)
        adj[v].append(u)
        deg[u]+=1
        deg[v]+=1

    # Special case: no edges, any permutation works.
    if m == 0:
        print("YES")
        print(' '.join(str(i) for i in range(1, n+1)))
        return

    # Find a vertex of minimum degree.
    min_deg = n+1
    s = 1
    for i in range(1, n+1):
        if deg[i] < min_deg:
            min_deg = deg[i]
            s = i

    # If min degree is 0, graph disconnected -> impossible (m>0).
    if min_deg == 0:
        print("NO")
        return

    # If min degree is 1, graph is a tree (connected) -> always possible.
    if min_deg == 1:
        # BFS from the degree-1 vertex.
        order = [s]
        visited = [False]*(n+1)
        visited[s] = True
        q = [s]
        head = 0
        while head < len(q):
            u = q[head]; head += 1
            for w in adj[u]:
                if not visited[w]:
                    visited[w] = True
                    q.append(w)
                    order.append(w)
        pos = [0]*(n+1)
        for i, v in enumerate(order):
            pos[v] = i+1
        total = 0
        for u,v in edges:
            total += abs(pos[u]-pos[v])
        if total <= B:
            print("YES")
            print(' '.join(str(pos[i]) for i in range(1, n+1)))
        else:
            print("NO")
        return

    # General case: min degree >= 2.
    # Try BFS order from min-degree vertex; if it fits budget, output.
    order = [s]
    visited = [False]*(n+1)
    visited[s] = True
    q = [s]
    head = 0
    while head < len(q):
        u = q[head]; head += 1
        for w in adj[u]:
            if not visited[w]:
                visited[w] = True
                q.append(w)
                order.append(w)
    pos = [0]*(n+1)
    for i, v in enumerate(order):
        pos[v] = i+1
    total = 0
    for u,v in edges:
        total += abs(pos[u]-pos[v])
    if total <= B:
        print("YES")
        print(' '.join(str(pos[i]) for i in range(1, n+1)))
        return

    # Otherwise, try placing neighbors of s contiguously at the front.
    nbrs = adj[s]
    k = len(nbrs)
    rest = [v for v in range(1, n+1) if v != s and v not in set(nbrs)]
    order2 = nbrs + [s] + rest
    pos2 = [0]*(n+1)
    for i, v in enumerate(order2):
        pos2[v] = i+1
    total2 = 0
    for u,v in edges:
        total2 += abs(pos2[u]-pos2[v])
    if total2 <= B:
        print("YES")
        print(' '.join(str(pos2[i]) for i in range(1, n+1)))
        return

    print("NO")

solve()