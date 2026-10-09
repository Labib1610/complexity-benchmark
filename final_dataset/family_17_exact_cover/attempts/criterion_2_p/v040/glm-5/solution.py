import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    # Build adjacency list for transmitters (1 to q)
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
    
    # Receivers are q+1 to 2q, map them to 0..q-1
    match_to_transmitter = [0] * (q + 1)  # match_to_transmitter[r] = transmitter matched to receiver r
    
    def bfs():
        dist = [-1] * (q + 1)
        queue = deque()
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                w = pair_v[v]
                if w != 0 and dist[w] == -1:
                    dist[w] = dist[u] + 1
                    queue.append(w)
                elif w == 0:
                    found = True
        return found, dist
    
    def dfs(u):
        for v in adj[u]:
            w = pair_v[v]
            if w == 0 or (dist[w] == dist[u] + 1 and dfs(w)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = -1
        return False
    
    pair_u = [0] * (q + 1)
    pair_v = [0] * (2 * q + 1)
    
    matching = 0
    while True:
        found, dist = bfs()
        if not found:
            break
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching != q:
        print("NO")
        return
    
    print("YES")
    for u in range(1, q + 1):
        print(u, pair_u[u])

if __name__ == "__main__":
    solve()