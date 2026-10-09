import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    left = []   # a <= b
    right = []  # a > b
    total_b = 0
    for _ in range(n):
        a = int(next(it))
        b = int(next(it))
        total_b += b
        if a <= b:
            left.append((a, b))
        else:
            right.append((a, b))
    # Johnson's rule
    left.sort(key=lambda x: x[0])          # increasing a
    right.sort(key=lambda x: -x[1])        # decreasing b
    order = left + right

    pref = 0
    suffix_b = total_b
    ans = 0
    for a, b in order:
        pref += a
        suffix_b -= b
        cur = pref + suffix_b
        if cur > ans:
            ans = cur
    print(ans)

if __name__ == "__main__":
    solve()