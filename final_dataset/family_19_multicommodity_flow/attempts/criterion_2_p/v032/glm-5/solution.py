import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx+=1
    m = int(input_data[idx]); idx+=1
    k = int(input_data[idx]); idx+=1
    s = int(input_data[idx]); idx+=1
    t = int(input_data[idx]); idx+=1
    d = int(input_data[idx]); idx+=1
    
    # convert to 0-indexed
    s -= 1; t -= 1
    
    if d < 0:
        s, t = t, s
        d = -d
    
    # edges
    N = n + 2
    S = n
    T = n + 1
    
    # Dinic structures
    graph = [[] for _ in range(N)]
    to = []
    cap = []
    
    def add_edge(u, v, c):
        graph[u].append(len(to))
        to.append(v)
        cap.append(c)
        graph[v].append(len(to))
        to.append(u)
        cap.append(0)
        return (len(to) - 2) // 2  # index of forward edge pair
    
    edge_ids = []
    for i in range(m):
        u = int(input_data[idx]); idx+=1
        v = int(input_data[idx]); idx+=1
        L = int(input_data[idx]); idx+=1
        u -= 1; v -= 1
        eid = add_edge(u, v, L)
        edge_ids.append(eid)
    
    add_edge(S, s, d)
    add_edge(t, T, d)
    
    # Dinic max flow from S to T
    ...