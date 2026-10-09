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
    
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        radj[b].append(a)
    
    # Topological sort using Kahn's algorithm
    indeg = [0] * n
    for u in range(n):
        for v in adj[u]:
            indeg[v] += 1
    
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
        # Cycle in graph - impossible to schedule
        print("NO")
        return
    
    # Compute longest path distances (minimum slot each task can be in)
    dist = [0] * n
    for u in topo:
        for v in adj[u]:
            if dist[v] < dist[u] + 1:
                dist[v] = dist[u] + 1
    
    if max(dist) >= T:
        print("NO")
        return
    
    # Create buckets for each deadline (latest slot a task can be scheduled)
    # We bucket by the maximum slot each task can be placed
    buckets = [[] for _ in range(T)]
    for i in range(n):
        max_deadline = T - 1 - dist[i]
        buckets[max_deadline].append(i)
    
    # Order tasks by decreasing max_deadline, then topological order
    order = []
    for d in range(T - 1, -1, -1):
        # Tasks in bucket d all have max_deadline = d
        # Sort by topological order to maintain proper ordering
        if buckets[d]:
            buckets[d].sort(key=lambda x: topo.index(x))
            order.extend(buckets[d])
    
    # Greedy scheduling: assign each task to the latest possible slot
    slots = [0] * n
    slot_count = [0] * T
    
    for task in order:
        # Find the latest available slot that respects precedence
        for s in range(dist[task], T):
            if slot_count[s] < M:
                slots[task] = s
                slot_count[s] += 1
                break
        else:
            print("NO")
            return
    
    # Verify constraints
    for u in range(n):
        for v in adj[u]:
            if slots[u] >= slots[v]:
                print("NO")
                return
    
    print("YES")
    print(' '.join(str(x + 1) for x in slots))

if __name__ == "__main__":
    solve()