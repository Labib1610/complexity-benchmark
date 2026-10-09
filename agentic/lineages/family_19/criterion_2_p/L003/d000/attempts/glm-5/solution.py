import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx+=1
    m = int(data[idx]); idx+=1
    _ = int(data[idx]); idx+=1
    s = int(data[idx]); idx+=1
    t = int(data[idx]); idx+=1
    d = int(data[idx]); idx+=1
    
    # edges
    graph = [[] for _ in range(n+2)]  # nodes 1..n, SS = 0? Let me use SS = n+1...