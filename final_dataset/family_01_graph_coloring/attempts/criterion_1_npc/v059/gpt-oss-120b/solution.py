import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u].append(v)
        adj[v].append(u)

    # masks: bit 0 -> colour 1, bit1 -> colour2, bit2 -> colour3
    ALL = 0b111
    mask = [ALL] * n
    color = [0] * n          # 0 = uncoloured, else 1..3

    # order for tie‑breaking (higher degree first)
    degree = [len(adj[i]) for i in range(n)]

    # ---------- helper functions ----------
    def popcnt(x: int) -> int:
        return (x & 1) + ((x >> 1) & 1) + ((x >> 2) & 1)

    # choose uncoloured vertex with smallest domain (MRV)
    def select_vertex() -> int:
        best = -1
        best_cnt = 4          # larger than any possible domain size
        best_deg = -1
        for v in range(n):
            if color[v] != 0:
                continue
            cnt = popcnt(mask[v])
            if cnt < best_cnt or (cnt == best_cnt and degree[v] > best_deg):
                best = v
                best_cnt = cnt
                best_deg = degree[v]
        return best

    # recursive backtracking
    def dfs() -> bool:
        # all coloured?
        if all(c != 0 for c in color):
            return True

        v = select_vertex()
        possible = mask[v]
        # try colours in any order
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (possible & bit):
                continue

            # assign colour c to v
            color[v] = c
            changed = []          # list of (u, old_mask)

            conflict = False
            for u in adj[v]:
                if color[u] == 0:
                    old = mask[u]
                    new = old & ~bit
                    if new != old:
                        mask[u] = new
                        changed.append((u, old))
                        if new == 0:
                            conflict = True
                            break
                elif color[u] == c:
                    conflict = True
                    break

            if not conflict:
                if dfs():
                    return True

            # undo changes
            for u, old in reversed(changed):
                mask[u] = old
            color[v] = 0

        return False

    # trivial case: no edges
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return

    if dfs():
        print("YES")
        print(" ".join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()