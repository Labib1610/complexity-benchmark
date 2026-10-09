import sys
from collections import deque
import random

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    B = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    if m == 0:
        print("YES")
        print(" ".join(str(i) for i in range(1, n+1)))
        return
    
    best_pos = None
    best_cost = float('inf')
    
    for trial in range(200):
        if trial == 0:
            start = max(range(1, n+1), key=lambda x: len(adj[x]))
        else:
            start = random.randint(1, n)
        
        order = []
        visited = [False] * (n+1)
        dq = deque([start])
        visited[start] = True
        while dq:
            u = dq.popleft()
            order.append(u)
            neighbors = sorted(adj[u], key=lambda x: len(adj[x]), reverse=True)
            for v in neighbors:
                if not visited[v]:
                    visited[v] = True
                    dq.append(v)
        
        for unvisited in range(1, n+1):
            if not visited[unvisited]:
                order.append(unvisited)
        
        pos = [0] * (n+1)
        for i, u in enumerate(order):
            pos[u] = i + 1
        
        cost = 0
        for u in range(1, n+1):
            for v in adj[u]:
                if v > u:
                    cost += abs(pos[u] - pos[v])
        
        if cost <= B:
            print("YES")
            print(" ".join(str(pos[i]) for i in range(1, n+1)))
            return
        
        if cost < best_cost:
            best_cost = cost
            best_pos = pos[:]
    
    # Try local search
    pos = best_pos[:]
    for _ in range(100000):
        i, j = random.randint(1, n), random.randint(1, n)
        if i == j:
            continue
        pos[i], pos[j] = pos[j], pos[i]
        cost = 0
        for u in range(1, n+1):
            for v in adj[u]:
                if v > u:
                    cost += abs(pos[u] - pos[v])
        if cost <= B:
            print("YES")
            print(" ".join(str(pos[i]) for i in range(1, n+1)))
            return
        if cost >= best_cost:
            pos[i], pos[j] = pos[j], pos[i]
        else:
            best_cost = cost
    
    print("NO")

solve()