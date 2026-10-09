import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        indeg[b] += 1
    
    # Binary search for the latest possible cycle for each node
    # Using Kahn's algorithm with priority queue (max-heap)
    import heapq
    
    latest = [T] * n
    indeg_copy = indeg[:]
    heap = []
    for i in range(n):
        if indeg_copy[i] == 0:
            heapq.heappush(heap, (-T, i))
    
    while heap:
        neg_cycle, u = heapq.heappop(heap)
        cycle_u = -neg_cycle
        latest[u] = cycle_u
        for v in adj[u]:
            indeg_copy[v] -= 1
            if indeg_copy[v] == 0:
                heapq.heappush(heap, (-(cycle_u - 1), v))
    
    # Check for cycle
    if any(indeg_copy[i] != 0 for i in range(n)):
        print("NO")
        return
    
    # Now assign cycles greedily from earliest to latest
    # Sort nodes by their latest deadline
    nodes = list(range(n))
    nodes.sort(key=lambda x: latest[x])
    
    cycle_count = [0] * (T + 2)
    assigned = [0] * n
    
    possible = True
    for u in nodes:
        # Find earliest cycle >= 1 such that count < M and cycle <= latest[u]
        # Start from cycle 1
        # We need to find the earliest available cycle
        # Since we process in order of latest, greedy works
        # We can use a pointer to track the earliest cycle with capacity
        # But for simplicity, iterate from 1 to latest[u]
        found = False
        for c in range(1, latest[u] + 1):
            if cycle_count[c] < M:
                assigned[u] = c
                cycle_count[c] += 1
                found = True
                break
        if not found:
            possible = False
            break
    
    if possible:
        print("YES")
        print(' '.join(map(str, assigned)))
    else:
        print("NO")

solve()