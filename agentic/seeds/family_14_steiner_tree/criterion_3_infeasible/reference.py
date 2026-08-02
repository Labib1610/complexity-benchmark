import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); m = int(data[idx + 1]); t = int(data[idx + 2]); idx += 3
    terminals = [int(data[idx + i]) for i in range(t)]; idx += t

    deg = [0] * (n + 1)
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 3  # weight unused here
        deg[u] += 1
        deg[v] += 1

    # A required site with no cabling option touching it cannot be connected.
    for site in sorted(terminals):
        if deg[site] == 0:
            print(site)
            return

    # Fallback (inputs for this criterion always contain such a site).
    print(-1)


main()
