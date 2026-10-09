import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    brackets = []
    total_d2 = 0
    for _ in range(n):
        d1 = int(next(it))
        d2 = int(next(it))
        brackets.append((d1, d2, d1 - d2))
        total_d2 += d2

    # Johnson's rule: sort by decreasing (d1 - d2)
    brackets.sort(key=lambda x: x[2], reverse=True)

    pref_d1 = 0
    removed_d2 = 0
    ans = 0
    for d1, d2, _ in brackets:
        pref_d1 += d1
        # suffix sum of d2 from current position = total_d2 - removed_d2
        suffix = total_d2 - removed_d2
        cur = pref_d1 + suffix
        if cur > ans:
            ans = cur
        removed_d2 += d2

    print(ans)

if __name__ == "__main__":
    solve()