import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    adj = [[] for _ in range(q + 1)]
    edges = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        edges.append((a, b))
    
    # Hopcroft-Karp algorithm for maximum bipartite matching
    pair_u = [0] * (q + 1)
    pair_v = [0] * (2 * q + 1)
    dist = [0] * (q + 1)
    
    def bfs():
        queue = deque()
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1
        dist[0] = -1
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if pair_v[v] == 0:
                        if dist[0] == -1:
                            dist[0] = dist[u] + 1
                    elif dist[pair_v[v]] == -1:
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[0] != -1
    
    def dfs(u):
        for v in adj[u]:
            if pair_v[v] == 0 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = -1
        return False
    
    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1
    
    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, pair_u[u])
    else:
        print("NO")

if __name__ == "__main__":
    solve()