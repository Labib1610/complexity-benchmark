import sys
sys.setrecursionlimit(10000)

def solve() -> None:
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

    color = [0] * n          # 0 = unassigned, else 1..3
    avail = [7] * n          # bitmask of available colors (bits 0,1,2)
    color_mask = [0, 0, 0]  # nodes colored with color 1,2,3

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        node = pos
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (avail[node] & bit):
                continue
            # conflict check with already colored neighbors
            if neigh[node] & color_mask[c - 1]:
                continue
            # assign
            color[node] = c
            color_mask[c - 1] |= 1 << node
            modified = []
            conflict = False
            nb = neigh[node]
            j = 0
            while nb:
                if nb & 1:
                    if not color[j]:
                        prev = avail[j]
                        new = prev & ~bit
                        if new != prev:
                            avail[j] = new
                            modified.append((j, prev))
                        if not new:
                            conflict = True
                            break
                nb >>= 1
                j += 1
            if not conflict and dfs(pos + 1):
                return True
            # revert modifications
            for j, prev in modified:
                avail[j] = prev
            color[node] = 0
            color_mask[c - 1] &= ~(1 << node)
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()