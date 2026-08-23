import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        if u < v:
            edges.append((u, v))
        else:
            edges.append((v, u))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
    edges.sort()
    best_a = n + 1
    best_b = n + 1
    best_c = n + 1
    for a, b in edges:
        if a > best_a:
            break
        if a == best_a and b >= best_b:
            continue
        mask = adj[a] & adj[b]
        if b < n:
            mask &= ~((1 << b) - 1)
        else:
            mask = 0
        if mask:
            c = (mask & -mask).bit_length()
            if a < best_a or (a == best_a and (b < best_b or (b == best_b and c < best_c))):
                best_a, best_b, best_c = a, b, c
    sys.stdout.write(f"{best_a} {best_b} {best_c}")

if __name__ == "__main__":
    solve()