import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])

    adj = [0] * n
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    all_mask = (1 << n) - 1
    adj_bar = [0] * n
    for i in range(n):
        adj_bar[i] = all_mask ^ adj[i] ^ (1 << i)

    found = None

    def color_sort(P_mask):
        nodes = []
        temp = P_mask
        while temp:
            v = (temp & -temp).bit_length() - 1
            temp ^= 1 << v
            nodes.append(v)

        colored = []
        color_masks = []
        for v in nodes:
            c = 0
            while c < len(color_masks):
                if (adj_bar[v] & color_masks[c]) == 0:
                    break
                c += 1
            if c == len(color_masks):
                color_masks.append(1 << v)
            else:
                color_masks[c] |= 1 << v
            colored.append((v, c + 1))
        return colored

    def search(P_mask, current):
        nonlocal found
        if found is not None:
            return
        if len(current) == k:
            found = list(current)
            return
        if not P_mask:
            return

        colored = color_sort(P_mask)
        for i in range(len(colored) - 1, -1, -1):
            v, c = colored[i]
            if len(current) + c < k:
                return
            if found is not None:
                return
            current.append(v)
            search(P_mask & adj_bar[v], current)
            current.pop()
            P_mask &= ~(1 << v)

    search(all_mask, [])

    if found is not None:
        print("YES")
        print(*(v + 1 for v in found))
    else:
        print("NO")


if __name__ == "__main__":
    solve()