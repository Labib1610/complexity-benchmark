import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    tiles = []
    total_bot = 0
    for _ in range(n):
        a = int(next(it))
        b = int(next(it))
        tiles.append((a, b, a - b))
        total_bot += b

    # sort by decreasing (a - b)
    tiles.sort(key=lambda x: -x[2])

    pref_top = 0
    pref_bot_prev = 0
    best = 0
    for a, b, _ in tiles:
        pref_top += a
        # suffix bottom includes current b
        suff_bot = total_bot - pref_bot_prev
        cost = pref_top + suff_bot
        if cost > best:
            best = cost
        pref_bot_prev += b

    print(best)

if __name__ == "__main__":
    solve()