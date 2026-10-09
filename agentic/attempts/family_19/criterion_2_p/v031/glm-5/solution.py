import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1  # = 1
    s = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1
    
    # edges
    # We'll build Dinic with nodes 1..n, plus S = 0, T = n+1.
    # Actually let me use 0-indexed: nodes 0..n-1 for junctions, S = n, T = n+1.
    
    ...