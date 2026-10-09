import sys


def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    adj_mask = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]

    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u
        adj_list[u].append(v)
        adj_list[v].append(u)

    for i in range(1, n + 1):
        adj_list[i].sort()

    for a in range(1, n + 1):
        for b in adj_list[a]:
            if b <= a:
                continue
            common = (adj_mask[a] & adj_mask[b]) >> (b + 1)
            if common:
                c = b + 1 + (common & -common).bit_length() - 1
                print(f"{a} {b} {c}")
                return


if __name__ == "__main__":
    main()