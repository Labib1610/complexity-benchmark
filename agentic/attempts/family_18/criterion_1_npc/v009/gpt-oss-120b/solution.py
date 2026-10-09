import sys
import itertools

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
    def total_dist(perm):
        pos = [0] * n
        for idx, v in enumerate(perm):
            pos[v] = idx
        s = 0
        for u, v in edges:
            s += abs(pos[u] - pos[v])
            if s > B:
                break
        return s

    # try identity first
    identity = list(range(n))
    if total_dist(identity) <= B:
        print("YES")
        print(' '.join(str(x + 1) for x in identity))
        return

    # if n is small, brute force
    if n <= 8:
        for perm in itertools.permutations(range(n)):
            if total_dist(perm) <= B:
                print("YES")
                print(' '.join(str(x + 1) for x in perm))
                return
        print("NO")
        return

    # for larger n, use a simple heuristic: sort by degree descending
    deg = [0] * n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    order = sorted(range(n), key=lambda x: -deg[x])
    if total_dist(order) <= B:
        print("YES")
        print(' '.join(str(x + 1) for x in order))
    else:
        print("NO")

if __name__ == "__main__":
    solve()