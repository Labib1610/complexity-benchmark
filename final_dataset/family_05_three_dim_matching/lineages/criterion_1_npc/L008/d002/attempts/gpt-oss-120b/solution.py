import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    rows_by_x = [[] for _ in range(k + 1)]          # 1‑based
    for _ in range(t):
        x = int(next(it)); y = int(next(it)); z = int(next(it))
        rows_by_x[x].append((y, z))

    full_mask = (1 << k) - 1
    solution = []

    sys.setrecursionlimit(10000)

    def search(maskX: int, maskY: int, maskZ: int) -> bool:
        if maskX == full_mask:          # all X‑planes are used
            return True

        # choose smallest uncovered X
        # (~maskX) has 1s where not used, isolate lowest set bit
        # but we need index, simple loop is fine (k ≤ 22)
        for x in range(1, k + 1):
            if not (maskX >> (x - 1)) & 1:
                break

        for y, z in rows_by_x[x]:
            bity = 1 << (y - 1)
            bitz = 1 << (z - 1)
            if (maskY & bity) or (maskZ & bitz):
                continue
            # take this triple
            solution.append((x, y, z))
            if search(maskX | (1 << (x - 1)), maskY | bity, maskZ | bitz):
                return True
            solution.pop()
        return False

    if search(0, 0, 0):
        out = ["YES"]
        out.extend(f"{x} {y} {z}" for x, y, z in solution)
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()