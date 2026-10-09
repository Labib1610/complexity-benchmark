import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    pairs = {}
    for _ in range(t):
        x, y, z = map(int, input().split())
        pairs.setdefault((x, y), []).append(z)
    
    # Build bipartite graph: left = (x,y) pairs, right = time slots
    pair_list = list(pairs.keys())
    n = len(pair_list)
    if n < k:
        print("NO")
        return
    
    # Map pair index to time slots
    adj = [[] for _ in range(n)]
    for i, (x, y) in enumerate(pair_list):
        for z in pairs[(x, y)]:
            adj[i].append(z - 1)  # 0-based time slot
    
    # Hopcroft-Karp for maximum bipartite matching
    match_right = [-1] * k
    match_left = [-1] * n
    dist = [0] * n
    
    def bfs():
        q = deque()
        for u in range(n):
            if match_left[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = -1
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                mu = match_right[v]
                if mu == -1:
                    found = True
                elif dist[mu] == -1:
                    dist[mu] = dist[u] + 1
                    q.append(mu)
        return found
    
    def dfs(u):
        for v in adj[u]:
            mu = match_right[v]
            if mu == -1 or (dist[mu] == dist[u] + 1 and dfs(mu)):
                match_left[u] = v
                match_right[v] = u
                return True
        dist[u] = -1
        return False
    
    matching = 0
    while bfs():
        for u in range(n):
            if match_left[u] == -1 and dfs(u):
                matching += 1
    
    if matching < k:
        print("NO")
        return
    
    # Build output
    print("YES")
    for i, (x, y) in enumerate(pair_list):
        if match_left[i] != -1:
            z = match_left[i] + 1
            print(x, y, z)

if __name__ == "__main__":
    main()