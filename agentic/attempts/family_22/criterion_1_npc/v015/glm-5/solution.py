import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n+1)]
    indeg = [0]*(n+1)
    
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        indeg[b] += 1
    
    # earliest shift for each component (1-indexed)
    earliest = [1]*(n+1)
    q = deque()
    for i in range(1, n+1):
        if indeg[i] == 0:
            q.append(i)
    
    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            if earliest[v] < earliest[u] + 1:
                earliest[v] = earliest[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(topo_order) != n:
        print("NO")
        return
    
    max_earliest = max(earliest[1:])
    if max_earliest > T:
        print("NO")
        return
    
    # latest shift for each component
    latest = [T]*(n+1)
    radj = [[] for _ in range(n+1)]
    for u in range(1, n+1):
        for v in adj[u]:
            radj[v].append(u)
    
    q = deque()
    for i in range(1, n+1):
        if not adj[i]:
            q.append(i)
    
    while q:
        v = q.popleft()
        for u in radj[v]:
            if latest[u] > latest[v] - 1:
                latest[u] = latest[v] - 1
            indeg[u] -= 1
            if indeg[u] == 0:
                q.append(u)
    
    # Check feasibility of latest times
    for i in range(1, n+1):
        if latest[i] < 1:
            print("NO")
            return
    
    # Build list of (earliest, latest, component)
    jobs = [(earliest[i], latest[i], i) for i in range(1, n+1)]
    # Sort by latest ascending, then earliest ascending
    jobs.sort(key=lambda x: (x[1], x[0]))
    
    schedule = [0]*(n+1)
    # For each shift, track how many jobs assigned
    shift_count = [0]*(T+2)
    
    for e, l, idx in jobs:
        assigned = False
        for s in range(e, l+1):
            if shift_count[s] < M:
                schedule[idx] = s
                shift_count[s] += 1
                assigned = True
                break
        if not assigned:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, schedule[1:])))

if __name__ == "__main__":
    solve()