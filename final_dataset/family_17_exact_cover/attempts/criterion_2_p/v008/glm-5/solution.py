import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    
    n_left = q
    n_right = q
    
    # Read edges
    # Build CSR
    deg = [0] * (n_left + 1)
    us = [0] * t
    vs = [0] * t
    for i in range(t):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        us[i] = a
        vs[i] = b - q  # right vertex index 1..q
        deg[a] += 1
    
    # CSR
    start = [0] * (n_left + 2)
    for i in range(1, n_left + 1):
        start[i+1] = start[i] + deg[i]
    # start[i] gives beginning index for vertex i... let me define start[v] = offset for v
    adj = [0] * t
    pos = start[:]  # copy... careful with indexing
    # Actually let me define: start[v] for v in 1..n_left is the start offset; start[v+1] is end.
    fill = start[1:n_left+1]  # hmm