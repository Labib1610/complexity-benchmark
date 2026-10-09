import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    M = int(input_data[idx]); idx += 1
    T = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    in_deg = [0] * (n + 1)
    
    for _ in range(m):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        adj[a].append(b)
        radj[b].append(a)
        in_deg[b] += 1
    
    # Topological order
    q = deque()
    for i in range(1, n + 1):
        if in_deg[i] == 0:
            q.append(i)
    
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
    
    # Earliest shift for each module (longest path ending at node)
    earliest = [1] * (n + 1)
    for u in topo:
        for v in adj[u]:
            if earliest[v] < earliest[u] + 1:
                earliest[v] = earliest[u] + 1
    
    # Check feasibility of earliest shifts
    for i in range(1, n + 1):
        if earliest[i] > T:
            print("NO")
            return
    
    # Greedy assignment: process in topological order, assign to earliest valid shift
    shift = [0] * (n + 1)
    count = [0] * (T + 2)  # count[i] = modules assigned to shift i
    
    for u in topo:
        min_s = earliest[u]
        for p in radj[u]:
            if shift[p] + 1 > min_s:
                min_s = shift[p] + 1
        
        s = min_s
        while s <= T and count[s] >= M:
            s += 1
        
        if s > T:
            print("NO")
            return
        
        shift[u] = s
        count[s] += 1
    
    print("YES")
    print(' '.join(str(shift[i]) for i in range(1, n + 1)))

solve()