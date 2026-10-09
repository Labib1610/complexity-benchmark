import sys


def main():
    sys.setrecursionlimit(100000)
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        edges.append((u, v))

    in_cover = [False] * (n + 1)

    def first_uncovered():
        for (u, v) in edges:
            if not in_cover[u] and not in_cover[v]:
                return (u, v)
        return None

    # Bounded search tree: pick an uncovered corridor; one of its two endpoints
    # must hold a guard, so branch on including u or v. Depth is bounded by k.
    def solve(budget):
        e = first_uncovered()
        if e is None:
            return True
        if budget == 0:
            return False
        u, v = e
        lo, hi = (u, v) if u < v else (v, u)
        for w in (lo, hi):
            in_cover[w] = True
            if solve(budget - 1):
                return True
            in_cover[w] = False
        return False

    if solve(k):
        cover = [w for w in range(1, n + 1) if in_cover[w]]
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, cover)) + "\n")
    else:
        sys.stdout.write("NO\n")


main()
