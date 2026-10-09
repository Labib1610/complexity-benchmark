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
        adj[u].append(v)
        adj[v].append(u)

    # colour: -1 = unassigned, else 0,1,2
    colour = [-1] * n
    # candidate masks, 3 bits (bit 0 -> colour 0)
    cand = [0b111] * n

    # order of vertices for tie‑breaking (higher degree first)
    degree = [len(adj[i]) for i in range(n)]

    # helper: popcount of 3‑bit mask
    popcnt = lambda x: (x & 1) + ((x >> 1) & 1) + ((x >> 2) & 1)

    # select next vertex: uncoloured with smallest candidate count
    def select_vertex():
        best = -1
        best_cnt = 4  # > max possible (3)
        best_deg = -1
        for v in range(n):
            if colour[v] == -1:
                cnt = popcnt(cand[v])
                if cnt < best_cnt or (cnt == best_cnt and degree[v] > best_deg):
                    best = v
                    best_cnt = cnt
                    best_deg = degree[v]
        return best

    # recursive backtracking
    def dfs(coloured_cnt: int) -> bool:
        if coloured_cnt == n:
            return True
        v = select_vertex()
        mask = cand[v]
        # try each possible colour
        for c in range(3):
            if mask & (1 << c):
                # assign colour c to v
                colour[v] = c
                # record changes to neighbours to undo later
                changed = []
                ok = True
                for nb in adj[v]:
                    if colour[nb] == -1:
                        if cand[nb] & (1 << c):
                            new_mask = cand[nb] & ~(1 << c)
                            if new_mask == 0:
                                ok = False
                                # no need to continue removing, but we still record for undo
                            changed.append((nb, cand[nb]))
                            cand[nb] = new_mask
                if ok and dfs(coloured_cnt + 1):
                    return True
                # undo
                for nb, old in changed:
                    cand[nb] = old
                colour[v] = -1
        return False

    possible = dfs(0)

    if not possible:
        print("NO")
    else:
        print("YES")
        # convert internal 0‑based colours to 1‑based output
        out = [str(colour[i] + 1) for i in range(n)]
        print(' '.join(out))

if __name__ == "__main__":
    solve()