import sys

def main():
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
    color_mask = [0, 0, 0, 0]  # 1-indexed
    sys.setrecursionlimit(1000000)
    found = False

    def dfs(pos):
        nonlocal found
        if found:
            return
        if pos == n:
            found = True
            return
        v = pos
        for c in (1, 2, 3):
            if adj[v] & color_mask[c]:
                continue
            colors[v] = c
            color_mask[c] |= 1 << v
            dfs(pos + 1)
            if found:
                return
            color_mask[c] &= ~(1 << v)
            colors[v] = 0

    dfs(0)

    out = sys.stdout
    if not found:
        out.write("NO\n")
    else:
        out.write("YES\n")
        out.write(' '.join(str(c) for c in colors))
        out.write('\n')

if __name__ == "__main__":
    main()