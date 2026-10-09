import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); m = int(data[idx + 1]); idx += 2
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        adj[u].append(v); adj[v].append(u)

    # Find ANY proper 3-colouring (or prove none) with forward checking + the most-constrained-vertex
    # (minimum-remaining-values) heuristic. `dom[v]` is a 3-bit mask of colours still available for v.
    ALL = 0b111
    dom = [ALL] * (n + 1)
    color = [0] * (n + 1)
    assigned = [False] * (n + 1)
    sys.setrecursionlimit(1 << 20)

    def pick():
        best, bestc = -1, 4
        for v in range(1, n + 1):
            if not assigned[v]:
                c = bin(dom[v]).count("1")
                if c < bestc:
                    bestc, best = c, v
                    if c <= 1:
                        break
        return best

    def solve(remaining):
        if remaining == 0:
            return True
        v = pick()
        if dom[v] == 0:
            return False
        options = dom[v]
        bit = 1
        for ci in range(3):
            if options & (1 << ci):
                assigned[v] = True
                color[v] = ci + 1
                removed = []
                ok = True
                cmask = ~(1 << ci)
                for u in adj[v]:
                    if not assigned[u] and (dom[u] & (1 << ci)):
                        dom[u] &= cmask
                        removed.append(u)
                        if dom[u] == 0:
                            ok = False
                if ok and solve(remaining - 1):
                    return True
                for u in removed:
                    dom[u] |= (1 << ci)
                assigned[v] = False
                color[v] = 0
        return False

    if solve(n):
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, color[1:n + 1])) + "\n")
    else:
        sys.stdout.write("NO\n")


main()
