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
    radj = [[] for _ in range(n)]
    
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1
    
    # Compute earliest possible slot for each job (topological order)
    earliest = [1] * n
    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            if earliest[v] < earliest[u] + 1:
                earliest[v] = earliest[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(topo) != n:
        print("NO")
        return
    
    # Check if any earliest exceeds deadline
    for i in range(n):
        if earliest[i] > T:
            print("NO")
            return
    
    # Compute latest possible slot for each job (reverse topological order)
    latest = [T] * n
    for u in reversed(topo):
        for v in adj[u]:
            if latest[u] > latest[v] - 1:
                latest[u] = latest[v] - 1
    
    # Check if any latest < earliest
    for i in range(n):
        if latest[i] < earliest[i]:
            print("NO")
            return
    
    # Sort jobs by latest slot (ascending), then by earliest (ascending)
    jobs = list(range(n))
    jobs.sort(key=lambda x: (latest[x], earliest[x]))
    
    slot = [0] * n
    # For each time t, track how many jobs are scheduled
    cnt = [0] * (T + 2)
    
    for job in jobs:
        # Find the earliest available slot >= earliest[job] that has capacity
        t = earliest[job]
        while t <= latest[job] and cnt[t] >= M:
            t += 1
        if t > latest[job]:
            print("NO")
            return
        slot[job] = t
        cnt[t] += 1
    
    print("YES")
    print(' '.join(map(str, slot)))

if __name__ == "__main__":
    solve()