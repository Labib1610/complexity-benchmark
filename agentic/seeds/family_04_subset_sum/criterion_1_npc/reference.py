import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    costs = [int(data[idx + i]) for i in range(n)]; idx += n
    T = int(data[idx]); idx += 1

    # Meet-in-the-middle: split the items into two halves, enumerate every
    # subset sum of each half (2^(n/2) each), hash the second half by sum, then
    # for each first-half sum s look up the complement T - s.
    half = n // 2
    A = costs[:half]
    B = costs[half:]

    def all_subset_sums(vals):
        res = [(0, 0)]  # (sum, mask over vals)
        for j, v in enumerate(vals):
            bit = 1 << j
            res += [(s + v, m | bit) for s, m in res]
        return res

    sums_b = {}
    for s, m in all_subset_sums(B):
        if s not in sums_b:
            sums_b[s] = m

    for s, mask_a in all_subset_sums(A):
        need = T - s
        m_b = sums_b.get(need)
        if m_b is not None:
            chosen = []
            for j in range(half):
                if mask_a >> j & 1:
                    chosen.append(j + 1)
            for j in range(len(B)):
                if m_b >> j & 1:
                    chosen.append(half + j + 1)
            print("YES")
            print(' '.join(map(str, chosen)))
            return

    print("NO")


main()
