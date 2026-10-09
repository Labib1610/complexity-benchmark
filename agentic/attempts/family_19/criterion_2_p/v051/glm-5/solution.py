import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx+=1
    m = int(input_data[idx]); idx+=1
    _ = int(input_data[idx]); idx+=1
    s = int(input_data[idx]); idx+=1
    t = int(input_data[idx]); idx+=1
    d = int(input_data[idx]); idx+=1
    
    # edges
    N = n + 2  # nodes 1..n, super sink = n+1
    graph = [[] for _ in range(N+1)]
    to = []
    cap = []
    
    edge_flows = []  # to record flows of original edges
    
    def add_edge(u, v, c):
        graph[u].append(len(to))
        to.append(v)
        cap.append(c)
        graph[v].append(len(to))
        to.append(u)
        cap.append(0)
    
    orig_edges = []
    for i in range(m):
        u = int(input_data[idx]); idx+=1
        v = int(input_data[idx]); idx+=1
        c = int(input_data[idx]); idx+=1
        orig_edges.append((u, v, c))
        add_edge(u, v, c)
    
    T = n + 1
    add_edge(t, T, d)
    
    # Dinic from s to T
    ...