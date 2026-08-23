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

    colorMask = [0, 0, 0]  # masks for colors 1,2,3
    color = [0] * n
    sys.setrecursionlimit(10000)

    def dfs(idx):
        if idx == n:
            return True
        for c in range(3):
            if adj[idx] & colorMask[c] == 0:
                colorMask[c] |= 1 << idx
                color[idx] = c + 1
                if dfs(idx + 1):
                    return True
                colorMask[c] &= ~(1 << idx)
        return False

    if dfs(0):
        out = ['YES', ' '.join(map(str, color))]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()