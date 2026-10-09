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
    edges = []
    deg = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        edges.append((u, v))
        deg[u] += 1
        deg[v] += 1

    # exact search for very small n
    if n <= 8:
        vertices = list(range(1, n + 1))
        for perm in itertools.permutations(range(1, n + 1)):
            # perm[i] is slot of vertex i+1
            total = 0
            for u, v in edges:
                total += abs(perm[u - 1] - perm[v - 1])
                if total > B:
                    break
            if total <= B:
                print("YES")
                print(' '.join(map(str, perm)))
                return
        print("NO")
        return

    # heuristic for larger n
    order = sorted(range(1, n + 1), key=lambda x: -deg[x])
    slot_of = [0] * (n + 1)          # slot_of[vertex] = assigned slot
    for idx, v in enumerate(order, start=1):
        slot_of[v] = idx
    total = 0
    for u, v in edges:
        total += abs(slot_of[u] - slot_of[v])
        if total > B:
            break
    if total <= B:
        print("YES")
        print(' '.join(str(slot_of[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()