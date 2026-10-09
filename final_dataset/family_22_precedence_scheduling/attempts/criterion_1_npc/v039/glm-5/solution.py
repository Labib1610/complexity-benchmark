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
    
    # Compute longest path to each node (earliest start time)
    earliest = [1] * n
    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    
    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            if earliest[u] + 1 > earliest[v]:
                earliest[v] = earliest[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(topo_order) != n:
        print("NO")
        return
    
    # Check if any job needs to start after T
    for i in range(n):
        if earliest[i] > T:
            print("NO")
            return
    
    # Compute latest start time for each node
    latest = [T] * n
    radj = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            radj[v].append(u)
    
    q = deque()
    for i in range(n):
        if not radj[i]:
            q.append(i)
    
    while q:
        v = q.popleft()
        for u in radj[v]:
            if latest[v] - 1 < latest[u]:
                latest[u] = latest[v] - 1
            # Check if we need to process u
            # We process when all successors are processed
            # Actually, we just need to update and continue
            # Since we're iterating in reverse topological order implicitly
            pass
    
    # Better approach: process in reverse topological order
    latest = [T] * n
    for v in reversed(topo_order):
        for u in radj[v]:
            if latest[v] - 1 < latest[u]:
                latest[u] = latest[v] - 1
    
    # Check feasibility
    for i in range(n):
        if earliest[i] > latest[i]:
            print("NO")
            return
    
    # Greedy assignment: assign each job to its earliest possible minute
    # respecting capacity constraints
    minute = [0] * n
    cap = [0] * (T + 2)  # cap[t] = number of jobs assigned to minute t
    
    # Sort jobs by earliest start time, then by latest start time (as tie-breaker)
    jobs = list(range(n))
    jobs.sort(key=lambda x: (earliest[x], latest[x]))
    
    for job in jobs:
        t = earliest[job]
        while t <= latest[job] and cap[t] >= M:
            t += 1
        if t > latest[job]:
            print("NO")
            return
        minute[job] = t
        cap[t] += 1
    
    print("YES")
    print(' '.join(map(str, minute)))

if __name__ == "__main__":
    solve()