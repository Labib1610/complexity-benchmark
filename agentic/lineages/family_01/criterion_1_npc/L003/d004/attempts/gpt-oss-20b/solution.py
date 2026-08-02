import sys
sys.setrecursionlimit(10000)

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

    color_mask = [0, 0, 0, 0]  # indices 1..3
    assigned = [0] * n
    found = False

    def dfs(idx):
        nonlocal found
        if idx == n:
            found = True
            return True
        for c in (1, 2, 3):
            if adj[idx] & color_mask[c] == 0:
                color_mask[c] |= 1 << idx
                assigned[idx] = c
                # forward checking
                ok = True
                for j in range(idx + 1, n):
                    if assigned[j] == 0:
                        if (adj[j] & color_mask[1]) and (adj[j] & color_mask[2]) and (adj[j] & color_mask[3]):
                            ok = False
                            break
                if ok and dfs(idx + 1):
                    return True
                # backtrack
                color_mask[c] ^= 1 << idx
                assigned[idx] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, assigned)))
    else:
        print("NO")

if __name__ == "__main__":
    main()