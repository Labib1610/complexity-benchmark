import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); B = int(data[idx + 1]); idx += 2
    items = []
    for _ in range(n):
        c = int(data[idx]); v = int(data[idx + 1]); idx += 2
        items.append((c, v))

    # 0/1 knapsack by pseudo-polynomial DP over the budget: dp[j] = best value with total cost <= j.
    # Polynomial here because B <= 2000. `take[i]` records, as a bitmask over capacities, where
    # item i was taken to improve dp[j], so one optimal subset can be reconstructed.
    dp = [0] * (B + 1)
    take = [0] * (n + 1)
    for i in range(1, n + 1):
        c, v = items[i - 1]
        if c > B:
            continue
        ti = 0
        for j in range(B, c - 1, -1):
            cand = dp[j - c] + v
            if cand > dp[j]:
                dp[j] = cand
                ti |= (1 << j)
        take[i] = ti

    best = dp[B]

    # Reconstruct one optimal subset by walking the take masks backwards.
    chosen = []
    j = B
    for i in range(n, 0, -1):
        if (take[i] >> j) & 1:
            chosen.append(i)
            j -= items[i - 1][0]
    chosen.sort()

    sys.stdout.write(f"{best}\n")
    sys.stdout.write(" ".join(map(str, chosen)) + "\n")


main()
