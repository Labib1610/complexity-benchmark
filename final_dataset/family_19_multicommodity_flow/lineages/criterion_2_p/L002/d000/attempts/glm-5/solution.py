import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx+=1
    m = int(input_data[idx]); idx+=1
    _k = int(input_data[idx]); idx+=1
    s = int(input_data[idx]) - 1; idx+=1
    t = int(input_data[idx]) - 1; idx+=1
    d = int(input_data[idx]); idx+=1
    
    edges = []
    for j in range(m):
        u = int(input_data[idx]) - 1; idx+=1
        v = int(input_data[idx]) - 1; idx+=1
        c = int(input_data[idx]); idx+=1
        edges.append((u, v, c))
    
    if d < 0:
        s, t = t, s
        d = -d
    
    if s == t:
        if d == 0:
            print("YES")
            print(' '.join(['0'] * m))
        else:
            print("NO")
        return
    
    # Build Dinic
    N = n + 2
    S = n
    T = n + 1
    graph = [[] for _ in range(N)]
    # edge storage: arrays cap, to; graph[v] = list of edge ids
    to = []
    cap = []
    
    def add_edge(u, v, c):
        graph[u].append(len(to))
        to.append(v)
        cap.append(c)
        graph[v].append(len(to))
        to.append(u)
        cap.append(0)
    
    edge_ids = []
    for (u, v, c) in edges:
        if u == v:
            # self loop: skip, x_j = 0
            edge_ids.append(-1)
            continue
        if c < 0:
            # empty domain -> infeasible
            print("NO")
            return
        add_edge(u, v, c)
        edge_ids.append(len(to) - 2)
    
    add_edge(S, s, d)
    add_edge(t, T, d)
    
    # Dinic
    ...