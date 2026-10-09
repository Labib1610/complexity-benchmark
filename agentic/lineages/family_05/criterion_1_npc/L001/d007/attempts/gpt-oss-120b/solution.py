import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []
    by_a = [[] for _ in range(k + 1)]          # 1‑based
    for idx in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triples.append((a, b, c))
        if 1 <= a <= k:
            by_a[a].append(idx)

    used_a = [False] * (k + 1)
    used_b = [False] * (k + 1)
    used_c = [False] * (k + 1)
    chosen = []

    INF = 10 ** 9

    def search(depth: int) -> bool:
        if depth == k:
            return True

        # select unused a with minimal number of usable rows
        best_a = -1
        best_cnt = INF
        for a in range(1, k + 1):
            if used_a[a]:
                continue
            cnt = 0
            for idx in by_a[a]:
                _, b, c = triples[idx]
                if not used_b[b] and not used_c[c]:
                    cnt += 1
            if cnt == 0:
                return False          # dead end
            if cnt < best_cnt:
                best_cnt = cnt
                best_a = a
                if cnt == 1:          # cannot get better
                    break

        # try all rows using best_a
        for idx in by_a[best_a]:
            a, b, c = triples[idx]
            if used_b[b] or used_c[c]:
                continue
            used_a[a] = used_b[b] = used_c[c] = True
            chosen.append(idx)
            if search(depth + 1):
                return True
            chosen.pop()
            used_a[a] = used_b[b] = used_c[c] = False

        return False

    possible = search(0)

    out = []
    if possible:
        out.append("YES")
        for idx in chosen:
            a, b, c = triples[idx]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()