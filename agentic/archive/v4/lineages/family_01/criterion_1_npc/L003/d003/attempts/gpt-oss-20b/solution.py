#!/usr/bin/env python3
import sys
sys.setrecursionlimit(1000000)

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
        mask_u = 1 << (v - 1)
        mask_v = 1 << (u - 1)
        neighbor_mask[u] |= mask_u
        neighbor_mask[v] |= mask_v

    colors = [0] * (n + 1)
    color_mask = [0, 0, 0, 0]  # index 1..3

    def dfs(i: int) -> bool:
        if i > n:
            return True
        neigh = neighbor_mask[i]
        for c in (1, 2, 3):
            if neigh & color_mask[c]:
                continue
            colors[i] = c
            color_mask[c] |= 1 << (i - 1)
            if dfs(i + 1):
                return True
            color_mask[c] ^= 1 << (i - 1)
            colors[i] = 0
        return False

    if dfs(1):
        out = ['YES', '\n', ' '.join(str(colors[i]) for i in range(1, n + 1))]
        sys.stdout.write(''.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()