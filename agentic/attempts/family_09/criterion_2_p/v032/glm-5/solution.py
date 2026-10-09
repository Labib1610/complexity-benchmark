import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx+=1
    m = int(input_data[idx]); idx+=1
    k = int(input_data[idx]); idx+=1
    
    # adjacency
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(input_data[idx]); idx+=1
        v = int(input_data[idx]); idx+=1
        adj[u].append(v)
        adj[v].append(u)
    
    # 2-color
    color = [-1]*(n+1)
    for s in range(1, n+1):
        if color[s] == -1:
            color[s] = 0
            stack = [s]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u]^1
                        stack.append(v)
    # sides
    # L = color 0, R = color 1
    
    # Build adjacency for left side only: adjL[u] = neighbors v (right side)
    # matchL[u] = matched right vertex or 0, matchR[v] = matched left vertex or 0
    
    left_nodes = [u for u in range(1, n+1) if color[u]==0]
    
    INF = float('inf')
    
    matchL = [0]*(n+1)  # for left vertices
    matchR = [0]*(n+1)  # for right vertices
    
    # Hopcroft-Karp
    # dist array for left vertices
    dist = [0]*(n+1)
    
    def bfs():
        q = deque()
        for u in left_nodes:
            if matchL[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                w = matchR[v]
                if w == 0:
                    found = True
                elif dist[w] == INF:
                    dist[w] = dist[u]+1
                    q.append(w)
        return found
    
    def dfs(u):
        # iterative DFS
        ...