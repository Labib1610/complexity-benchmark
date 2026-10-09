import sys
import random

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Initial order: BFS from node 0
    order = []
    visited = [False]*n
    from collections import deque
    q = deque([0])
    visited[0] = True
    while q:
        u = q.popleft()
        order.append(u)
        for w in adj[u]:
            if not visited[w]:
                visited[w] = True
                q.append(w)
    # Add any isolated nodes
    for i in range(n):
        if not visited[i]:
            order.append(i)
    
    pos = [0]*n
    for idx, node in enumerate(order):
        pos[node] = idx
    
    def cost():
        total = 0
        for u,v in edges:
            total += abs(pos[u] - pos[v])
        return total
    
    cur_cost = cost()
    
    # Local search: try swaps
    # We'll do multiple random restarts if needed
    best_order = order[:]
    best_cost = cur_cost
    
    for restart in range(20):
        # Shuffle a bit for restart
        if restart > 0:
            random.shuffle(order)
            for idx, node in enumerate(order):
                pos[node] = idx
            cur_cost = cost()
        
        improved = True
        while improved:
            improved = False
            for i in range(n):
                for j in range(i+1, n):
                    # Try swap i and j
                    u = order[i]
                    v = order[j]
                    # Compute delta
                    delta = 0
                    for a,b in edges:
                        if a == u or b == u:
                            other = b if a == u else a
                            old = abs(pos[u] - pos[other])
                            new = abs(pos[v] - pos[other])
                            delta += new - old
                        if a == v or b == v:
                            other = b if a == v else a
                            old = abs(pos[v] - pos[other])
                            new = abs(pos[u] - pos[other])
                            delta += new - old
                    if delta < 0:
                        # swap
                        order[i], order[j] = order[j], order[i]
                        pos[u], pos[v] = pos[v], pos[u]
                        cur_cost += delta
                        improved = True
                        if cur_cost <= B:
                            print("YES")
                            print(' '.join(str(p+1) for p in order))
                            return
        if cur_cost < best_cost:
            best_cost = cur_cost
            best_order = order[:]
        if best_cost <= B:
            break
    
    if best_cost <= B:
        print("YES")
        print(' '.join(str(p+1) for p in best_order))
    else:
        print("NO")

if __name__ == "__main__":
    solve()