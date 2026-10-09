import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx+=1
    m = int(input_data[idx]); idx+=1
    one = int(input_data[idx]); idx+=1  # should be 1
    s = int(input_data[idx]); idx+=1
    t = int(input_data[idx]); idx+=1
    d = int(input_data[idx]); idx+=1
    
    # edges
    graph = [[] for _ in range(n+1)]
    to = []
    cap = []
    # store edge ids for original edges: edge i and its reverse i^1
    orig_edge_ids = []
    
    for i in range(m):
        u = int(input_data[idx]); idx+=1
        v = int(input_data[idx]); idx+=1
        c = int(input_data[idx]); idx+=1
        orig_edge_ids.append(len(to))
        graph[u].append(len(to)); to.append(v); cap.append(c)
        graph[v].append(len(to)); to.append(u); cap.append(0)
    
    if d == 0:
        print("YES")
        print(" ".join(["0"]*m))
        return
    
    if s == t:
        print("NO")
        return
    
    # Dinic
    INF = float('inf')
    
    def bfs():
        level = [-1]*(n+1)
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for eid in graph[u]:
                if cap[eid] > 0 and level[to[eid]] < 0:
                    level[to[eid]] = level[u] + 1
                    q.append(to[eid])
        return level
    
    def dfs():
        # iterative DFS finding augmenting paths with current-arc
        # returns total flow pushed
        total = 0
        it = [0]*(n+1)  # current arc index per node
        # We'll do iterative DFS
        # Actually standard approach: recursive with limit; let's do iterative path-based
        ...