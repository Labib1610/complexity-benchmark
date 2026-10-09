import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    adj = [[] for _ in range(2 * q + 1)]
    for i in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append((b, i))
        adj[b].append((a, i))
    
    visited = [False] * (2 * q + 1)
    edge_used = [False] * t
    parent = [0] * (2 * q + 1)
    parent_edge = [-1] * (2 * q + 1)
    stack = []
    
    for s in range(1, 2 * q + 1):
        if not visited[s]:
            visited[s] = True
            parent[s] = 0
            parent_edge[s] = -1
            stack.append(s)
            while stack:
                u = stack.pop()
                for v, e in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        parent[v] = u
                        parent_edge[v] = e
                        edge_used[e] = True
                        stack.append(v)
                    elif v != parent[u] and not edge_used[e]:
                        edge_used[e] = True
                        cur = u
                        while cur != v and cur != 0:
                            pe = parent_edge[cur]
                            if pe == -1:
                                break
                            if edge_used[pe]:
                                edge_used[pe] = False
                            else:
                                edge_used[pe] = True
                            cur = parent[cur]
    
    deg = [0] * (2 * q + 1)
    for e in range(t):
        if edge_used[e]:
            deg[adj[e][0][0]] += 1
    
    for u in range(1, 2 * q + 1):
        if deg[u] == 0:
            stack = [u]
            while stack:
                cur = stack.pop()
                improved = False
                for v, e in adj[cur]:
                    if edge_used[e]:
                        nxt = v
                    else:
                        nxt = cur
                    if deg[nxt] > 1:
                        if edge_used[e]:
                            edge_used[e] = False
                            deg[cur] -= 1
                            deg[nxt] -= 1
                        else:
                            edge_used[e] = True
                            deg[cur] += 1
                            deg[nxt] += 1
                        improved = True
                        break
                if not improved:
                    for v, e in adj[cur]:
                        if not edge_used[e] and deg[v] > 0:
                            edge_used[e] = True
                            deg[cur] += 1
                            deg[v] += 1
                            improved = True
                            break
                if improved and deg[cur] == 0:
                    stack.append(cur)
    
    for u in range(1, 2 * q + 1):
        if deg[u] != 1:
            print("NO")
            return
    
    out = ["YES"]
    for e in range(t):
        if edge_used[e]:
            a, b = adj[e][0][0], adj[e][0][1]
            out.append(f"{a} {b}")
    sys.stdout.write("\n".join(out))

solve()