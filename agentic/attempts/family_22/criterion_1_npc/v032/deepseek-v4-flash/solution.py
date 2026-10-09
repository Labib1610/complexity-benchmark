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
    
    # earliest phase for each module
    earliest = [1] * n
    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    
    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            earliest[v] = max(earliest[v], earliest[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(topo_order) != n:
        print("NO")
        return
    
    # Check if earliest exceeds T
    if max(earliest) > T:
        print("NO")
        return
    
    # Assign phases greedily: sort by earliest, then fill capacity
    modules = list(range(n))
    modules.sort(key=lambda x: earliest[x])
    
    phase_count = [0] * (T + 1)
    assignment = [0] * n
    
    for u in modules:
        # find earliest feasible phase >= earliest[u]
        p = earliest[u]
        while p <= T and phase_count[p] >= M:
            p += 1
        if p > T:
            print("NO")
            return
        assignment[u] = p
        phase_count[p] += 1
    
    print("YES")
    print(" ".join(str(assignment[i]) for i in range(n)))

if __name__ == "__main__":
    solve()