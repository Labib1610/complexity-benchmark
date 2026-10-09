import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    t = int(input_data[1])
    
    # Store for each x its associated y
    # and adjacency list for x -> z
    y_of_x = [0] * (k + 1)
    adj = [[] for _ in range(k + 1)]
    
    idx = 2
    for _ in range(t):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        z = int(input_data[idx+2])
        idx += 3
        y_of_x[x] = y
        adj[x].append(z)
        
    # Hopcroft-Karp bipartite matching between X (1..k) and Z (1..k)
    pair_u = [0] * (k + 1)
    pair_v = [0] * (k + 1)
    dist = [0] * (k + 1)
    INF = float('inf')
    
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
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = v
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

    if matching == k:
        out = ["YES"]
        for x in range(1, k + 1):
            out.append(f"{x} {y_of_x[x]} {pair_u[x]}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()