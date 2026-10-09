import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); m = int(data[idx+1]); idx += 3  # skip the "1"
    S = int(data[idx]); T = int(data[idx+1]); D = int(data[idx+2]); idx += 3
    
    edges = []
    adj = [[] for _ in range(n+1)]
    for j in range(m):
        u = int(data[idx]); v = int(data[idx+1]); C = int(data[idx+2]); idx += 3
        edges.append((u, v, C))
        adj[u].append((v, j, False))
        adj[v].append((u, j, True))
    
    # BFS to find augmenting path
    def bfs():
        parent = [-1] * (n+1)
        parent_edge = [None] * (n+1)
        parent_dir = [None] * (n+1)
        visited = [False] * (n+1)
        q = deque()
        q.append(S)
        visited[S] = True
        while q:
            u = q.popleft()
            if u == T:
                break
            for v, j, is_rev in adj[u]:
                if is_rev:
                    cap = flow[j]
                else:
                    cap = edges[j][2] - flow[j]
                if cap > 0 and not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    parent_edge[v] = j
                    parent_dir[v] = is_rev
                    q.append(v)
        if not visited[T]:
            return 0, parent, parent_edge, parent_dir
        # Find bottleneck
        path = []
        v = T
        bottleneck = float('inf')
        while v != S:
            j = parent_edge[v]
            is_rev = parent_dir[v]
            if is_rev:
                cap = flow[j]
            else:
                cap = edges[j][2] - flow[j]
            bottleneck = min(bottleneck, cap)
            path.append((j, is_rev))
            v = parent[v]
        for j, is_rev in path:
            if is_rev:
                flow[j] -= bottleneck
            else:
                flow[j] += bottleneck
        return bottleneck, parent, parent_edge, parent_dir
    
    flow = [0] * m
    total = 0
    while True:
        f, _, _, _ = bfs()
        if f == 0:
            break
        total += f
        if total >= D:
            break
    
    if total >= D:
        # Scale down to exactly D
        if total > D:
            excess = total - D
            # Remove excess by finding path from T to S in residual
            while excess > 0:
                parent = [-1] * (n+1)
                parent_edge = [None] * (n+1)
                parent_dir = [None] * (n+1)
                visited = [False] * (n+1)
                q = deque()
                q.append(T)
                visited[T] = True
                found = False
                while q:
                    u = q.popleft()
                    if u == S:
                        found = True
                        break
                    for v, j, is_rev in adj[u]:
                        if is_rev:
                            cap = edges[j][2] - flow[j]
                        else:
                            cap = flow[j]
                        if cap > 0 and not visited[v]:
                            visited[v] = True
                            parent[v] = u
                            parent_edge[v] = j
                            parent_dir[v] = is_rev
                            q.append(v)
                if not found:
                    break
                path = []
                v = S
                bottleneck = float('inf')
                while v != T:
                    j = parent_edge[v]
                    is_rev = parent_dir[v]
                    if is_rev:
                        cap = edges[j][2] - flow[j]
                    else:
                        cap = flow[j]
                    bottleneck = min(bottleneck, cap)
                    path.append((j, is_rev))
                    v = parent[v]
                bottleneck = min(bottleneck, excess)
                for j, is_rev in path:
                    if is_rev:
                        flow[j] += bottleneck
                    else:
                        flow[j] -= bottleneck
                excess -= bottleneck
        
        # Verify
        net = [0] * (n+1)
        for j in range(m):
            u, v, C = edges[j]
            net[u] -= flow[j]
            net[v] += flow[j]
        if net[S] == -D and net[T] == D and all(net[i] == 0 for i in range(1, n+1) if i != S and i != T):
            print("YES")
            print(" ".join(str(x) for x in flow))
        else:
            print("NO")
    else:
        print("NO")

solve()