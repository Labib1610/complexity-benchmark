import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[False]*n for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u][v] = adj[v][u] = True
    
    for a in range(n):
        non_neighbors = [i for i in range(n) if i != a and not adj[a][i]]
        if len(non_neighbors) < 2:
            continue
        # Check pairs
        for idx1 in range(len(non_neighbors)):
            b = non_neighbors[idx1]
            if b <= a:
                continue
            for idx2 in range(idx1+1, len(non_neighbors)):
                c = non_neighbors[idx2]
                if c <= b:
                    continue
                if not adj[b][c]:
                    print(a+1, b+1, c+1)
                    return

if __name__ == "__main__":
    main()