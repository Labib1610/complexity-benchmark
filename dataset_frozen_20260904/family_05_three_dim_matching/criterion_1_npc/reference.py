import sys


def main():
    sys.setrecursionlimit(10000)
    data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1

    # Group allowed combinations by their specialist x, sorted by (y, z) so the
    # search is deterministic. Backtracking assigns specialists 1..k in order,
    # each getting one allowed combination whose machine and slot are still free.
    by_x = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx + 1]); z = int(data[idx + 2]); idx += 3
        by_x[x].append((y, z))
    for x in range(1, k + 1):
        by_x[x].sort()

    used_y = [False] * (k + 1)
    used_z = [False] * (k + 1)
    chosen = []

    def solve(x):
        if x > k:
            return True
        for (y, z) in by_x[x]:
            if not used_y[y] and not used_z[z]:
                used_y[y] = used_z[z] = True
                chosen.append((x, y, z))
                if solve(x + 1):
                    return True
                chosen.pop()
                used_y[y] = used_z[z] = False
        return False

    if solve(1):
        out = ["YES"]
        out.extend(f"{x} {y} {z}" for (x, y, z) in chosen)
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")


main()
