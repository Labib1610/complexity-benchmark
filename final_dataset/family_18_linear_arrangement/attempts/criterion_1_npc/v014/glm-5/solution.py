import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1]); B = int(data[2])
    edges = []
    idx = 3
    adj = [0]*n
    deg = [0]*n
    for _ in range(m):
        u = int(data[idx])-1; v = int(data[idx+1])-1; idx += 2
        if u != v:
            edges.append((u,v))
            adj[u] |= 1<<v
            adj[v] |= 1<<u
            deg[u]+=1; deg[v]+=1
    # solve
    ...