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
    
    # Topological levels (minimum slot)
    level = [0] * n
    q = deque([i for i in range(n) if indeg[i] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            if level[v] < level[u] + 1:
                level[v] = level[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(topo) != n:
        print("NO")
        return
    
    # Check if any level exceeds deadline
    for i in range(n):
        if level[i] >= T:
            print("NO")
            return
    
    # Build reverse graph for latest slot computation
    radj = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            radj[v].append(u)
    
    latest = [T - 1] * n
    for u in reversed(topo):
        for v in adj[u]:
            if latest[u] > latest[v] - 1:
                latest[u] = latest[v] - 1
    
    # Check feasibility
    for i in range(n):
        if level[i] > latest[i]:
            print("NO")
            return
    
    # Assign slots greedily by level, then by latest deadline
    slot = [0] * n
    jobs_by_level = [[] for _ in range(T)]
    for i in range(n):
        jobs_by_level[level[i]].append(i)
    
    for L in range(T):
        jobs_by_level[L].sort(key=lambda x: latest[x])
        for u in jobs_by_level[L]:
            slot[u] = L
    
    # Verify capacity constraints
    cap = [0] * T
    for i in range(n):
        cap[slot[i]] += 1
        if cap[slot[i]] > M:
            print("NO")
            return
    
    print("YES")
    print(' '.join(str(x + 1) for x in slot))

if __name__ == "__main__":
    solve()