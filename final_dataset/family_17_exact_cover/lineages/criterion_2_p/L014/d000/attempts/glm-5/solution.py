import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    n = 2 * q
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        adj[b].append(a)
    
    pairU = [0] * (n + 1)
    pairV = [0] * (n + 1)
    dist = [0] * (n + 1)
    
    def bfs():
        queue = deque()
        for u in range(1, q + 1):
            if pairU[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = 0
        dist[0] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[pairV[v]] == 0:
                        dist[pairV[v]] = dist[u] + 1
                        queue.append(pairV[v])
        return dist[0] != float('inf')
    
    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[pairV[v]] == dist[u] + 1:
                    if dfs(pairV[v]):
                        pairV[v] = u
                        pairU[u] = v
                        return True
            dist[u] = 0
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pairU[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, pairU[u])
    else:
        print("NO")

if __name__ == "__main__":
    solve()