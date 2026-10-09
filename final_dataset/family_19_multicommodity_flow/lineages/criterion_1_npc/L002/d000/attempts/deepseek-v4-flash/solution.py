import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    requests = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        requests.append((s, t, d))
    
    edges = []
    cap = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v))
        cap.append(c)
    
    # residual capacities
    residual = cap[:]
    
    # flow per request per edge
    flow_assign = [[0]*m for _ in range(k)]
    
    # For each request, run max flow on the graph with current residual capacities
    for idx, (s, t, d) in enumerate(requests):
        # Build adjacency for this request
        adj = [[] for _ in range(n)]
        for eid, (u, v) in enumerate(edges):
            if residual[eid] > 0:
                adj[u].append((v, eid))
        
        # BFS/DFS to find a path and push flow
        # We'll use Edmonds-Karp style but only need to send d units
        total_sent = 0
        while total_sent < d:
            # BFS to find augmenting path
            parent = [-1]*n
            parent_edge = [-1]*n
            q = deque([s])
            parent[s] = s
            found = False
            while q and not found:
                u = q.popleft()
                for v, eid in adj[u]:
                    if parent[v] == -1 and residual[eid] > 0:
                        parent[v] = u
                        parent_edge[v] = eid
                        if v == t:
                            found = True
                            break
                        q.append(v)
            if not found:
                break
            # find bottleneck
            v = t
            bottleneck = float('inf')
            while v != s:
                eid = parent_edge[v]
                bottleneck = min(bottleneck, residual[eid])
                v = parent[v]
            # push flow
            v = t
            while v != s:
                eid = parent_edge[v]
                residual[eid] -= bottleneck
                flow_assign[idx][eid] += bottleneck
                v = parent[v]
            total_sent += bottleneck
        
        if total_sent < d:
            print("NO")
            return
    
    print("YES")
    for i in range(k):
        print(' '.join(str(flow_assign[i][j]) for j in range(m)))

if __name__ == "__main__":
    solve()