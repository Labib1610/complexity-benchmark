import sys
sys.setrecursionlimit(10000)

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
    color_masks = [0, 0, 0]  # mask of nodes colored with color 1,2,3

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        mask = adj[idx]
        for c in range(3):  # colors 1..3
            if (color_masks[c] & mask) == 0:
                colors[idx] = c + 1
                color_masks[c] |= 1 << idx
                if dfs(idx + 1):
                    return True
                color_masks[c] ^= 1 << idx
        colors[idx] = 0
        return False

    if dfs(0):
        out = [str(c) for c in colors]
        sys.stdout.write("YES\n" + " ".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()