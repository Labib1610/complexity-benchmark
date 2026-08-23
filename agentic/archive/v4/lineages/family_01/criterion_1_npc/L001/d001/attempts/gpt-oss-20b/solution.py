import sys
sys.setrecursionlimit(1000000)

def main():
    data = sys.stdin.read().strip().split()
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

    color = [0] * n
    color_mask = [0] * 4  # indices 1..3

    def dfs(idx):
        if idx == n:
            return True
        i = idx
        for c in (1, 2, 3):
            if (adj_mask[i] & color_mask[c]) == 0:
                color[i] = c
                color_mask[c] |= 1 << i
                if dfs(idx + 1):
                    return True
                color_mask[c] ^= 1 << i
                color[i] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(c) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    main()