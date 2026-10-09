import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx+=1
    m = int(data[idx]); idx+=1
    s = int(data[idx]); idx+=1
    t = int(data[idx]); idx+=1
    B = int(data[idx]); idx+=1
    
    # edges
    E = 2*m
    to = [0]*E
    cap = [0]*E
    graph = [[] for _ in range(n+1)]
    eu = [0]*m
    ev = [0]*m
    ew = [0]*m
    for i in range(m):
        u = int(data[idx]); v = int(data[idx+1]); w = int(data[idx+2]); idx+=3
        eu[i]=u; ev[i]=v; ew[i]=w
        j = 2*i
        to[j] = v; cap[j] = w
        to[j+1] = u; cap[j+1] = w
        graph[u].append(j)
        graph[v].append(j+1)
    
    if s == t:
        print("NO")
        return
    
    INF = float('inf')
    level = [0]*(n+1)
    it = [0]*(n+1)
    
    def bfs():
        for i in range(n+1): level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            lu = level[u] + 1
            for e in graph[u]:
                if cap[e] > 0:
                    v = to[e]
                    if level[v] == -1:
                        level[v] = lu
                        q.append(v)
        return level[t] != -1
    
    def dfs(u, f):
        if u == t:
            return f
        while it[u] < len(graph[u]):
            e = graph[u][it[u]]
            v = to[e]
            if cap[e] > 0 and level[v] == level[u]+1:
                d = dfs(v, min(f, cap[e]))
                if d > 0:
                    cap[e] -= d
                    cap[e^1] += d
                    return d
            it[u] += 1
        return 0
    
    flow = 0
    while bfs():
        for i in range(n+1): it[i] = 0
        while True:
            f = dfs(s, INF)
            if f == 0: break
            flow += f
    
    if flow > B:
        print("NO")
        return
    
    # find S: reachable from s in residual
    # reuse bfs-like: level from last bfs has level[t] == -1 (since loop ended), and level = reachable set!
    # Actually after the final bfs() returns False, level[] marks reachable vertices (level != -1).
    # But careful: the last successful bfs was followed by augmentation which changes residual.
    # So we need a fresh reachability computation after the final augmentation.