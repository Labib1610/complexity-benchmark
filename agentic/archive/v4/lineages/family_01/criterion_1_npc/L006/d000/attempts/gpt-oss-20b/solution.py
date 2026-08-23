import sys
sys.setrecursionlimit(1000000)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neigh = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        neigh[u] |= 1 << v
        neigh[v] |= 1 << u

    colors = [0] * n
    color_mask = [0, 0, 0, 0]  # 1-indexed

    def dfs(idx):
        if idx == n:
            return True
        for c in (1, 2, 3):
            if neigh[idx] & color_mask[c]:
                continue
            color_mask[c] |= 1 << idx
            colors[idx] = c
            if dfs(idx + 1):
                return True
            color_mask[c] ^= 1 << idx
        return False

    if dfs(0):
        out = ["YES", " ".join(str(colors[i]) for i in range(n))]
    else:
        out = ["NO"]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()