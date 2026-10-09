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
    
    # Topological sort to get a valid order
    q = deque([i for i in range(n) if indeg[i] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(topo) != n:
        print("NO")
        return
    
    # Compute earliest possible day for each injection
    earliest = [1] * n
    for u in topo:
        for v in adj[u]:
            if earliest[v] < earliest[u] + 1:
                earliest[v] = earliest[u] + 1
    
    # Check if any earliest day exceeds T
    for d in earliest:
        if d > T:
            print("NO")
            return
    
    # Compute latest possible day for each injection
    latest = [T] * n
    # Process in reverse topological order
    for u in reversed(topo):
        for v in adj[u]:
            if latest[u] > latest[v] - 1:
                latest[u] = latest[v] - 1
    
    # Check if any latest day is less than 1
    for d in latest:
        if d < 1:
            print("NO")
            return
    
    # Check if earliest > latest for any injection
    for i in range(n):
        if earliest[i] > latest[i]:
            print("NO")
            return
    
    # Greedy assignment: assign each injection to its earliest possible day
    # respecting capacity constraints
    days = [0] * n
    capacity = [0] * (T + 2)  # capacity[d] = number of injections assigned to day d
    
    for u in topo:
        d = earliest[u]
        # Find the earliest day >= d that has capacity < M and <= latest[u]
        while d <= latest[u] and capacity[d] >= M:
            d += 1
        if d > latest[u]:
            print("NO")
            return
        days[u] = d
        capacity[d] += 1
    
    print("YES")
    print(' '.join(map(str, days)))

if __name__ == "__main__":
    solve()