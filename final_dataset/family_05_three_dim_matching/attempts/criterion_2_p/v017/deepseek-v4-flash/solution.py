import sys
from collections import deque

input = sys.stdin.readline

def main():
    k, t = map(int, input().split())
    # operator -> terminal mapping
    op_terminal = {}
    # adjacency list: operator index -> list of windows
    adj = [[] for _ in range(k)]
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        z -= 1
        op_terminal[x] = y
        adj[x].append(z)
    
    # Hopcroft-Karp for maximum bipartite matching
    # left: operators (0..k-1), right: windows (0..k-1)
    pair_u = [-1] * k
    pair_v = [-1] * k
    dist = [0] * k
    
    def bfs():
        q = deque()
        for u in range(k):
            if pair_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = float('inf')
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pair_v[v]
                if pu != -1 and dist[pu] == float('inf'):
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    found = True
        return found
    
    def dfs(u):
        for v in adj[u]:
            pu = pair_v[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = float('inf')
        return False
    
    matching = 0
    while bfs():
        for u in range(k):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    
    if matching != k:
        print("NO")
        return
    
    print("YES")
    for u in range(k):
        v = pair_u[u]
        print(u + 1, op_terminal[u] + 1, v + 1)

if __name__ == "__main__":
    main()