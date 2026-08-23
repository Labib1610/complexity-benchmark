import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    neighbors = [0] * n
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        neighbors[u] |= 1 << v
        neighbors[v] |= 1 << u

    color_mask = [0, 0, 0, 0]  # indices 1..3
    assign = [0] * n
    found = False

    def dfs(idx: int) -> bool:
        nonlocal found
        if idx == n:
            found = True
            return True
        for c in (1, 2, 3):
            if neighbors[idx] & color_mask[c] == 0:
                assign[idx] = c
                color_mask[c] |= 1 << idx
                if dfs(idx + 1):
                    return True
                color_mask[c] ^= 1 << idx
                assign[idx] = 0
        return False

    if dfs(0):
        out_lines = ["YES", " ".join(map(str, assign))]
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()