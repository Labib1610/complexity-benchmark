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

    # If n is small, try all permutations
    if n <= 8:
        positions = list(range(1, n + 1))
        for perm in itertools.permutations(positions):
            # perm[i] is position of module i (0‑based)
            total = 0
            for u, v in edges:
                total += abs(perm[u] - perm[v])
                if total > B:
                    break
            if total <= B:
                print("YES")
                print(' '.join(map(str, perm)))
                return
        print("NO")
        return

    # For larger n, use a simple greedy heuristic:
    # place nodes with highest degree near the centre.
    deg = [0] * n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    order = sorted(range(n), key=lambda x: -deg[x])
    # assign positions from centre outwards
    pos = [0] * n
    left = (n + 1) // 2
    right = left + 1
    for idx, node in enumerate(order):
        if idx % 2 == 0:
            pos[node] = left
            left -= 1
        else:
            pos[node] = right
            right += 1
    total = sum(abs(pos[u] - pos[v]) for u, v in edges)
    if total <= B:
        print("YES")
        print(' '.join(map(str, pos)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()