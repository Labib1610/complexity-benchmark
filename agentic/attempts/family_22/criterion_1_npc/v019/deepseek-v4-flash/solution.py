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
    
    # Topological sort with earliest serving time
    q = deque()
    earliest = [1] * n
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
    
    # Now assign serving numbers respecting capacity
    serving_count = [0] * (T + 1)
    serving = [0] * n
    
    for u in topo_order:
        # Find smallest serving >= earliest[u] with capacity < M
        s = earliest[u]
        while s <= T and serving_count[s] >= M:
            s += 1
        if s > T:
            print("NO")
            return
        serving[u] = s
        serving_count[s] += 1
    
    print("YES")
    print(" ".join(str(serving[i]) for i in range(n)))

if __name__ == "__main__":
    solve()