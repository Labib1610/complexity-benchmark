import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adjacency = [0] * (n + 1)
    neighbors = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adjacency[u] |= 1 << (v - 1)
        adjacency[v] |= 1 << (u - 1)
        neighbors[u].append(v)
        neighbors[v].append(u)

    for a in range(1, n + 1):
        mask_a = adjacency[a]
        for b in neighbors[a]:
            if b <= a:
                continue
            common = mask_a & adjacency[b]
            # need c > b
            mask = common >> b
            if mask == 0:
                continue
            lowbit = mask & -mask
            c = b + lowbit.bit_length()
            print(a, b, c)
            return

if __name__ == "__main__":
    main()