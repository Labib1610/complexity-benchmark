from collections import defaultdict, deque
import sys

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    k = int(data[idx])
    idx += 1
    
    orders = []
    for _ in range(k):
        s = int(data[idx]) - 1
        idx += 1
        t = int(data[idx]) - 1
        idx += 1
        d = int(data[idx])
        idx += 1
        orders.append((s, t, d))
    
    belts = []
    belt_graph = defaultdict(list)
    for i in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        cap = int(data[idx])
        idx += 1
        belts.append((u, v, cap))
        belt_graph[u].append((v, i))
    
    # For each order, compute the flow on each edge using BFS (since it's a unit flow)
    flows = []
    for s, t, d in orders:
        # We need to send 'd' units of flow from s to t
        # We'll compute a path decomposition
        total_flow = [0] * m
        for _ in range(d):
            # BFS to find a path from s to t
            parent = [-1] * n
            parent_edge = [-1] * n
            queue = deque()
            queue.append(s)
            parent[s] = s
            found = False
            while queue:
                u = queue.popleft()
                if u == t:
                    found = True
                    break
                for v, edge_idx in belt_graph[u]:
                    if parent[v] == -1:
                        parent[v] = u
                        parent_edge[v] = edge_idx
                        queue.append(v)
            if not found:
                print("NO")
                return
            # Augment along the path
            cur = t
            while cur != s:
                prev = parent[cur]
                edge_idx = parent_edge[cur]
                total_flow[edge_idx] += 1
                cur = prev
        flows.append(total_flow)
    
    # Check if the total flow on each edge is within capacity
    total_usage = [0] * m
    for flow in flows:
        for i in range(m):
            total_usage[i] += flow[i]
    
    for i in range(m):
        if total_usage[i] > belts[i][2]:
            print("NO")
            return
    
    print("YES")
    for flow in flows:
        print(' '.join(map(str, flow)))

solve()