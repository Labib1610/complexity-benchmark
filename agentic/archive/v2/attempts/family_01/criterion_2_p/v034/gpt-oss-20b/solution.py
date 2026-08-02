import sys

# ------------------------------------------------------------
# Disjoint Set Union with parity (distance modulo 2)
# ------------------------------------------------------------
class DSU:
    __slots__ = ('parent', 'parity', 'root_color')

    def __init__(self, n: int):
        # 1‑based indexing
        self.parent = list(range(n + 1))
        self.parity = [0] * (n + 1)          # parity to parent
        self.root_color = [None] * (n + 1)   # colour of DSU root

    # recursive find with path compression
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            p = self.parent[x]
            r = self.find(p)
            self.parity[x] ^= self.parity[p]
            self.parent[x] = r
        return self.parent[x]

    # try to merge u and v (they must be in different lots)
    def union(self, u: int, v: int) -> bool:
        ru = self.find(u)
        rv = self.find(v)
        if ru == rv:
            # same component: parity must be 1
            return (self.parity[u] ^ self.parity[v]) == 1

        # parity of the old root ru to the new root rv
        parity_ru_to_rv = self.parity[u] ^ self.parity[v] ^ 1

        # attach old root ru under rv
        self.parent[ru] = rv
        self.parity[ru] = parity_ru_to_rv

        # merge root colours
        color_ru = self.root_color[ru]
        color_rv = self.root_color[rv]

        if color_ru is not None:
            # component colour of rv changes accordingly
            self.root_color[rv] = color_ru ^ parity_ru_to_rv
            # old colour is now irrelevant
            self.root_color[ru] = None
        elif color_rv is not None:
            # rv already fixed, nothing changes
            pass
        # otherwise both are None → nothing to do

        return True


# ------------------------------------------------------------
# Main solving routine
# ------------------------------------------------------------
def solve() -> None:
    sys.setrecursionlimit(1_000_000)

    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]

    dsu = DSU(n)
    idx = 2
    for _ in range(m):
        u, v = data[idx], data[idx + 1]
        idx += 2
        if not dsu.union(u, v):
            print("NO")
            return

    # assignment of lots: 0 -> lot 1, 1 -> lot 2
    lot = [0] * (n + 1)

    for v in range(1, n + 1):
        r = dsu.find(v)
        p = dsu.parity[v]

        # try lot 0 first (lot 1)
        desired_root = p ^ 0
        current_root = dsu.root_color[r]
        if current_root is None:
            dsu.root_color[r] = desired_root
            lot[v] = 0
            continue
        if current_root == desired_root:
            lot[v] = 0
            continue

        # try lot 1
        desired_root = p ^ 1
        if current_root is None:
            dsu.root_color[r] = desired_root
            lot[v] = 1
            continue
        if current_root == desired_root:
            lot[v] = 1
            continue

        # neither lot possible
        print("NO")
        return

    # print result
    print("YES")
    print(' '.join(str(l) for l in lot[1:]))


# ------------------------------------------------------------
if __name__ == "__main__":
    solve()