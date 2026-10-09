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
    
    # Kahn's algorithm to get topological order
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
        print("NO")
        return
    
    # Assign days greedily
    day = [0] * n
    count = [0] * (T + 1)
    
    for u in topo:
        # Earliest day = max(day[predecessor]+1, 1)
        earliest = 1
        for v in adj[u]:
            # Actually we need predecessors, so we need reverse adjacency
            pass
    
    # We need reverse edges to know predecessors
    preds = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            preds[v].append(u)
    
    for u in topo:
        earliest = 1
        for p in preds[u]:
            earliest = max(earliest, day[p] + 1)
        # Find first day >= earliest with capacity
        d = earliest
        while d <= T and count[d] >= M:
            d += 1
        if d > T:
            print("NO")
            return
        day[u] = d
        count[d] += 1
    
    print("YES")
    print(" ".join(str(day[i]) for i in range(n)))

if __name__ == "__main__":
    solve()