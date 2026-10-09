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
    by_elem = [[] for _ in range(n + 1)]
    for idx in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        triples.append((a, b, c))
        by_elem[a].append(idx)
        by_elem[b].append(idx)
        by_elem[c].append(idx)

    used = [False] * (n + 1)
    solution = []

    # list of uncovered elements for fast iteration
    uncovered = set(range(1, n + 1))

    def choose_sector():
        """return uncovered sector with minimal number of usable triples"""
        best = None
        best_cnt = None
        for x in uncovered:
            cnt = 0
            for idx in by_elem[x]:
                a, b, c = triples[idx]
                if not (used[a] or used[b] or used[c]):
                    cnt += 1
            if cnt == 0:
                # dead end, prune immediately
                return x, 0
            if best_cnt is None or cnt < best_cnt:
                best_cnt = cnt
                best = x
                if cnt == 1:
                    break
        return best, best_cnt

    def dfs() -> bool:
        if not uncovered:
            return True
        x, cnt = choose_sector()
        if cnt == 0:
            return False
        for idx in by_elem[x]:
            a, b, c = triples[idx]
            if used[a] or used[b] or used[c]:
                continue
            # choose this triple
            used[a] = used[b] = used[c] = True
            uncovered.discard(a); uncovered.discard(b); uncovered.discard(c)
            solution.append(idx)
            if dfs():
                return True
            # backtrack
            solution.pop()
            used[a] = used[b] = used[c] = False
            uncovered.add(a); uncovered.add(b); uncovered.add(c)
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