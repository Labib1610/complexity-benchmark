import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    # Build adjacency list for bipartite graph
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
    
    # Sort adjacency lists for deterministic matching (optional but helpful)
    for i in range(1, q + 1):
        adj[i].sort()
    
    # Bipartite matching using Hopcroft-Karp
    # Left side: Alpha isotopes 1 to q
    # Right side: Beta isotopes q+1 to 2q
    
    match_r = {}  # match_r[b] = a if b is matched to a
    INF = float('inf')
    
    def bfs():
        dist = {}
        queue = deque()
        for u in range(1, q + 1):
            if u not in match_r.values():
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[None] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[None]:
                for v in adj[u]:
                    # Find what v is matched to
                    matched_u = None
                    for key, val in match_r.items():
                        if val == v:
                            matched_u = key
                            break
                    if matched_u is not None and matched_u not in dist:
                        dist[matched_u] = dist[u] + 1
                        queue.append(matched_u)
                    elif matched_u is None:
                        dist[None] = dist[u] + 1
        return dist[None] != INF
    
    def dfs(u, dist):
        for v in adj[u]:
            matched_u = None
            for key, val in match_r.items():
                if val == v:
                    matched_u = key
                    break
            if matched_u is None:
                if dist.get(None, INF) == dist[u] + 1:
                    match_r[v] = u
                    return True
            elif matched_u in dist and dist[matched_u] == dist[u] + 1:
                if dfs(matched_u, dist):
                    match_r[v] = u
                    return True
        dist[u] = INF
        return False
    
    # Hopcroft-Karp main loop
    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if u not in match_r.values():
                if dfs(u, {}):
                    matching += 1
    
    if matching != q:
        print("NO")
        return
    
    # Check sum constraints
    sum_a = sum(match_r.values())
    sum_b = sum(match_r.keys())
    target_a = q * (q + 1) // 2
    target_b = q * (3 * q + 1) // 2
    
    if sum_a != target_a or sum_b != target_b:
        print("NO")
        return
    
    print("YES")
    for b, a in match_r.items():
        print(a, b)

if __name__ == "__main__":
    solve()