import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    # specialist -> machine (fixed by protocol)
    spec_to_machine = {}
    # machine -> specialist (exclusive assignment)
    machine_to_spec = {}
    # (specialist, machine) -> list of time slots
    sm_to_times = {}
    
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        if x not in spec_to_machine:
            spec_to_machine[x] = y
            machine_to_spec[y] = x
            sm_to_times[(x, y)] = []
        sm_to_times[(x, y)].append(z)
    
    # Specialists that appear in catalogue
    specs = sorted(spec_to_machine.keys())
    n = len(specs)
    
    # If fewer than k specialists appear, impossible (each crew needs distinct specialist)
    if n < k:
        print("NO")
        return
    
    # Build bipartite graph: left = specialists (0..n-1), right = time slots (0..k-1)
    # Edge if (specialist, its_machine) has that time slot available
    adj = [[] for _ in range(n)]
    for i, s in enumerate(specs):
        m = spec_to_machine[s]
        for z in sm_to_times[(s, m)]:
            adj[i].append(z - 1)  # 0-indexed time slot
    
    # Hopcroft-Karp for maximum matching
    pair_u = [-1] * n  # which time slot each specialist is matched to
    pair_v = [-1] * k  # which specialist each time slot is matched to
    dist = [0] * n
    NIL = -1
    INF = float('inf')
    
    from collections import deque
    
    def bfs():
        queue = deque()
        for u in range(n):
            if pair_u[u] == NIL:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        d = INF
        while queue:
            u = queue.popleft()
            if dist[u] < d:
                for v in adj[u]:
                    if pair_v[v] != NIL:
                        if dist[pair_v[v]] == INF:
                            dist[pair_v[v]] = dist[u] + 1
                            queue.append(pair_v[v])
                    else:
                        d = dist[u] + 1
        return d != INF
    
    def dfs(u, d):
        if dist[u] > d:
            return False
        for v in adj[u]:
            if pair_v[v] == NIL or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v], d)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False
    
    matching = 0
    while bfs():
        d = max((dist[u] for u in range(n) if dist[u] != INF), default=INF)
        for u in range(n):
            if pair_u[u] == NIL:
                if dfs(u, d):
                    matching += 1
    
    if matching < k:
        print("NO")
        return
    
    # We have exactly k matches (since we need k distinct specialists and k distinct time slots)
    # pair_u[i] gives the time slot for specialist specs[i]
    print("YES")
    for i in range(k):
        s = specs[i]
        m = spec_to_machine[s]
        z = pair_u[i] + 1  # back to 1-indexed
        print(f"{s} {m} {z}")

solve()