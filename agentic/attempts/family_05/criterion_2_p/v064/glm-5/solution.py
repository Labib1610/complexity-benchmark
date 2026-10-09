import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # For each specialist, store list of (machine, time_slot) pairs
    # Since each specialist has a unique machine, we can simplify
    specialist_assignments = [[] for _ in range(k + 1)]
    specialist_machine = [0] * (k + 1)  # The unique machine for each specialist
    
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        specialist_assignments[x].append((y, z))
        specialist_machine[x] = y
    
    # Build bipartite graph: specialists on left, time slots on right
    # Edge from specialist x to time slot z if assignment (x, machine[x], z) exists
    
    # Graph representation for Hopcroft-Karp
    # Left side: specialists 1..k
    # Right side: time slots 1..k
    
    adj = [[] for _ in range(k + 1)]
    for x in range(1, k + 1):
        for y, z in specialist_assignments[x]:
            adj[x].append(z)
    
    # Hopcroft-Karp algorithm
    INF = float('inf')
    pair_u = [0] * (k + 1)  # pair_u[u] = v matched with u (specialist -> time)
    pair_v = [0] * (k + 1)  # pair_v[v] = u matched with v (time -> specialist)
    dist = [0] * (k + 1)
    
    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if pair_v[v] == 0:
                        dist[0] = dist[u] + 1
                    elif dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[0] != INF
    
    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if pair_v[v] == 0 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True
            dist[u] = INF
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching != k:
        print("NO")
        return
    
    print("YES")
    for x in range(1, k + 1):
        z = pair_u[x]
        y = specialist_machine[x]
        print(x, y, z)

if __name__ == "__main__":
    solve()