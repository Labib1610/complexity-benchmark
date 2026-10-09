from collections import deque, defaultdict
import sys

def solve():
    data = sys.stdin.read().strip().split()
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
    
    # topological order using Kahn's algorithm
    q = deque()
    for i in range(1, n+1):
        if indeg[i] == 0:
            q.append(i)
    
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
    
    slot = [0]*(n+1)
    # earliest possible slot respecting precedence
    for u in topo:
        if slot[u] == 0:
            slot[u] = 1
        for v in adj[u]:
            slot[v] = max(slot[v], slot[u] + 1)
    
    # Now assign slots respecting capacity
    # We'll try to push jobs later if needed to respect capacity
    # Use a priority queue per slot to assign jobs
    from heapq import heappush, heappop
    
    # group jobs by their earliest slot
    by_slot = defaultdict(list)
    for i in range(1, n+1):
        by_slot[slot[i]].append(i)
    
    # We'll process slots from 1 to T
    # For each slot, we have capacity M
    # Jobs that can be scheduled at slot s are those with earliest <= s
    # and all predecessors already scheduled.
    
    # We'll do a greedy: schedule jobs as early as possible, but if capacity exceeded,
    # push some to later slots.
    
    # Recompute indegrees for scheduling
    indeg2 = [0]*(n+1)
    adj2 = [[] for _ in range(n+1)]
    for a in range(1, n+1):
        for b in adj[a]:
            adj2[a].append(b)
            indeg2[b] += 1
    
    ready = []
    for i in range(1, n+1):
        if indeg2[i] == 0:
            heappush(ready, (slot[i], i))
    
    assigned = [0]*(n+1)
    current_slot = 1
    scheduled_count = 0
    
    while scheduled_count < n:
        if current_slot > T:
            print("NO")
            return
        # pick up to M jobs for this slot
        count = 0
        temp = []
        while ready and count < M:
            earliest, job = heappop(ready)
            if earliest <= current_slot:
                assigned[job] = current_slot
                scheduled_count += 1
                count += 1
                # release dependents
                for v in adj2[job]:
                    indeg2[v] -= 1
                    if indeg2[v] == 0:
                        heappush(ready, (slot[v], v))
            else:
                temp.append((earliest, job))
        # put back jobs not scheduled
        for item in temp:
            heappush(ready, item)
        current_slot += 1
    
    # check deadline
    if max(assigned[1:]) > T:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(assigned[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    solve()