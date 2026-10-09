import sys

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

    # possible colors bitmask: bits 0,1,2 correspond to colors 1,2,3
    possible = [0b111] * n
    assign = [0] * n  # 0 = unassigned, else 1..3

    # order vertices by degree for initial heuristic
    order = sorted(range(n), key=lambda x: -len(adj[x]))

    # helper to pick next vertex: MRV among unassigned
    def select_vertex():
        best = -1
        best_cnt = 4
        for v in order:
            if assign[v] == 0:
                cnt = possible[v].bit_count()
                if cnt < best_cnt:
                    best_cnt = cnt
                    best = v
                    if cnt == 1:
                        break
        return best

    sys.setrecursionlimit(10000)

    def dfs(remaining: int) -> bool:
        if remaining == 0:
            return True
        v = select_vertex()
        mask = possible[v]
        # try each possible color
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if mask & bit == 0:
                continue
            # assign v = c
            assign[v] = c
            changed = []  # list of (neighbor, old_mask)
            fail = False
            for nb in adj[v]:
                if assign[nb] == 0:
                    old = possible[nb]
                    if old & bit:
                        new = old & ~bit
                        if new == 0:
                            fail = True
                            # no need to continue updating
                            break
                        possible[nb] = new
                        changed.append((nb, old))
            if not fail and dfs(remaining - 1):
                return True
            # backtrack
            for nb, old in reversed(changed):
                possible[nb] = old
            assign[v] = 0
        return False

    if dfs(n):
        out = ["YES"]
        out.append(" ".join(str(assign[i]) for i in range(n)))
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()