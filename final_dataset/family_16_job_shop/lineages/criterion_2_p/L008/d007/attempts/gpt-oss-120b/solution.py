import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    it = iter(data[1:])
    total_a = 0
    pos = []          # (d, c, a, b)   for b >= a
    neg = []          # (a, b)         for b <  a

    for a, b in zip(it, it):
        total_a += a
        if b >= a:
            d = b - a               # we keep half of the real d (divide by 2)
            c = 2 * b
            pos.append((d, c, a, b))
        else:
            neg.append((a, b))

    # group with non‑negative d : decreasing d, then increasing c
    pos.sort(key=lambda x: (-x[0], x[1]))
    # group with negative d : decreasing a
    neg.sort(key=lambda x: -x[0])

    D = 0  # current difference S - P
    for d_half, c, a, b in pos:
        inc = 2 * (b - a)           # = 2*d_half
        tmp = D + inc
        D = c if tmp < c else tmp

    for a, b in neg:
        inc = 2 * (b - a)           # negative
        c = 2 * b
        tmp = D + inc
        D = c if tmp < c else tmp

    answer = total_a + D // 2
    sys.stdout.write(str(answer))

if __name__ == "__main__":
    solve()