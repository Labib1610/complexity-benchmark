import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)

    for a in range(1, n + 1):
        # neighbors greater than a
        neigh = [v for v in adj[a] if v > a]
        if len(neigh) < 2:
            continue
        neigh.sort()
        sz = len(neigh)
        for i in range(sz):
            b = neigh[i]
            # if we want lexicographically smallest, we need to consider smallest c after b
            for j in range(i + 1, sz):
                c = neigh[j]
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()