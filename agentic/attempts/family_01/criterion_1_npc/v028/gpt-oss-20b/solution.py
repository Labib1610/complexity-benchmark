import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neighbor_mask = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        mask_u = 1 << (v - 1)
        mask_v = 1 << (u - 1)
        neighbor_mask[u] |= mask_u
        neighbor_mask[v] |= mask_v

    colors = [0] * (n + 1)
    color_mask = [0, 0, 0, 0]  # index 1..3

    sys.setrecursionlimit(10000)

    def dfs(idx: int) -> bool:
        if idx > n:
            return True
        nb = neighbor_mask[idx]
        for c in (1, 2, 3):
            if nb & color_mask[c] == 0:
                colors[idx] = c
                color_mask[c] |= 1 << (idx - 1)
                if dfs(idx + 1):
                    return True
                color_mask[c] ^= 1 << (idx - 1)
                colors[idx] = 0
        return False

    if dfs(1):
        out = ["YES", " ".join(str(colors[i]) for i in range(1, n + 1))]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()