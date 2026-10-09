import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = [(int(next(it)), int(next(it))) for _ in range(m)]

    # simple assignment: identity permutation
    perm = list(range(1, n + 1))
    total = 0
    for u, v in edges:
        total += abs(perm[u - 1] - perm[v - 1])
        if total > B:  # early exit
            break

    if total <= B:
        print("YES")
        print(' '.join(map(str, perm)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()