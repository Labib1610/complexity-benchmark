import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    idx = 2
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
    
    best = None
    for a in range(1, n + 1):
        if best is not None and a >= best[0]:
            break
        neighbors = adj[a]
        # candidates b > a
        sorted_b = sorted(neighbors)
        for b in sorted_b:
            if b <= a:
                continue
            if best is not None and (a > best[0] or (a == best[0] and b >= best[1])):
                break
            # find c > b in both adj[a] and adj[b]
            adj_b = adj[b]
            for c in sorted_b:
                if c > b and c in adj_b:
                    candidate = (a, b, c)
                    if best is None or candidate < best:
                        best = candidate
                    break
        if best is not None and best[0] == a:
            # we found the smallest a, and smallest b for this a
            # but we need to ensure we have the smallest b overall for this a
            # since we iterate b in sorted order and break at first c, the first found is smallest b
            break
    
    if best is not None:
        sys.stdout.write(f"{best[0]} {best[1]} {best[2]}")

solve()