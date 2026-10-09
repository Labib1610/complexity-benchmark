import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    # Power modules: 1 to q
    # Habitation modules: q+1 to 2q
    # We'll use 0-indexed internally for convenience
    
    # Build adjacency list
    adj = [[] for _ in range(q)]
    for _ in range(t):
        a = int(next(it)) - 1  # 0-indexed power module
        b = int(next(it)) - 1  # 0-indexed habitation module
        adj[a].append(b)
    
    # We need to find a perfect matching
    # Using Hopcroft-Karp algorithm
    
    # match_power[i] = matched habitation module for power i, or -1
    # match_hab[j] = matched power module for habitation j, or -1
    match_power = [-1] * q
    match_hab = [-1] * q
    
    INF = q + 5
    
    def bfs():
        dist = [INF] * q
        dq = deque()
        for u in range(q):
            if match_power[u] == -1:
                dist[u] = 0
                dq.append(u)
        
        found = False
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                u2 = match_hab[v]
                if u2 != -1 and dist[u2] == INF:
                    dist[u2] = dist[u] + 1
                    dq.append(u2)
                elif u2 == -1:
                    found = True
        return dist, found
    
    def dfs(u, dist):
        for v in adj[u]:
            u2 = match_hab[v]
            if u2 == -1 or (dist[u2] == dist[u] + 1 and dfs(u2, dist)):
                match_power[u] = v
                match_hab[v] = u
                return True
        dist[u] = INF
        return False
    
    matching_size = 0
    while True:
        dist, found = bfs()
        if not found:
            break
        for u in range(q):
            if match_power[u] == -1:
                if dfs(u, dist):
                    matching_size += 1
    
    if matching_size != q:
        print("NO")
    else:
        print("YES")
        for i in range(q):
            print(f"{i+1} {match_power[i]+1}")

if __name__ == "__main__":
    solve()