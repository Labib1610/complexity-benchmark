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

    for a in range(1, n - 1):
        neigh_a = [v for v in adj[a] if v > a]
        if len(neigh_a) < 2:
            continue
        neigh_a.sort()
        la = len(neigh_a)
        for i in range(la - 1):
            b = neigh_a[i]
            # Only need to check c > b
            for j in range(i + 1, la):
                c = neigh_a[j]
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()