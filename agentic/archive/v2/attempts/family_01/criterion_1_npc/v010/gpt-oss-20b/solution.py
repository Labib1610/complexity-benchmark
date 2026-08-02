import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        neighbors[u].append(v)
        neighbors[v].append(u)

    # availability mask: bit i (0-index) means color (i+1) is available
    avail_masks = [0b111] * n
    color = [0] * n  # 0 uncolored, 1..3 colored

    order = list(range(n))  # vertices in increasing index order

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = order[pos]
        if color[v] != 0:  # should not happen
            return dfs(pos + 1)
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if avail_masks[v] & bit:
                # assign
                color[v] = c
                changed = []
                conflict = False
                for u in neighbors[v]:
                    if color[u] == 0 and (avail_masks[u] & bit):
                        avail_masks[u] ^= bit
                        changed.append(u)
                        if avail_masks[u] == 0:
                            conflict = True
                            break
                if not conflict:
                    if dfs(pos + 1):
                        return True
                # backtrack
                for u in changed:
                    avail_masks[u] |= bit
                color[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()