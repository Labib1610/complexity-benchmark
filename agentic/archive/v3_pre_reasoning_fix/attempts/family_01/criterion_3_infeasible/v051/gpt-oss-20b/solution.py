import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [bytearray(n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = 1
        adj[v][u] = 1

    for a in range(1, n + 1):
        # neighbors of a with index > a
        neigh = [v for v in range(a + 1, n + 1) if adj[a][v]]
        sz = len(neigh)
        for i in range(sz):
            b = neigh[i]
            for j in range(i + 1, sz):
                c = neigh[j]
                if adj[b][c]:
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    main()