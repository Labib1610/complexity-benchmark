import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    # adjacency
    adj = [[] for _ in range(q)]
    for _ in range(t):
        a = int(input_data[idx]) - 1; idx += 1
        b = int(input_data[idx]) - 1 - q; idx += 1
        adj[a].append(b)
    
    # match_left[u] = right node matched to left u, or -1
    # match_right[v] = left node matched to right v, or -1
    match_left = [-1] * q
    match_right = [-1] * q
    
    INF = float('inf')
    
    matched = 0
    # Greedy initial matching
    for u in range(q):
        for v in adj[u]:
            if match_right[v] == -1:
                match_left[u] = v
                match_right[v] = u
                matched += 1
                break
    
    # Hopcroft-Karp
    dist = [0] * q
    # BFS from free left nodes
    ...