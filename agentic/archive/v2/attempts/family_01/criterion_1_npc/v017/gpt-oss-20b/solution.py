import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    colors = [0] * (n + 1)
    color_masks = [0, 0, 0, 0]  # index 1..3

    sys.setrecursionlimit(10000)

    def dfs(v):
        if v > n:
            return True
        mask = adj[v]
        for c in (1, 2, 3):
            if mask & color_masks[c] == 0:
                colors[v] = c
                color_masks[c] |= 1 << (v - 1)
                if dfs(v + 1):
                    return True
                color_masks[c] ^= 1 << (v - 1)
                colors[v] = 0
        return False

    if dfs(1):
        out = ['YES', '\n', ' '.join(str(colors[i]) for i in range(1, n + 1))]
        sys.stdout.write(''.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    main()