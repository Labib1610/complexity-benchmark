import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    idx = 2
    neighbor_sets = [set() for _ in range(n + 1)]
    adj_bits = [0] * (n + 1)
    for _ in range(m):
        u, v = data[idx], data[idx + 1]
        idx += 2
        if v not in neighbor_sets[u]:
            neighbor_sets[u].add(v)
            neighbor_sets[v].add(u)
            adj_bits[u] |= 1 << (v - 1)
            adj_bits[v] |= 1 << (u - 1)
    neighbors = [sorted(neighbor_sets[i]) for i in range(n + 1)]
    for a in range(1, n + 1):
        for b in neighbors[a]:
            if b <= a:
                continue
            intersect = adj_bits[a] & adj_bits[b]
            shift = b - 1
            y = intersect >> shift
            if y:
                low = y & -y
                k = low.bit_length() - 1
                c = b + k
                print(a, b, c)
                return

if __name__ == "__main__":
    main()