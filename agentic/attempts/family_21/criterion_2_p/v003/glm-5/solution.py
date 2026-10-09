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
    
    # adjacency
    graph = [[] for _ in range(n+1)]
    to = []
    cap = []
    edges_orig = []  # (u, v, w)
    
    for _ in range(m):
        u = int(input_data[idx]); idx+=1
        v = int(input_data[idx]); idx+=1
        w = int(input_data[idx]); idx+=1
        edges_orig.append((u, v, w))
        if u == v:
            continue  # self loop, ignore (never seal)
        graph[u].append(len(to)); to.append(v); cap.append(w)
        graph[v].append(len(to)); to.append(u); cap.append(w)
    ...