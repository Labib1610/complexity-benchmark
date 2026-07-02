import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    d = [int(data[1 + i]) for i in range(n)]

    total = sum(d)
    if total % 2 != 0:
        sys.stdout.write("NO\n")
        return
    target = total // 2

    # Meet-in-the-middle: find a subset summing to target (half of the total).
    half = n // 2
    A = d[:half]
    B = d[half:]

    def all_subsets(part):
        res = [(0, 0)]  # (sum, mask over local indices)
        for i, v in enumerate(part):
            bit = 1 << i
            res += [(s + v, m | bit) for (s, m) in res]
        return res

    sums_b = {}
    for s, m in all_subsets(B):
        if s not in sums_b:
            sums_b[s] = m

    for s, mask_a in all_subsets(A):
        need = target - s
        m_b = sums_b.get(need)
        if m_b is not None:
            chosen = []
            for i in range(half):
                if mask_a >> i & 1:
                    chosen.append(i + 1)
            for i in range(len(B)):
                if m_b >> i & 1:
                    chosen.append(half + i + 1)
            sys.stdout.write("YES\n")
            sys.stdout.write(" ".join(map(str, chosen)) + "\n")
            return

    sys.stdout.write("NO\n")


main()
