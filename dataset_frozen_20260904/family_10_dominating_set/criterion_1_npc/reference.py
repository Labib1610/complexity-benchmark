import sys


def main():
    sys.setrecursionlimit(100000)
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    # Closed-neighborhood bitsets: nb[v] has bit v and every neighbor of v.
    nb = [1 << v for v in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1; v = int(data[idx + 1]) - 1; idx += 2
        nb[u] |= (1 << v)
        nb[v] |= (1 << u)

    full = (1 << n) - 1
    found = []

    # Branch on the lowest still-uncovered location u: some sensor covering u
    # must be placed at a location in nb[u]. Try each, bounded by budget k.
    def solve(covered, chosen, budget):
        if found:
            return
        if covered == full:
            found.extend(chosen)
            return
        if budget == 0:
            return
        rest = ~covered & full
        u = (rest & -rest).bit_length() - 1
        cand = nb[u]
        while cand and not found:
            w = (cand & -cand).bit_length() - 1
            cand &= cand - 1
            chosen.append(w)
            solve(covered | nb[w], chosen, budget - 1)
            chosen.pop()

    solve(0, [], k)

    if found:
        sensors = sorted(x + 1 for x in found)
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, sensors)) + "\n")
    else:
        sys.stdout.write("NO\n")


main()
