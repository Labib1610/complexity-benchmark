import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    neighbors = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u][v] = adj[v][u] = True
        neighbors[u].append(v)
        neighbors[v].append(u)
    
    for a in range(1, n + 1):
        neigh = sorted(neighbors[a])
        L = len(neigh)
        for i in range(L):
            b = neigh[i]
            if b <= a:
                continue
            for j in range(i + 1, L):
                c = neigh[j]
                if c <= b:
                    continue
                if adj[b][c]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()