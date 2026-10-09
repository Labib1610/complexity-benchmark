import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        edges.append((u, v))

    # Greedily collect corridors whose endpoints are still unused, building a set
    # of pairwise independent corridors, until k+1 are gathered. Each such
    # corridor needs its own guard, certifying k guards cannot suffice.
    used = [False] * (n + 1)
    picked = []
    for (u, v) in edges:
        if not used[u] and not used[v]:
            used[u] = used[v] = True
            picked.append((u, v))
            if len(picked) == k + 1:
                break

    out = "\n".join(f"{u} {v}" for (u, v) in picked)
    sys.stdout.write(out + "\n")


main()
