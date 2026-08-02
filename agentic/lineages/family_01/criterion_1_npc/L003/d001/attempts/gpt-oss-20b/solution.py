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
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    color = [0] * n
    mask = [0, 0, 0, 0]  # mask[1], mask[2], mask[3]

    sys.setrecursionlimit(1000000)

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        v = idx
        for c in (1, 2, 3):
            if adj[v] & mask[c] == 0:
                color[v] = c
                mask[c] |= 1 << v
                if dfs(idx + 1):
                    return True
                mask[c] ^= 1 << v
                color[v] = 0
        return False

    if dfs(0):
        out_lines = ["YES", " ".join(str(color[i]) for i in range(n))]
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()