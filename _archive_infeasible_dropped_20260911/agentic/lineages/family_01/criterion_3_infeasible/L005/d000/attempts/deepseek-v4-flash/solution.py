import sys

def solve():
    data = sys.stdin.buffer.read().split()
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
        # sorted neighbors of a that are > a
        neigh_a = sorted(x for x in adj[a] if x > a)
        for b in range(a + 1, n + 1):
            if b not in adj[a]:
                continue
            # find smallest c > b that is neighbor of both a and b
            for c in neigh_a:
                if c > b and c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()