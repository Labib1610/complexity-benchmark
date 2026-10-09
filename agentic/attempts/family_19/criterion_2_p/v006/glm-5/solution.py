import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))
        adj[u].append(v)
        adj[v].append(u)
    
    # Build level graph for Dinic's algorithm
    def bfs(level, ptr):
        level[:] = [-1] * (n + 1)
        q = deque([s])
        level[s] = 0
        while q:
            u = q.popleft()
            for eid in adj[u]:
                v = (edges[eid][1] if edges[eid][0] == u else edges[eid][0]) if eid < m else edges[eid - m][0]
                # Check forward edge or backward edge
                if eid < m:
                    # Forward edge from u to v
                    if edges[eid][0] == u:
                        # Forward residual
                        if cap_list[eid] - flow[eid] > 0 and level[edges[eid][1]] < 0:
                            level[edges[eid][1]] = level[u] + 1
                            q.append(edges[eid][1])
                    # Backward edge (from v to u)
                    else:
                        if flow[eid] > 0 and level[edges[eid][0]] < 0:
                            level[edges[eid][0]] = level[u] + 1
                            q.append(edges[eid][0])
                else:
                    # Reverse edge
                    actual_eid = eid - m
                    if edges[actual_eid][1] == u:
                        # This is forward edge in residual (using reverse edge)
                        if flow[actual_eid] > 0 and level[edges[actual_eid][0]] < 0:
                            level[edges[actual_eid][0]] = level[u] + 1
                            q.append(edges[actual_eid][0])
                    else:
                        # This is backward edge in residual (using forward edge)
                        if cap_list[actual_eid] - flow[actual_eid] > 0 and level[edges[actual_eid][1]] < 0:
                            level[edges[actual_eid][1]] = level[u] + 1
                            q.append(edges[actual_eid][1])
        return level[t] >= 0
    
    def dfs(u, pushed, level, ptr):
        if pushed == 0 or u == t:
            return pushed
        for i in range(ptr[u], len(adj[u])):
            ptr[u] = i
            eid = adj[u][i]
            if eid < m:
                v = edges[eid][1] if edges[eid][0] == u else edges[eid][0]
                # Forward edge
                if edges[eid][0] == u:
                    if level[v] == level[u] + 1 and cap_list[eid] - flow[eid] > 0:
                        tr = dfs(v, min(pushed, cap_list[eid] - flow[eid]), level, ptr)
                        if tr:
                            flow[eid] += tr
                            return tr
                else:
                    if level[v] == level[u] + 1 and flow[eid] > 0:
                        tr = dfs(v, min(pushed, flow[eid]), level, ptr)
                        if tr:
                            flow[eid] -= tr
                            return tr
            else:
                actual_eid = eid - m
                if edges[actual_eid][1] == u:
                    # Forward using reverse edge
                    if level[edges[actual_eid][0]] == level[u] + 1 and flow[actual_eid] > 0:
                        tr = dfs(edges[actual_eid][0], min(pushed, flow[actual_eid]), level, ptr)
                        if tr:
                            flow[actual_eid] -= tr
                            return tr
                else:
                    if level[edges[actual_eid][1]] == level[u] + 1 and cap_list[actual_eid] - flow[actual_eid] > 0:
                        tr = dfs(edges[actual_eid][1], min(pushed, cap_list[actual_eid] - flow[actual_eid]), level, ptr)
                        if tr:
                            flow[actual_eid] += tr
                            return tr
        return 0
    
    cap_list = [e[2] for e in edges]
    flow = [0] * m
    level = [-1] * (n + 1)
    ptr = [0] * (n + 1)
    
    total_flow = 0
    while bfs(level, ptr):
        ptr[:] = [0] * (n + 1)
        while True:
            f = dfs(s, d - total_flow, level, ptr)
            if f == 0:
                break
            total_flow += f
            if total_flow >= d:
                break
        if total_flow >= d:
            break
    
    if total_flow >= d:
        print("YES")
        print(" ".join(map(str, flow)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()