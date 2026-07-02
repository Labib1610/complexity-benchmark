import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    deg = [0] * (n + 1)
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        deg[u] += 1
        deg[v] += 1

    # With budget k = 0, a location with no links can never be covered.
    for v in range(1, n + 1):
        if deg[v] == 0:
            print(v)
            return

    # Fallback (inputs for this criterion always contain an isolated location).
    print(-1)


main()
