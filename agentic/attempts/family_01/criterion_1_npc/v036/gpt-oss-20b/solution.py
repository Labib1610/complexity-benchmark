import sys

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
    color_masks = [0, 0, 0]  # masks for colors 1,2,3

    sys.setrecursionlimit(1000000)

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        for c in range(3):  # colors 0,1,2 correspond to 1,2,3
            if (adj[pos] & color_masks[c]) == 0:
                colors[pos] = c + 1
                color_masks[c] |= 1 << pos

                # forward checking: ensure no uncolored vertex has all colors blocked
                ok = True
                for k in range(pos + 1, n):
                    if (adj[k] & color_masks[0]) and (adj[k] & color_masks[1]) and (adj[k] & color_masks[2]):
                        ok = False
                        break
                if ok and dfs(pos + 1):
                    return True

                color_masks[c] ^= 1 << pos
                colors[pos] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(map(str, colors))]
    else:
        out = ["NO"]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()