import sys, random, time

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    # quick check with identity permutation
    perm = list(range(n))
    total = 0
    for u, v in edges:
        total += abs(perm[u] - perm[v])
    if total <= B:
        print("YES")
        print(' '.join(str(p + 1) for p in perm))
        return

    # try random permutations within time limit
    start = time.time()
    limit = 4.5  # seconds, leave margin
    best_perm = None
    best_total = None

    while time.time() - start < limit:
        perm = list(range(n))
        random.shuffle(perm)
        pos = [0] * n
        for idx, node in enumerate(perm):
            pos[node] = idx
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
            if total > B:
                break
        if total <= B:
            print("YES")
            print(' '.join(str(p + 1) for p in perm))
            return
        # keep best for possible fallback (not required by problem)
        if best_total is None or total < best_total:
            best_total = total
            best_perm = perm[:]

    # if not found
    print("NO")

if __name__ == "__main__":
    solve()