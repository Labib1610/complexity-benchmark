import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx+=1
    m = int(input_data[idx]); idx+=1
    s = int(input_data[idx]); idx+=1
    t = int(input_data[idx]); idx+=1
    B = int(input_data[idx]); idx+=1
    
    # edges list
    edges = []  # (u, v, w)
    # Dinic structures
    # graph as adjacency list of edge indices; edges stored in arrays: to[], cap[]
    graph = [[] for _ in range(n+1)]
    to = []
    cap = []
    
    def add_edge(u, v, w):
        graph[u].append(len(to)); to.append(v); cap.append(w)
        graph[v].append(len(to)); to.append(u); cap.append(0)
    
    for _ in range(m):
        u = int(input_data[idx]); idx+=1
        v = int(input_data[idx]); idx+=1
        w = int(input_data[idx]); idx+=1
        edges.append((u, v, w))
        if u == v:
            continue  # self-loop, irrelevant
        # undirected edge: two directed arcs each with capacity w
        # Represent as: arc u->v cap w with reverse arc v->u cap w? 
        # For undirected edge, standard: add_edge(u,v,w) where reverse cap is also w.
        graph[u].append(len(to)); to.append(v); cap.append(w)
        graph[v].append(len(to)); to.append(u); cap.append(w)
    
    if s == t:
        print("NO")
        return
    
    # Dinic's
    ...