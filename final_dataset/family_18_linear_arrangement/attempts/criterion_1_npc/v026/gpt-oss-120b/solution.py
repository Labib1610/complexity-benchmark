import sys, itertools

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    # quick check for small n using full search
    if n <= 10:
        perm = list(range(n))
        for p in itertools.permutations(perm):
            pos = [0] * n
            for idx, v in enumerate(p):
                pos[v] = idx + 1          # sectors are 1‑based
            total = 0
            for u, v in edges:
                total += abs(pos[u] - pos[v])
                if total > B:
                    break
            if total <= B:
                print("YES")
                print(' '.join(str(pos[i]) for i in range(n)))
                return
        print("NO")
        return

    # heuristic for larger n: try identity and its reverse
    def check(order):
        pos = [0] * n
        for idx, v in enumerate(order):
            pos[v] = idx + 1
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
            if total > B:
                return None
        return pos

    identity = list(range(n))
    rev = identity[::-1]

    for order in (identity, rev):
        res = check(order)
        if res is not None:
            print("YES")
            print(' '.join(str(res[i]) for i in range(n)))
            return

    # simple greedy: place vertices by degree descending
    deg = [0] * n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    order = [v for _, v in sorted((-deg[i], i) for i in range(n))]
    res = check(order)
    if res is not None:
        print("YES")
        print(' '.join(str(res[i]) for i in range(n)))
        return

    print("NO")

if __name__ == "__main__":
    solve()