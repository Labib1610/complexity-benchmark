import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    color = [0] * n          # 0 = unassigned, 1/2/3 = shift
    color_mask = [0, 0, 0, 0]  # index by color

    sys.setrecursionlimit(10000)

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        neighbors = adj_mask[idx]
        for c in (1, 2, 3):
            if neighbors & color_mask[c]:
                continue
            color[idx] = c
            color_mask[c] |= 1 << idx
            if dfs(idx + 1):
                return True
            color_mask[c] ^= 1 << idx
            color[idx] = 0
        return False

    if dfs(0):
        out_lines = ["YES", " ".join(str(color[i]) for i in range(n))]
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()