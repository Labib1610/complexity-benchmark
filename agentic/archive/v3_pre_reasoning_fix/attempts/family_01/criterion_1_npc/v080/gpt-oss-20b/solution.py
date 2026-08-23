import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neighbors = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        neighbors[u] |= 1 << v
        neighbors[v] |= 1 << u

    assigned = [0, 0, 0]  # bitmask for colors 1,2,3
    ans = [0] * n

    def dfs(v: int) -> bool:
        if v == n:
            return True
        mask_v = neighbors[v]
        for c in range(3):
            if mask_v & assigned[c]:
                continue
            assigned[c] |= 1 << v
            ans[v] = c + 1
            if dfs(v + 1):
                return True
            assigned[c] ^= 1 << v
        return False

    if dfs(0):
        print("YES")
        print(" ".join(map(str, ans)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()