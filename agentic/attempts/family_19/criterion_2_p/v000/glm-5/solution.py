import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx+=1
    m = int(input_data[idx]); idx+=1
    _ = int(input_data[idx]); idx+=1  # number of products = 1
    s = int(input_data[idx]); idx+=1
    t = int(input_data[idx]); idx+=1
    d = int(input_data[idx]); idx+=1
    
    # nodes: 1..n, S = n+1
    S = n + 1
    N = n + 2
    graph = [[] for _ in range(N)]
    # edge storage: to, cap, rev_index; also record edge id for original edges
    edge_to = []
    edge_cap = []
    edge_rev = []
    
    def add_edge(u, v, cap):
        graph[u].append(len(edge_to))
        edge_to.append(v)
        edge_cap.append(cap)
        edge_rev.append(len(edge_to)+1)
        graph[v].append(len(edge_to))
        edge_to.append(u)
        edge_cap.append(0)
        edge_rev.append(len(edge_to)-1)
    
    orig_ids = []
    for j in range(m):
        u = int(input_data[idx]); idx+=1
        v = int(input_data[idx]); idx+=1
        cap = int(input_data[idx]); idx+=1
        add_edge(u, v, cap)
        orig_ids.append(len(edge_to) - 2)  # forward edge index
    
    add_edge(S, s, d)
    
    # Dinic from S to t
    ...