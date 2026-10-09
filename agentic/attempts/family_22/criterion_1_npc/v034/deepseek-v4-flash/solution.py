from collections import deque
import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
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
    
    # Kahn's algorithm with cycle detection
    q = deque()
    for i in range(n):
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
    
    # Assign cycles
    cycle = [0] * n
    # We'll process in topological order, assigning earliest possible cycle
    # but also respecting capacity M per cycle.
    # We'll keep track of how many procedures are assigned to each cycle.
    count_in_cycle = [0] * (T + 1)
    
    for u in topo:
        # Earliest cycle = max(cycle of predecessors) + 1
        earliest = 1
        for v in adj[u]:
            # Actually we need predecessors, so we need reverse adjacency
            pass
    
    # Better: build reverse adjacency for predecessors
    preds = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            preds[v].append(u)
    
    for u in topo:
        if preds[u]:
            earliest = max(cycle[p] for p in preds[u]) + 1
        else:
            earliest = 1
        
        # Find earliest cycle with capacity
        c = earliest
        while c <= T and count_in_cycle[c] >= M:
            c += 1
        if c > T:
            print("NO")
            return
        cycle[u] = c
        count_in_cycle[c] += 1
    
    print("YES")
    print(" ".join(str(cycle[i]) for i in range(n)))

if __name__ == "__main__":
    solve()