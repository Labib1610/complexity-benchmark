import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = defaultdict(list)
    degree = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # Find node with maximum degree
    max_deg = 0
    center = 1
    for i in range(1, n + 1):
        if degree[i] > max_deg:
            max_deg = degree[i]
            center = i
    
    # Place center at position 1, neighbors at positions 2, 3, ..., others at remaining
    pos = [0] * (n + 1)
    slot = 1
    pos[center] = slot
    slot += 1
    
    neighbors = []
    others = []
    for i in range(1, n + 1):
        if i == center:
            continue
        if i in adj[center]:
            neighbors.append(i)
        else:
            others.append(i)
    
    # Place neighbors first (closest to center)
    for node in neighbors:
        pos[node] = slot
        slot += 1
    
    # Place others
    for node in others:
        pos[node] = slot
        slot += 1
    
    # Calculate total wire consumption
    total = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, pos[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()