import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    costs = [int(next(it)) for _ in range(n)]
    T = int(next(it))

    dp = [-1] * (T + 1)          # dp[t] = index used to reach t, -1 unreachable
    prev = [-1] * (T + 1)        # prev[t] = previous sum before using dp[t]
    dp[0] = -2                   # sentinel for start

    for idx, c in enumerate(costs):
        if c > T:
            continue
        for t in range(T, c - 1, -1):
            if dp[t] == -1 and dp[t - c] != -1:
                dp[t] = idx
                prev[t] = t - c

    if dp[T] == -1:
        print("NO")
        return

    # reconstruct indices
    indices = []
    t = T
    while t > 0:
        idx = dp[t]
        indices.append(idx + 1)  # convert to 1-based
        t = prev[t]
    indices.reverse()

    print("YES")
    if indices:
        print(' '.join(map(str, indices)))
    else:
        print()

if __name__ == "__main__":
    solve()