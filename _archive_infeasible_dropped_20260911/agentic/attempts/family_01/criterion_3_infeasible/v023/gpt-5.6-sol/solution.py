import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]

    adjacency = [0] * n
    neighbors = [[] for _ in range(n)]

    index = 2
    for _ in range(m):
        u = data[index] - 1
        v = data[index + 1] - 1
        index += 2

        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u
        neighbors[u].append(v)
        neighbors[v].append(u)

    for vertex_neighbors in neighbors:
        vertex_neighbors.sort()

    for a in range(n - 2):
        for b in neighbors[a]:
            if b <= a:
                continue

            common = adjacency[a] & adjacency[b] & (-1 << (b + 1))
            if common:
                c = (common & -common).bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    main()