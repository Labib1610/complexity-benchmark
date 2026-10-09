import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    edges = [[] for _ in range(k)]          # edges[a] = list of (c,w)
    for _ in range(t):
        a = int(next(it)) - 1
        c = int(next(it)) - 1
        w = int(next(it)) - 1
        edges[a].append((c, w))

    usedA = usedC = usedW = 0
    answer = [None] * k                     # answer[a] = (c,w)

    # pre‑compute for speed: for each analyst, a list of its pairs as bit masks
    pair_masks = []
    for a in range(k):
        lst = []
        for c, w in edges[a]:
            lst.append((c, w, 1 << c, 1 << w))
        pair_masks.append(lst)

    # recursion
    def dfs(assigned_cnt: int) -> bool:
        nonlocal usedA, usedC, usedW
        if assigned_cnt == k:
            return True

        # choose analyst with fewest currently feasible pairs
        best_a = -1
        best_opts = None
        for a in range(k):
            if (usedA >> a) & 1:
                continue
            opts = []
            for c, w, cm, wm in pair_masks[a]:
                if (usedC & cm) or (usedW & wm):
                    continue
                opts.append((c, w, cm, wm))
            if not opts:          # dead end
                return False
            if best_a == -1 or len(opts) < len(best_opts):
                best_a = a
                best_opts = opts
                if len(best_opts) == 1:
                    break

        a = best_a
        for c, w, cm, wm in best_opts:
            # take this triple
            usedA |= 1 << a
            usedC |= cm
            usedW |= wm
            answer[a] = (c, w)

            if dfs(assigned_cnt + 1):
                return True

            # backtrack
            usedA ^= 1 << a
            usedC ^= cm
            usedW ^= wm
            answer[a] = None

        return False

    if dfs(0):
        out = ["YES"]
        for a in range(k):
            c, w = answer[a]
            out.append(f"{a+1} {c+1} {w+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()