import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    n_left = q
    n_right = q
    total_nodes = n_left + n_right
    
    adj = [[] for _ in range(total_nodes + 1)]
    
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        adj[b].append(a)
    
    pair_u = [0] * (n_left + 1)
    pair_v = [0] * (n_right + 1)
    dist = [0] * (n_left + 1)
    
    def bfs():
        queue = deque()
        for u in range(1, n_left + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                pu = pair_v[v - n_left]
                if pu != 0 and dist[pu] == -1:
                    dist[pu] = dist[u] + 1
                    queue.append(pu)
                elif pu == 0:
                    found = True
        return found
    
    def dfs(u):
        for v in adj[u]:
            pu = pair_v[v - n_left]
            if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v - n_left] = u
                return True
        dist[u] = -1
        return False
    
    matching = 0
    while bfs():
        for u in range(1, n_left + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1
    
    if matching != q:
        print("NO")
    else:
        print("YES")
        for u in range(1, n_left + 1):
            print(u, pair_u[u])

if __name__ == "__main__":
    solve()