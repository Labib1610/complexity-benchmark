import sys


def main():
    sys.setrecursionlimit(100000)
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    adj = [0] * n  # bitset of neighbors
    for _ in range(m):
        u = int(data[idx]) - 1; v = int(data[idx + 1]) - 1; idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    found = []

    # Branch and bound over candidate sets. `R` is the current clique, `P` the
    # bitset of vertices adjacent to all of R. Extend until |R| == k.
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
            P &= ~(1 << v)                 # v not reused in later siblings
            R.append(v)
            expand(R, P & adj[v])
            R.pop()
            if len(R) + bin(P).count("1") < k:
                return

    expand([], (1 << n) - 1)

    if found:
        clique = sorted(x + 1 for x in found)
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, clique)) + "\n")
    else:
        sys.stdout.write("NO\n")


main()
