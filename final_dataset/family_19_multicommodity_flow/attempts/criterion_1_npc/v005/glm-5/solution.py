import sys
from sys import setrecursionlimit

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx+=1
    m = int(data[idx]); idx+=1
    k = int(data[idx]); idx+=1
    comms = []
    for _ in range(k):
        s = int(data[idx])-1; t = int(data[idx+1])-1; d = int(data[idx+2]); idx+=3
        comms.append((s,t,d))
    edges = []
    for _ in range(m):
        u = int(data[idx])-1; v = int(data[idx+1])-1; c = int(data[idx+2]); idx+=3
        edges.append((u,v,c))