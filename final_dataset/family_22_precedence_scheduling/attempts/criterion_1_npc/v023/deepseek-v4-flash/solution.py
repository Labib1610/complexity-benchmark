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
    
    # Kahn's topological sort
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
    
    phase = [0] * n
    capacity = [0] * (T + 1)  # 1-indexed phases
    
    for u in topo:
        # earliest phase = max(phase of predecessors) + 1
        earliest = 1
        # We need to know predecessors; we can compute by scanning all edges
        # but that's O(n+m) if we store reverse edges.
        # Instead, we can compute earliest by checking all nodes that point to u.
        # We'll precompute reverse adjacency.
        pass
    
    # Let's do it properly with reverse adjacency
    rev_adj = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            rev_adj[v].append(u)
    
    phase = [0] * n
    capacity = [0] * (T + 1)
    
    for u in topo:
        # find earliest phase
        earliest = 1
        for p in rev_adj[u]:
            earliest = max(earliest, phase[p] + 1)
        # find first phase >= earliest with capacity < M
        p = earliest
        while p <= T and capacity[p] >= M:
            p += 1
        if p > T:
            print("NO")
            return
        phase[u] = p
        capacity[p] += 1
    
    print("YES")
    print(" ".join(str(phase[i]) for i in range(n)))

if __name__ == "__main__":
    solve()