import sys
from collections import deque

def hopcroft_karp(graph, U, V_count):
    pair_u = [-1] * (U + 1)
    pair_v = [-1] * (V_count + 1)
    dist = [0] * (U + 1)

    def bfs():
        q = deque()
        for u in range(1, U + 1):
            if pair_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = float('inf')
        found = False
        while q:
            u = q.popleft()
            for v in graph[u]:
                if pair_v[v] == -1:
                    found = True
                else:
                    if dist[pair_v[v]] == float('inf'):
                        dist[pair_v[v]] = dist[u] + 1
                        q.append(pair_v[v])
        return found

    def dfs(u):
        for v in graph[u]:
            if pair_v[v] == -1 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = float('inf')
        return False

    matching = 0
    while bfs():
        for u in range(1, U + 1):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching, pair_u

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # allowed[x][z] = set of machines y
    allowed = [[set() for _ in range(k + 1)] for _ in range(k + 1)]
    triples = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        allowed[x][z].add(y)
        triples.append((x, y, z))
    
    # We will assign specialists to time slots.
    # For a fixed assignment (x -> z), we build graph and check if machines can be matched.
    
    # To reduce search, we sort specialists by number of allowed triples (small domain first)
    specialists = list(range(1, k + 1))
    
    # Precompute possible z for each x
    possible_z = [list(range(1, k + 1)) for _ in range(k + 1)]
    
    used_z = [False] * (k + 1)
    assignment = [-1] * (k + 1)  # assignment[x] = z
    
    result_edges = []
    
    def dfs(x_idx):
        if x_idx == k:
            # All specialists assigned to time slots, now match machines
            graph = [[] for _ in range(k + 1)]
            for x in range(1, k + 1):
                z = assignment[x]
                for y in allowed[x][z]:
                    graph[x].append(y)
            matching, pair_u = hopcroft_karp(graph, k, k)
            if matching == k:
                for x in range(1, k + 1):
                    y = pair_u[x]
                    z = assignment[x]
                    result_edges.append((x, y, z))
                return True
            return False
        
        x = specialists[x_idx]
        # Try assigning this specialist to an unused time slot
        for z in range(1, k + 1):
            if not used_z[z] and allowed[x][z]:
                used_z[z] = True
                assignment[x] = z
                if dfs(x_idx + 1):
                    return True
                assignment[x] = -1
                used_z[z] = False
        return False
    
    if dfs(0):
        print("YES")
        for x, y, z in result_edges:
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()