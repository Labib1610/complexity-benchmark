import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    us = data[2:2+2*m:2]
    vs = data[3:2+2*m:2]
    # convert
    # Build CSR
    deg = [0]*(n+1)
    idx = 0
    U = [0]*m
    V = [0]*m
    for i in range(m):
        u = int(data[2+2*i]); v = int(data[3+2*i])
        U[i] = u; V[i] = v
        deg[u] += 1
        deg[v] += 1
    # prefix sums
    start = [0]*(n+2)
    for i in range(1, n+1):
        start[i+1] = start[i] + deg[i]
    adj = [0]*(2*m)
    pos = start[:]  # copy, pos[i] is next insertion index for vertex i
    # Actually start has n+2 entries; pos = list(start)
    for i in range(m):
        u = U[i]; v = V[i]
        adj[pos[u]] = v; pos[u] += 1
        adj[pos[v]] = u; pos[v] += 1
    color = [0]*(n+1)
    for s in range(1, n+1):
        if color[s] == 0:
            color[s] = 1
            stack = [s]
            while stack:
                x = stack.pop()
                cx = color[x]
                for j in range(start[x], start[x+1]):
                    y = adj[j]
                    if color[y] == 0:
                        color[y] = 3 - cx
                        stack.append(y)
                    elif color[y] == cx:
                        print("NO")
                        return
    out = []
    out.append("YES")
    out.append(' '.join(map(str, color[1:])))
    sys.stdout.write('\n'.join(out) + '\n')

main()