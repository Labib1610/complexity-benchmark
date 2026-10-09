import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    d = [int(data[1 + i]) for i in range(n)]

    total = sum(d)
    if total % 2 != 0:
        sys.stdout.write("NO\n")
        return
    target = total // 2

    # Bitset subset-sum DP: dp[i] = the set of sums reachable with the first i items, stored as a
    # Python int (bit j set == sum j reachable). O(n * target / 64) -- fast and well within limits.
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] | (dp[i - 1] << d[i - 1])

    if not (dp[n] >> target) & 1:
        sys.stdout.write("NO\n")
        return

    # Reconstruct one group by walking the dp layers backwards.
    chosen = []
    j = target
    for i in range(n, 0, -1):
        if (dp[i - 1] >> j) & 1:
            continue                      # sum j reachable without item i -> item i not needed
        chosen.append(i)                  # item i is required
        j -= d[i - 1]
    chosen.sort()

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, chosen)) + "\n")


main()
