import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # drone -> station mapping
    drone_station = {}
    # adjacency: drone -> list of frequencies
    adj = [[] for _ in range(k + 1)]
    
    for _ in range(t):
        d, c, f = map(int, input().split())
        drone_station[d] = c
        adj[d].append(f)
    
    # Hopcroft-Karp for maximum bipartite matching
    # Left: drones (1..k), Right: frequencies (1..k)
    pair_u = [0] * (k + 1)  # drone -> frequency
    pair_v = [0] * (k + 1)  # frequency -> drone
    dist = [0] * (k + 1)
    
    def bfs():
        q = deque()
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = float('inf')
        dist[0] = float('inf')
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[pair_v[v]] == float('inf'):
                        dist[pair_v[v]] = dist[u] + 1
                        q.append(pair_v[v])
        return dist[0] != float('inf')
    
    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = float('inf')
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
    else:
        print("YES")
        for d in range(1, k + 1):
            f = pair_u[d]
            c = drone_station[d]
            print(d, c, f)

if __name__ == "__main__":
    main()