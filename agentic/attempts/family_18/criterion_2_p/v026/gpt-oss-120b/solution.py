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

    # try the identity permutation: position[i] = i
    pos = list(range(1, n + 1))
    total = 0
    for u, v in edges:
        total += abs(pos[u - 1] - pos[v - 1])
        if total > B:
            break

    if total <= B:
        print("YES")
        print(' '.join(map(str, pos)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()