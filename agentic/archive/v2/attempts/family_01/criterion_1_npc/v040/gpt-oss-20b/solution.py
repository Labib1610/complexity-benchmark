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

    assignment = [0] * n
    color_mask = [0, 0, 0]  # bitmask of vertices assigned to each color

    def dfs(v: int) -> bool:
        if v == n:
            return True
        for c in range(3):
            if adj[v] & color_mask[c] == 0:
                color_mask[c] |= 1 << v
                assignment[v] = c + 1
                if dfs(v + 1):
                    return True
                color_mask[c] ^= 1 << v
        return False

    found = dfs(0)
    out = sys.stdout
    if found:
        out.write("YES\n")
        out.write(' '.join(map(str, assignment)))
    else:
        out.write("NO")

if __name__ == "__main__":
    solve()