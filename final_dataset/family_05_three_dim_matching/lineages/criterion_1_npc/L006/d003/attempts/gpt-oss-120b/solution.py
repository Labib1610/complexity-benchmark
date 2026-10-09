import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples_by_base = [[] for _ in range(k)]          # 0‑based
    for _ in range(t):
        m = int(next(it)) - 1
        c = int(next(it)) - 1
        f = int(next(it)) - 1
        triples_by_base[m].append((m, c, f))

    answer = []
    full_mask = (1 << k) - 1

    # depth‑first search
    def dfs(usedM: int, usedC: int, usedF: int) -> bool:
        if usedM == full_mask:          # all bases are used
            return True

        # pick first free base
        b = (usedM ^ full_mask).bit_length() - 1   # index of highest zero bit
        # iterate over its triples
        for (bm, rc, ft) in triples_by_base[b]:
            if (usedC >> rc) & 1:      # reagent already used
                continue
            if (usedF >> ft) & 1:      # temperature already used
                continue
            # choose this triple
            answer.append((bm, rc, ft))
            if dfs(usedM | (1 << bm), usedC | (1 << rc), usedF | (1 << ft)):
                return True
            answer.pop()
        return False

    possible = dfs(0, 0, 0)

    out_lines = []
    if possible:
        out_lines.append("YES")
        for (m, c, f) in answer:
            out_lines.append(f"{m+1} {c+1} {f+1}")
    else:
        out_lines.append("NO")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()