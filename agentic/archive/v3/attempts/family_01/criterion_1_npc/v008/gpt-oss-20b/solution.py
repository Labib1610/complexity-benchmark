import sys
sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    colors = [0] * n
    color_masks = [0, 0, 0, 0]  # 1-indexed for colors 1..3

    found = False

    def dfs(i: int) -> bool:
        nonlocal found
        if i == n:
            found = True
            return True
        for c in (1, 2, 3):
            if (adj[i] & color_masks[c]) == 0:
                colors[i] = c
                color_masks[c] ^= 1 << i
                if dfs(i + 1):
                    return True
                color_masks[c] ^= 1 << i
                colors[i] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(map(str, colors))]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()