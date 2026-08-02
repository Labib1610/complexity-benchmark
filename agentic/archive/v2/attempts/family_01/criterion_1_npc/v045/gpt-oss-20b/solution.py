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
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    assignment = [0] * n          # color 1..3
    color_mask = [0] * 4          # bitmask of nodes assigned each color

    sys.setrecursionlimit(1000000)
    found = False

    def dfs(idx: int) -> bool:
        nonlocal found
        if idx == n:
            return True
        # try colors 1..3
        for c in (1, 2, 3):
            if (adj[idx] & color_mask[c]) == 0:
                assignment[idx] = c
                color_mask[c] |= 1 << idx
                if dfs(idx + 1):
                    return True
                color_mask[c] &= ~(1 << idx)
                assignment[idx] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(c) for c in assignment))
    else:
        print("NO")

if __name__ == "__main__":
    solve()