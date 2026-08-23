import sys, bisect

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v); adj[v].append(u)
    for a in range(1, n + 1):
        adj[a].sort()
    for a in range(1, n + 1):
        neigh_a = adj[a]
        for b in neigh_a:
            if b <= a:
                continue
            neigh_b = adj[b]
            i = bisect.bisect_left(neigh_a, b + 1)
            j = bisect.bisect_left(neigh_b, b + 1)
            while i < len(neigh_a) and j < len(neigh_b):
                va = neigh_a[i]
                vb = neigh_b[j]
                if va == vb:
                    sys.stdout.write(f"{a} {b} {va}")
                    return
                elif va < vb:
                    i += 1
                else:
                    j += 1

if __name__ == "__main__":
    solve()