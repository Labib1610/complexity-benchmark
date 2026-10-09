import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it))
        M = int(next(it))
        T = int(next(it))
        m = int(next(it))
    except StopIteration:
        return
    
    adj = [[] for _ in range(n + 1)]
    in_deg = [0] * (n + 1)
    
    for _ in range(m):
        try:
            a = int(next(it))
            b = int(next(it))
            adj[a].append(b)
            in_deg[b] += 1
        except StopIteration:
            break
    
    # Kahn's algorithm to find topological order
    q = deque([i for i in range(1, n + 1) if in_deg[i] == 0])
    topo = []
    
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                q.append(v)
    
    if len(topo) != n:
        print("NO")
        return
    
    # Compute earliest possible slot for each task
    earliest = [0] * (n + 1)
    for u in topo:
        for v in adj[u]:
            if earliest[v] < earliest[u] + 1:
                earliest[v] = earliest[u] + 1
    
    # Check if any task's minimum slot exceeds deadline
    max_earliest = max(earliest[1:n + 1])
    if max_earliest >= T:
        print("NO")
        return
    
    # Try to fit tasks: use Earliest-Deadline-First (EDF)
    # Deadline of task u is T-1 - (max_earliest - earliest[u])
    deadlines = [0] * (n + 1)
    for u in range(1, n + 1):
        deadlines[u] = T - 1 - (max_earliest - earliest[u])
    
    # Sort tasks by deadline (ascending), then by earliest (ascending)
    tasks = list(range(1, n + 1))
    tasks.sort(key=lambda x: (deadlines[x], earliest[x]))
    
    slot = [0] * (n + 1)
    slot_usage = [0] * T
    
    for u in tasks:
        # Find earliest available slot that can accommodate this task
        start = earliest[u]
        end = deadlines[u]
        assigned = -1
        for t in range(start, end + 1):
            if slot_usage[t] < M:
                assigned = t
                break
        if assigned == -1:
            print("NO")
            return
        slot[u] = assigned
        slot_usage[assigned] += 1
    
    print("YES")
    print(" ".join(str(slot[i] + 1) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()