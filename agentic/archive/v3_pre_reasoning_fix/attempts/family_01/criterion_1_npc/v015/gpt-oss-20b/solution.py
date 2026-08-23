import sys
sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_mask = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u

    colors = [0] * n
    color_masks = [0, 0, 0, 0]  # 1-indexed colors
    found = False

    def dfs(idx: int):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        mask = adj_mask[idx]
        for c in (1, 2, 3):
            if mask & color_masks[c] == 0:
                colors[idx] = c
                color_masks[c] |= 1 << idx
                dfs(idx + 1)
                if found:
                    return
                color_masks[c] ^= 1 << idx
                colors[idx] = 0

    dfs(0)
    out = sys.stdout
    if not found:
        out.write("NO\n")
    else:
        out.write("YES\n")
        out.write(' '.join(str(c) for c in colors))
        out.write('\n')

if __name__ == "__main__":
    solve()