import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    # For each drone, store its station and the set of available frequencies
    drone_station = [0] * (k + 1)
    # adj[d] = list of frequencies available for drone d
    adj = [[] for _ in range(k + 1)]
    # config_idx[d][f] = index in input of the configuration (d, station, f)
    config_idx = [dict() for _ in range(k + 1)]
    
    for i in range(t):
        d = int(input_data[idx]); idx += 1
        c = int(input_data[idx]); idx += 1
        f = int(input_data[idx]); idx += 1
        drone_station[d] = c
        adj[d].append(f)
        config_idx[d][f] = i
    
    # Hopcroft-Karp for bipartite matching: drones (1..k) to frequencies (1..k)
    # pair_d[d] = matched frequency for drone d, or 0
    # pair_f[f] = matched drone for frequency f, or 0
    pair_d = [0] * (k + 1)
    pair_f = [0] * (k + 1)
    INF = float('inf')
    
    def bfs():
        dist = [0] * (k + 1)
        queue = deque()
        for d in range(1, k + 1):
            if pair_d[d] == 0:
                dist[d] = 0
                queue.append(d)
            else:
                dist[d] = INF
        dist_null = INF
        while queue:
            d = queue.popleft()
            if dist[d] < dist_null:
                for f in adj[d]:
                    nd = pair_f[f]
                    if nd == 0:
                        dist_null = dist[d] + 1
                    elif dist[nd] == INF:
                        dist[nd] = dist[d] + 1
                        queue.append(nd)
        return dist_null != INF, dist
    
    def dfs(d, dist):
        for f in adj[d]:
            nd = pair_f[f]
            if nd == 0 or (dist[nd] == dist[d] + 1 and dfs(nd, dist)):
                pair_d[d] = f
                pair_f[f] = d
                return True
        dist[d] = INF
        return False
    
    matching = 0
    while True:
        found, dist = bfs()
        if not found:
            break
        for d in range(1, k + 1):
            if pair_d[d] == 0:
                if dfs(d, dist):
                    matching += 1
    
    if matching < k:
        print("NO")
        return
    
    print("YES")
    out = []
    for d in range(1, k + 1):
        f = pair_d[d]
        c = drone_station[d]
        out.append(f"{d} {c} {f}")
    print('\n'.join(out))

solve()