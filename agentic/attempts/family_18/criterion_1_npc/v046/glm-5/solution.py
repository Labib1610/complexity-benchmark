import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    B = int(input_data[idx]); idx += 1
    
    adj = defaultdict(set)
    deg = [0] * (n + 1)
    edges = []
    for _ in range(m):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        adj[x].add(y)
        adj[y].add(x)
        deg[x] += 1
        deg[y] += 1
        edges.append((x, y))
    
    if n == 0:
        print("YES")
        print()
        return
    
    best_pos = None
    best_cost = float('inf')
    
    for direction in [1, -1]:
        start_v = max(range(1, n + 1), key=lambda v: deg[v])
        pos = [0] * (n + 1)
        placed = [False] * (n + 1)
        
        pos[start_v] = 1
        placed[start_v] = True
        order = [start_v]
        total_cost = 0
        
        for p in range(2, n + 1):
            best_v = -1
            best_inc = float('inf')
            for v in range(1, n + 1):
                if placed[v]:
                    continue
                inc = 0
                for u in adj[v]:
                    if placed[u]:
                        inc += abs(p - pos[u])
                if inc < best_inc or (inc == best_inc and v < best_v):
                    best_inc = inc
                    best_v = v
            
            pos[best_v] = p
            placed[best_v] = True
            order.append(best_v)
            total_cost += best_inc
        
        if total_cost < best_cost:
            best_cost = total_cost
            best_pos = pos[:]
    
    if best_cost <= B:
        print("YES")
        print(' '.join(str(best_pos[v]) for v in range(1, n + 1)))
    else:
        print("NO")

solve()