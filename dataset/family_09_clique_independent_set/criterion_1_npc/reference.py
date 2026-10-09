import sys


def main():
    sys.setrecursionlimit(100000)
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    adjG = [0] * n
    for _ in range(m):
        u = int(data[idx]) - 1; v = int(data[idx + 1]) - 1; idx += 2
        adjG[u] |= (1 << v)
        adjG[v] |= (1 << u)

    # An independent set in G is a clique in the complement of G. Build complement adjacency and run
    # a bitset branch-and-bound to find a clique of size k there (== an independent set of size k).
    comp = [(((1 << n) - 1) ^ (1 << i)) & ~adjG[i] for i in range(n)]

    found = []

    def expand(R, P):
        if found:
            return
        if len(R) == k:
            found.extend(R)
            return
        if len(R) + bin(P).count("1") < k:
            return
        Pp = P
        while Pp and not found:
            v = (Pp & -Pp).bit_length() - 1
            Pp &= Pp - 1
            P &= ~(1 << v)
            R.append(v)
            expand(R, P & comp[v])
            R.pop()
            if len(R) + bin(P).count("1") < k:
                return

    if k <= n:
        expand([], (1 << n) - 1)

    if found:
        iset = sorted(x + 1 for x in found)
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, iset)) + "\n")
    else:
        sys.stdout.write("NO\n")


main()
