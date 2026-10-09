import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q
    triples = []
    elem_triples = [[] for _ in range(n + 1)]
    for idx in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        triples.append((a, b, c))
        elem_triples[a].append(idx)
        elem_triples[b].append(idx)
        elem_triples[c].append(idx)

    uncovered = set(range(1, n + 1))
    active = set(range(t))
    solution = []

    # heuristic cache for candidate counts
    def choose_element():
        # pick uncovered element with fewest available triples
        best = None
        best_cnt = None
        for e in uncovered:
            cnt = 0
            for r in elem_triples[e]:
                if r in active and all(v in uncovered for v in triples[r]):
                    cnt += 1
            if cnt == 0:
                return e, 0
            if best_cnt is None or cnt < best_cnt:
                best_cnt = cnt
                best = e
        return best, best_cnt

    def dfs() -> bool:
        if not uncovered:
            return True
        e, cnt = choose_element()
        if cnt == 0:
            return False
        # collect candidate triples for e
        candidates = []
        for r in elem_triples[e]:
            if r in active and all(v in uncovered for v in triples[r]):
                candidates.append(r)
        for r in candidates:
            solution.append(r)
            removed_triples = []
            covered = []
            # cover elements of r
            for v in triples[r]:
                uncovered.remove(v)
                covered.append(v)
            # remove all triples that intersect these elements
            for v in triples[r]:
                for r2 in elem_triples[v]:
                    if r2 in active:
                        active.remove(r2)
                        removed_triples.append(r2)
            if dfs():
                return True
            # backtrack
            for r2 in removed_triples:
                active.add(r2)
            for v in covered:
                uncovered.add(v)
            solution.pop()
        return False

    if dfs():
        out = ["YES"]
        for idx in solution:
            a, b, c = triples[idx]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()