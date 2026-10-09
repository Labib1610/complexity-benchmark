import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx+=1
    m = int(input_data[idx]); idx+=1
    K = int(input_data[idx]); idx+=1
    s = int(input_data[idx]); idx+=1
    t = int(input_data[idx]); idx+=1
    d = int(input_data[idx]); idx+=1
    
    # normalize to 0-indexed
    s -= 1; t -= 1
    
    # handle d
    if d < 0:
        # flow from t to s of value -d
        s, t = t, s
        d = -d
    
    if s == t:
        if d == 0:
            print("YES")
            print(' '.join(['0']*m))
        else:
            print("NO")
        return
    
    # Build Dinic
    # nodes: 0..n-1, super source = n
    N = n + 1
    S = n
    
    graph = [[] for _ in range(N)]  # each entry: list of edge ids
    # edges stored as arrays: to, cap (residual), and paired edge id
    to = []
    cap = []
    edge_index = []  # for original edges, the id of forward edge
    
    def add_edge(u, v, c):
        graph[u].append(len(to))
        to.append(v)
        cap.append(c)
        graph[v].append(len(to))
        to.append(u)
        cap.append(0)
    
    add_edge(S, s, d)
    
    for j in range(m):
        u = int(input_data[idx]); idx+=1
        v = int(input_data[idx]); idx+=1
        c = int(input_data[idx]); idx+=1
        u -= 1; v -= 1
        edge_index.append(len(to))
        add_edge(u, v, c)
    
    # Dinic from S to t
    ...