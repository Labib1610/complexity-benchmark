import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx+=1
    m = int(data[idx]); idx+=1
    s_label = int(data[idx]); idx+=1
    t_label = int(data[idx]); idx+=1
    limit = int(data[idx]); idx+=1
    
    edges = []
    # label compression
    label_to_id = {}
    def get_id(label):
        if label in label_to_id:
            return label_to_id[label]
        else:
            new_id = len(label_to_id)
            label_to_id[label] = new_id
            return new_id
    
    s = get_id(s_label)
    t = get_id(t_label)
    
    for _ in range(m):
        u = int(data[idx]); idx+=1
        v = int(data[idx]); idx+=1
        w = int(data[idx]); idx+=1
        edges.append((get_id(u), get_id(v), w, u, v))  # store original labels too
    
    V = len(label_to_id)
    
    if s == t:
        # same vault: impossible to isolate (a vault communicates with itself)
        print("NO")
        return
    
    # Check if s and t connected at all (ignoring zero-cost edges? no, all edges count)
    # Actually just run max flow.
    
    # Dinic
    # graph as adjacency lists with edge arrays: to, cap, and reverse index
    graph = [[] for _ in range(V)]
    
    def add_edge(u, v, cap):
        graph[u].append([v, cap, len(graph[v])])
        graph[v].append([u, 0, len(graph[u]) - 1])
    
    # For undirected edge: add u->v with cap w and v->u with cap w.
    # Standard trick: add_edge(u, v, w) then also set reverse cap to w.
    # Actually for undirected: add edge u->v cap w with reverse cap w.
    
    for (u, v, w, _, _) in edges:
        if u == v:
            continue  # self-loop, irrelevant for connectivity
        # undirected edge
        graph[u].append([v, w, len(graph[v])])
        graph[v].append([u, w, len(graph[u]) - 1])
    
    # Dinic's algorithm
    ...