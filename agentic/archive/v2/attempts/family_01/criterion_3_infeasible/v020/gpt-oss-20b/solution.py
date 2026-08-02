import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    adj_set = [set() for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if v not in adj_set[u]:
            adj[u].append(v)
            adj[v].append(u)
            adj_set[u].add(v)
            adj_set[v].add(u)

    for a in range(1, n + 1):
        neigh_a = sorted(adj[a])  # sorted list of neighbors of a
        for b in neigh_a:
            if b <= a:
                continue
            for c in neigh_a:
                if c <= b:
                    continue
                if c in adj_set[b]:
                    sys.stdout.write(f"{a} {b} {c}\n")
                    return

if __name__ == "__main__":
    main()