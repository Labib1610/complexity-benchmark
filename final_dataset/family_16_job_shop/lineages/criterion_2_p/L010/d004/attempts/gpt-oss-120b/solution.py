import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    first = []
    second = []
    for _ in range(n):
        d1 = int(next(it)); d2 = int(next(it))
        if d1 <= d2:
            first.append((d1, d2))
        else:
            second.append((d1, d2))
    first.sort(key=lambda x: x[0])          # ascending d1
    second.sort(key=lambda x: x[1], reverse=True)  # descending d2
    order = first + second

    X = 0
    Y = 0
    for i, (d1, d2) in enumerate(order):
        if i == 0:
            X = 0
            Y = X + d1
        else:
            # advance X by previous d1 (already accounted in previous loop)
            X += prev_d1
            # Y must be at least previous Y + previous d2, and also X + d1
            Y = max(Y + prev_d2, X + d1)
        prev_d1, prev_d2 = d1, d2
    # after last job, final boundary
    result = Y + prev_d2
    sys.stdout.write(str(result))

if __name__ == "__main__":
    solve()