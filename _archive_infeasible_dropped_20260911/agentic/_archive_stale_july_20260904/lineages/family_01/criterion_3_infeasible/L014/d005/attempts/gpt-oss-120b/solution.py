import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    masks = [0] * (n + 1)          # 1‑based
    edges = []                     # list of (u,v) with u<v

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        masks[u] |= 1 << (v - 1)
        masks[v] |= 1 << (u - 1)
        edges.append((u, v))

    # sort edges to guarantee lexicographic order of (a,b)
    edges.sort()

    for a, b in edges:
        # common neighbours of a and b
        common = masks[a] & masks[b]
        # discard vertices <= b
        common >>= b
        if common:
            # least significant set bit
            lsb = (common & -common).bit_length() - 1
            c = b + 1 + lsb
            sys.stdout.write(f"{a} {b} {c}\n")
            return

if __name__ == "__main__":
    solve()