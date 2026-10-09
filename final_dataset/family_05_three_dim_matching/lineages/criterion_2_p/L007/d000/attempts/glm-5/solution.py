import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # pilot_to_starfighter[pilot] = starfighter
    pilot_to_starfighter = {}
    # missions_for_pilot[pilot] = set of missions
    missions_for_pilot = [[] for _ in range(k + 1)]
    
    for _ in range(t):
        p = int(next(it))
        s = int(next(it))
        m = int(next(it))
        
        if p not in pilot_to_starfighter:
            pilot_to_starfighter[p] = s
        missions_for_pilot[p].append(m)
    
    # Check if all pilots are present
    if len(pilot_to_starfighter) != k:
        print("NO")
        return
    
    # Build bipartite graph between pilots and missions
    adj = [[] for _ in range(k + 1)]
    for p in range(1, k + 1):
        adj[p] = missions_for_pilot[p]
    
    # Hopcroft-Karp for maximum matching
    pair_U = [0] * (k + 1)
    pair_V = [0] * (k + 1)
    dist = [0] * (k + 1)
    NIL = 0
    
    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if pair_U[u] == NIL:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[NIL] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[NIL]:
                for v in adj[u]:
                    if dist[pair_V[v]] == float('inf'):
                        dist[pair_V[v]] = dist[u] + 1
                        queue.append(pair_V[v])
        return dist[NIL] != float('inf')
    
    def dfs(u):
        if u != NIL:
            for v in adj[u]:
                if dist[pair_V[v]] == dist[u] + 1:
                    if dfs(pair_V[v]):
                        pair_V[v] = u
                        pair_U[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_U[u] == NIL:
                if dfs(u):
                    matching += 1
    
    if matching != k:
        print("NO")
    else:
        print("YES")
        for p in range(1, k + 1):
            m = pair_U[p]
            s = pilot_to_starfighter[p]
            print(f"{p} {s} {m}")

if __name__ == "__main__":
    solve()