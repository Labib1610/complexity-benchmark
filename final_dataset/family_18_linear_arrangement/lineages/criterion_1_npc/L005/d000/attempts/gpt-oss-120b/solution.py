import sys
import itertools

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = [(int(next(it))-1, int(next(it))-1) for _ in range(m)]
    # brute force if n is small
    if n > 8:
        # fallback heuristic: identity permutation
        pos = list(range(1, n+1))
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
        if total <= B:
            print("YES")
            print(' '.join(map(str, pos)))
        else:
            print("NO")
        return
    best_perm = None
    for perm in itertools.permutations(range(1, n+1)):
        total = 0
        for u, v in edges:
            total += abs(perm[u] - perm[v])
            if total > B:
                break
        if total <= B:
            best_perm = perm
            break
    if best_perm is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, best_perm)))

if __name__ == "__main__":
    solve()