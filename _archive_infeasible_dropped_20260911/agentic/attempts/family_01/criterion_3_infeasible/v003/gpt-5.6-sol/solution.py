import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]

    adjacency = [0] * n
    upper_neighbors = [[] for _ in range(n)]

    index = 2
    for _ in range(m):
        u = data[index] - 1
        v = data[index + 1] - 1
        index += 2

        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u

        if u < v:
            upper_neighbors[u].append(v)
        else:
            upper_neighbors[v].append(u)

    full_mask = (1 << n) - 1
    higher_mask = [full_mask ^ ((1 << (i + 1)) - 1) for i in range(n)]

    for a in range(n):
        upper_neighbors[a].sort()
        row_a = adjacency[a]

        for b in upper_neighbors[a]:
            common = row_a & adjacency[b] & higher_mask[b]
            if common:
                c = (common & -common).bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    main()