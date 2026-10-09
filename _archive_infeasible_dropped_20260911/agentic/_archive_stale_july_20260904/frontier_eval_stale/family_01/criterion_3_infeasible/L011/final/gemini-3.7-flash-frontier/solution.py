import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    adj = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for u in range(1, n + 1):
        mask_u = adj[u]
        # Iterate over neighbors v > u
        v_mask = mask_u >> (u + 1)
        v = u + 1
        while v_mask:
            if v_mask & 1:
                common = (mask_u & adj[v]) >> (v + 1)
                if common:
                    lsb = common & -common
                    w = v + lsb.bit_length()
                    print(f"{u} {v} {w}")
                    return
            v_mask >>= 1
            v += 1


if __name__ == "__main__":
    solve()