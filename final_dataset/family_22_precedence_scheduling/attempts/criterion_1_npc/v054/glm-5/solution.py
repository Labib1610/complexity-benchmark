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
    in_degree = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        in_degree[b] += 1
    
    # Kahn's algorithm for topological sort
    q = deque()
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)
    
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    
    if len(topo) != n:
        print("NO")
        return
    
    # Compute earliest start times (forward pass)
    earliest = [1] * n
    for u in topo:
        for v in adj[u]:
            if earliest[v] < earliest[u] + 1:
                earliest[v] = earliest[u] + 1
    
    # Check if any step must start after T
    for i in range(n):
        if earliest[i] > T:
            print("NO")
            return
    
    # Compute latest start times (backward pass)
    latest = [T] * n
    rev_adj = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            rev_adj[v].append(u)
    
    for u in reversed(topo):
        for v in rev_adj[u]:
            if latest[v] > latest[u] - 1:
                latest[v] = latest[u] - 1
    
    # Check consistency
    for i in range(n):
        if earliest[i] > latest[i]:
            print("NO")
            return
    
    # Greedy assignment: assign each step to its earliest available cycle
    # respecting capacity constraints
    result = [0] * n
    # Group steps by their earliest start time
    by_earliest = [[] for _ in range(T + 1)]
    for i in range(n):
        by_earliest[earliest[i]].append(i)
    
    # Sort each group by latest start time (ascending) for priority
    for t in range(1, T + 1):
        by_earliest[t].sort(key=lambda x: latest[x])
    
    # Track which steps are ready to be scheduled
    ready = set()
    for i in range(n):
        if earliest[i] == 1:
            ready.add(i)
    
    scheduled = [False] * n
    # For each step, track how many predecessors are still unscheduled
    pred_count = [0] * n
    for u in range(n):
        for v in adj[u]:
            pred_count[v] += 1
    
    for cycle in range(1, T + 1):
        # Add steps that become ready at this cycle
        for i in by_earliest[cycle]:
            if not scheduled[i] and pred_count[i] == 0:
                ready.add(i)
        
        # Select up to M steps to schedule, prioritizing those with smallest latest time
        to_schedule = []
        for node in ready:
            if not scheduled[node]:
                to_schedule.append((latest[node], node))
        
        to_schedule.sort()
        count = 0
        for _, node in to_schedule:
            if count >= M:
                break
            if latest[node] < cycle:
                print("NO")
                return
            result[node] = cycle
            scheduled[node] = True
            count += 1
            # Update successors
            for v in adj[node]:
                pred_count[v] -= 1
        
        # Remove scheduled nodes from ready
        new_ready = set()
        for node in ready:
            if not scheduled[node]:
                new_ready.add(node)
        ready = new_ready
    
    # Check if all steps are scheduled
    if not all(scheduled):
        print("NO")
        return
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()