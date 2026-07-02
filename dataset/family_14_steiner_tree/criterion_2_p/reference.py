import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); m = int(data[idx + 1]); idx += 2

    edges = []
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); w = int(data[idx + 2]); idx += 3
        edges.append((w, u, v))

    edges.sort()

    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    # Kruskal: add cabling options cheapest first, skipping ones that would form
    # a redundant loop, until all sites are connected.
    total = 0
    used = 0
    for w, u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
            total += w
            used += 1
            if used == n - 1:
                break

    print(total)


main()
