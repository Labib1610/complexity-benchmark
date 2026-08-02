import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_mask = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj_mask[u] |= 1 << (v - 1)
        adj_mask[v] |= 1 << (u - 1)
        adj_list[u].append(v)
        adj_list[v].append(u)

    for i in range(1, n + 1):
        adj_list[i].sort()

    for a in range(1, n + 1):
        for b in adj_list[a]:
            if b <= a:
                continue
            common = adj_mask[a] & adj_mask[b]
            mask = common >> b
            if mask:
                pos = mask & -mask
                idx = pos.bit_length() - 1
                c = idx + b + 1
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    main()