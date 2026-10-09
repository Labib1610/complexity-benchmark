import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
    
    # Convert to adjacency list for platforms (index from q+1 to 2q)
    # We'll use 0-indexed internal representation for matching
    # Controllers: 0 to q-1, Platforms: 0 to q-1 (representing q+1 to 2q)
    
    match_platform = [-1] * q  # match_platform[i] = controller matched to platform i
    match_controller = [-1] * q  # match_controller[i] = platform matched to controller i
    
    def bfs():
        dist = [-1] * q
        dq = deque()
        for u in range(q):
            if match_controller[u] == -1:
                dist[u] = 0
                dq.append(u)
        found = False
        while dq:
            u = dq.popleft()
            for b in adj[u + 1]:
                v = b - (q + 1)
                u2 = match_platform[v]
                if u2 != -1 and dist[u2] == -1:
                    dist[u2] = dist[u] + 1
                    dq.append(u2)
                elif u2 == -1:
                    found = True
        return dist, found
    
    def dfs(u, dist):
        for b in adj[u + 1]:
            v = b - (q + 1)
            u2 = match_platform[v]
            if u2 == -1 or (dist[u2] == dist[u] + 1 and dfs(u2, dist)):
                match_platform[v] = u
                match_controller[u] = v
                return True
        dist[u] = -1
        return False
    
    matching_size = 0
    while True:
        dist, found = bfs()
        if not found:
            break
        for u in range(q):
            if match_controller[u] == -1:
                if dfs(u, dist):
                    matching_size += 1
    
    if matching_size != q:
        print("NO")
        return
    
    print("YES")
    for u in range(q):
        v = match_controller[u]
        print(f"{u + 1} {v + q + 1}")

if __name__ == "__main__":
    solve()