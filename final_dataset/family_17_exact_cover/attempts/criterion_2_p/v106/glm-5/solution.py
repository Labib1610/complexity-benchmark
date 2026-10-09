import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    # adjacency list
    adj = [[] for _ in range(q + 1)]  # adj[u] for u in 1..q, list of right vertices (0-indexed 0..q-1)
    
    for _ in range(t):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        adj[a].append(b - q - 1)  # right vertex index 0..q-1
    
    matchL = [-1] * (q + 1)  # matchL[u] = right vertex
    matchR = [-1] * q        # matchR[v] = left vertex (1..q)
    
    INF = float('inf')
    
    # Hopcroft-Karp
    def bfs():
        dist_local = [INF] * (q + 1)
        queue = deque()
        for u in range(1, q + 1):
            if matchL[u] == -1:
                dist_local[u] = 0
                queue.append(u)
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                w = matchR[v]
                if w == -1:
                    found = True
                elif dist_local[w] == INF:
                    dist_local[w] = dist_local[u] + 1
                    queue.append(w)
        return found, dist_local
    
    def dfs(u, dist_local):
        for v in adj[u]:
            w = matchR[v]
            if w == -1 or (dist_local[w] == dist_local[u] + 1 and dfs(w, dist_local)):
                matchL[u] = v
                matchR[v] = u
                return True
        dist_local[u] = INF
        return False
    
    matching = 0
    while True:
        found, dist_local = bfs()
        if not found:
            break
        for u in range(1, q + 1):
            if matchL[u] == -1:
                if dfs(u, dist_local):
                    matching += 1
    
    if matching == q:
        out = ["YES"]
        for u in range(1, q + 1):
            out.append(f"{u} {matchL[u] + q + 1}")
        print("\n".join(out))
    else:
        print("NO")

main()