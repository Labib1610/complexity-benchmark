import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    us = [0]*m
    vs = [0]*m
    deg = [0]*(n+1)
    selfloop = False
    for i in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        us[i] = u; vs[i] = v
        if u == v:
            selfloop = True
        deg[u] += 1
        deg[v] += 1
    if selfloop:
        print("NO")
        return
    # CSR
    start = [0]*(n+2)
    for i in range(1, n+1):
        start[i+1] = start[i] + deg[i]
    # start[i] .. start[i+1]-1 holds neighbors of i? Let's define adj_start array of size n+2 where positions for vertex i are [start[i], start[i+1]).
    adj = [0]*(2*m)
    pos = start[:]  # copy, pos[i] = next insertion index for vertex i... wait start has size n+2.