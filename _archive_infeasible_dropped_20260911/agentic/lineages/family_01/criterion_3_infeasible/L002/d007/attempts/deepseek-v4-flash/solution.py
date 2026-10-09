import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u][v] = True
        adj[v][u] = True

    for a in range(1, n + 1):
        neighbors = [v for v in range(a + 1, n + 1) if adj[a][v]]
        for i in range(len(neighbors)):
            b = neighbors[i]
            for j in range(i + 1, len(neighbors)):
                c = neighbors[j]
                if adj[b][c]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()