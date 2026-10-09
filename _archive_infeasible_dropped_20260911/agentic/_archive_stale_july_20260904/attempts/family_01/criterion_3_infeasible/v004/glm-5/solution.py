import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    edge_set = set()
    
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        if u > v:
            u, v = v, u
        adj[u].append(v)
        adj[v].append(u)
        edge_set.add(u * 2001 + v)
    
    for a in range(1, n + 1):
        neighbors = adj[a]
        neighbors.sort()
        L = len(neighbors)
        for i in range(L):
            b = neighbors[i]
            if b < a:
                continue
            for j in range(i + 1, L):
                c = neighbors[j]
                if c < b:
                    continue
                # Check if b-c is an edge
                x, y = (b, c) if b < c else (c, b)
                if x * 2001 + y in edge_set:
                    print(a, b, c)
                    return

main()