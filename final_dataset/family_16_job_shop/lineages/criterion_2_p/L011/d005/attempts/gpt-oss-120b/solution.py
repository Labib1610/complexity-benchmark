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
        x = int(next(it))
        y = int(next(it))
        if x <= y:
            first.append((x, y))
        else:
            second.append((x, y))
    # Johnson's rule
    first.sort(key=lambda p: p[0])          # increasing X
    second.sort(key=lambda p: p[1], reverse=True)  # decreasing Y
    seq = first + second

    # compute makespan using the given formula (or simulate)
    pref = 0
    suffix_y = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_y[i] = suffix_y[i + 1] + seq[i][1]

    ans = 0
    for i, (x, _) in enumerate(seq, 1):
        pref += x
        cur = pref + suffix_y[i - 1]   # suffix from i to end
        if cur > ans:
            ans = cur
    print(ans)

if __name__ == "__main__":
    solve()