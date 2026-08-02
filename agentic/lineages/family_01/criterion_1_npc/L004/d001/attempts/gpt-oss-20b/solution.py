import sys

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj_mask = [0] * n  # bitmask of neighbors for each vertex
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u

    colors = [0] * n
    color_masks = [0, 0, 0, 0]  # index 1..3

    sys.setrecursionlimit(10000)

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        mask_adj = adj_mask[idx]
        for c in (1, 2, 3):
            if mask_adj & color_masks[c] == 0:
                colors[idx] = c
                color_masks[c] |= 1 << idx
                if dfs(idx + 1):
                    return True
                color_masks[c] ^= 1 << idx
                colors[idx] = 0
        return False

    if dfs(0):
        out_lines = ["YES", " ".join(map(str, colors))]
    else:
        out_lines = ["NO"]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()