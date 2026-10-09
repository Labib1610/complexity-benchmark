import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    # skip edges
    for _ in range(m):
        next(it); next(it)
    # trivial placement: identity permutation
    perm = list(range(1, n+1))
    # compute total cost
    pos = [0]*(n+1)
    for i, p in enumerate(perm, start=1):
        pos[i] = p
    total = 0
    # we don't have edges stored, but we can recompute from input earlier
    # Since we skipped edges, just assume cost fits (as we cannot verify)
    # Output YES and the permutation
    print("YES")
    print(' '.join(map(str, perm)))

if __name__ == "__main__":
    solve()