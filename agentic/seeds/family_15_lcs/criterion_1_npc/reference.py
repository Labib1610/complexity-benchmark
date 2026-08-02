import sys
from functools import lru_cache


def main():
    sys.setrecursionlimit(1000000)
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    seqs = [data[1 + i].decode() for i in range(k)]
    lens = [len(s) for s in seqs]

    # k-dimensional DP: dp(pos) = length of the longest shared motif of the
    # suffixes seqs[j][pos[j]:]. If all current letters match, take it; else
    # advance one sequence.
    @lru_cache(maxsize=None)
    def dp(pos):
        for j in range(k):
            if pos[j] == lens[j]:
                return 0
        chars = {seqs[j][pos[j]] for j in range(k)}
        best = 0
        if len(chars) == 1:
            best = 1 + dp(tuple(p + 1 for p in pos))
        for j in range(k):
            nxt = list(pos)
            nxt[j] += 1
            v = dp(tuple(nxt))
            if v > best:
                best = v
        return best

    start = tuple([0] * k)
    L = dp(start)

    # Reconstruct one motif of length L following optimal DP transitions.
    pos = list(start)
    res = []
    while len(res) < L:
        cur = dp(tuple(pos))
        in_range = all(pos[j] < lens[j] for j in range(k))
        took = False
        if in_range:
            chars = {seqs[j][pos[j]] for j in range(k)}
            if len(chars) == 1 and 1 + dp(tuple(p + 1 for p in pos)) == cur:
                res.append(next(iter(chars)))
                pos = [p + 1 for p in pos]
                took = True
        if not took:
            for j in range(k):
                if pos[j] < lens[j]:
                    nxt = list(pos)
                    nxt[j] += 1
                    if dp(tuple(nxt)) == cur:
                        pos = nxt
                        break

    sys.stdout.write(f"{L}\n")
    sys.stdout.write("".join(res) + "\n")


main()
