import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u][v] = True
        adj[v][u] = True

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if adj[i][j]:
                for k in range(j + 1, n + 1):
                    if adj[i][k] and adj[j][k]:
                        print(i, j, k)
                        return

if __name__ == "__main__":
    main()