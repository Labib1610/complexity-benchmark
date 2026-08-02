import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    neighbors = [[] for _ in range(n + 1)]
    adj = [bytearray(n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        neighbors[u].append(v)
        neighbors[v].append(u)
        adj[u][v] = 1
        adj[v][u] = 1
    for a in range(1, n + 1):
        neigh_a = neighbors[a]
        if len(neigh_a) < 2:
            continue
        neigh_a.sort()
        l = len(neigh_a)
        for i in range(l):
            b = neigh_a[i]
            if b <= a:
                continue
            for j in range(i + 1, l):
                c = neigh_a[j]
                if c <= b:
                    continue
                if adj[b][c]:
                    sys.stdout.write(f"{a} {b} {c}\n")
                    return

if __name__ == "__main__":
    main()