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

    color_mask = [0, 0, 0, 0]  # indices 1..3
    result = [0] * n
    found = False

    def dfs(idx: int) -> bool:
        nonlocal found
        if idx == n:
            found = True
            return True
        for c in (1, 2, 3):
            if adj[idx] & color_mask[c]:
                continue
            # assign
            color_mask[c] |= 1 << idx
            result[idx] = c
            if dfs(idx + 1):
                return True
            # backtrack
            color_mask[c] ^= 1 << idx
            result[idx] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(map(str, result))]
    else:
        out = ["NO"]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()