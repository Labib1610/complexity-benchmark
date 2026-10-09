import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx+=1
    m = int(input_data[idx]); idx+=1
    s = int(input_data[idx]); idx+=1
    t = int(input_data[idx]); idx+=1
    limit = int(input_data[idx]); idx+=1
    
    edges = []
    for _ in range(m):
        u = int(input_data[idx]); idx+=1
        v = int(input_data[idx]); idx+=1
        w = int(input_data[idx]); idx+=1
        edges.append((u, v, w))
    
    if s == t:
        print("NO")
        return
    
    # Build Dinic
    # graph as adjacency list of edge indices
    graph = [[] for _ in range(n+1)]
    cap = []  # capacity array, edge i paired with i^1
    to = []   # target vertex of edge i
    
    for (u, v, w) in edges:
        if u == v:
            continue  # self-loops irrelevant
        graph[u].append(len(cap))
        to.append(v); cap.append(w)
        graph[v].append(len(cap))
        to.append(u); cap.append(w)
    
    # Dinic
    ...