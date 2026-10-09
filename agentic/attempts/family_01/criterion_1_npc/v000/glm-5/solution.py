import sys
from sys import setrecursionlimit

def main():
    input_data = sys.stdin.buffer.read().split()
    n = int(input_data[0]); m = int(input_data[1])
    adj = [0]*n
    idx = 2
    edges = []
    for _ in range(m):
        u = int(input_data[idx])-1; v = int(input_data[idx+1])-1; idx += 2
        if u != v:
            adj[u] |= 1<<v
            adj[v] |= 1<<u
        edges.append((u,v))
    # (assume no self loops in input; handle just in case by ignoring? A self-loop makes it impossible... 
    # Problem likely has no self-loops. If u==v, then worker conflicts with itself → impossible. Let's handle: if u==v → NO. Hmm, m pairs "u v" conflicting pair — probably u≠v guaranteed. I'll treat self-loop as NO.)