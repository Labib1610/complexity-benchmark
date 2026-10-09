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
    
    edges = []
    # Dinic structures
    # graph[u] = list of edge ids
    graph = [[] for _ in range(n+1)]
    to = []
    cap = []
    
    def add_arc(u, v, c):
        graph[u].append(len(to))
        to.append(v)
        cap.append(c)
        graph[v].append(len(to))
        to.append(u)
        cap.append(0)
    
    for i in range(m):
        u = int(data[idx]); v = int(data[idx+1]); w = int(data[idx+2]); idx += 3
        edges.append((u, v, w))
        if u != v and w > 0:
            add_arc(u, v, w)
            # set reverse cap to w as well: the paired arc
            cap[-1] = w
        # if w == 0: edge can't be in a useful cut... but wait, w=0 edges are free to remove!
    
    ...