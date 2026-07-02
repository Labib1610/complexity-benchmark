import sys


def main():
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    s = [data[1 + i].decode() for i in range(k)]

    # Drop any fragment that is a substring of another; for equal fragments keep
    # the smallest index. What remains has no fragment contained in another.
    remove = [False] * k
    for i in range(k):
        for j in range(k):
            if i == j:
                continue
            if s[i] in s[j]:
                if len(s[i]) < len(s[j]) or (len(s[i]) == len(s[j]) and j < i):
                    remove[i] = True
                    break
    frags = [s[i] for i in range(k) if not remove[i]]
    m = len(frags)

    if m == 1:
        sys.stdout.write(frags[0] + "\n")
        return

    # Max suffix-prefix overlap ov[i][j]: longest L with frags[i][-L:] == frags[j][:L].
    ov = [[0] * m for _ in range(m)]
    for i in range(m):
        a = frags[i]
        for j in range(m):
            if i == j:
                continue
            b = frags[j]
            mx = min(len(a), len(b))
            for L in range(mx, 0, -1):
                if a[len(a) - L:] == b[:L]:
                    ov[i][j] = L
                    break

    # Held-Karp: dp[mask][last] = (length, string) of the shortest, then
    # lexicographically smallest, superstring of `mask` that ends with `last`.
    dp = [[None] * m for _ in range(1 << m)]
    for i in range(m):
        dp[1 << i][i] = (len(frags[i]), frags[i])

    for mask in range(1 << m):
        row = dp[mask]
        for i in range(m):
            cur = row[i]
            if cur is None:
                continue
            clen, cstr = cur
            for j in range(m):
                if mask >> j & 1:
                    continue
                add = frags[j][ov[i][j]:]
                cand = (clen + len(add), cstr + add)
                nmask = mask | (1 << j)
                old = dp[nmask][j]
                if old is None or cand < old:
                    dp[nmask][j] = cand

    full = (1 << m) - 1
    best = None
    for i in range(m):
        c = dp[full][i]
        if c is not None and (best is None or c < best):
            best = c

    sys.stdout.write(best[1] + "\n")


main()
