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

    # try the natural order 1..n
    total = 0
    for u, v in edges:
        total += abs(u - v)  # positions are same as node numbers
        if total > B:  # early exit
            break

    if total <= B:
        print("YES")
        print(' '.join(str(i) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()