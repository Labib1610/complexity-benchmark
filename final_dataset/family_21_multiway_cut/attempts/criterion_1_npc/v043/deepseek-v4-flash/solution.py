import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))
    sources = set()
    for _ in range(k):
        sources.add(int(next(it)))
    edges = []
    for _ in range(m:
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((w, u, v))
    # sort descending by cost
    edges.sort(reverse=True)
    parent = list(range(n+1))
    size = [1]*(n+1)
    has_source = [False]*(n+1)
    for s in sources:
        has_source[s] = True
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False
        # merge, update source flag
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        has_source[ra] = has_source[ra] or has_source[rb]
        return True
    filtered = []
    total_cost = 0
    for w, u, v in edges:
        ru = find(u)
        rv = find(v)
        if ru == rv:
            # already connected, no need to keep; we can filter it
            filtered.append((u, v))
            total_cost += w
        elif has_source[ru] and has_source[rv]:
            # would merge two sources -> must filter
            filtered.append((u, v))
            total_cost += w
        else:
            # safe to keep
            union(ru, rv)
    if total_cost > B:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write(str(len(filtered)) + "\n")
        for u, v in filtered:
            sys.stdout.write(f"{u} {v}\n")

if __name__ == "__main__":
    solve()