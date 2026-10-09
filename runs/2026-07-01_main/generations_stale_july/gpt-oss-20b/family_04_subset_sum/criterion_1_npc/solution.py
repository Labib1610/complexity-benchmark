import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    costs = [int(next(it)) for _ in range(n)]
    T = int(next(it))

    mid = n // 2
    first = costs[:mid]
    second = costs[mid:]

    sum_to_mask = {}
    len1 = len(first)
    for mask in range(1 << len1):
        s = 0
        m = mask
        idx = 0
        while m:
            if m & 1:
                s += first[idx]
            idx += 1
            m >>= 1
        if s not in sum_to_mask:
            sum_to_mask[s] = mask

    len2 = len(second)
    found = False
    res_mask1 = 0
    res_mask2 = 0
    for mask in range(1 << len2):
        s = 0
        m = mask
        idx = 0
        while m:
            if m & 1:
                s += second[idx]
            idx += 1
            m >>= 1
        need = T - s
        if need in sum_to_mask:
            res_mask1 = sum_to_mask[need]
            res_mask2 = mask
            found = True
            break

    out = []
    if found:
        indices = []
        m = res_mask1
        idx = 0
        while m:
            if m & 1:
                indices.append(idx + 1)
            idx += 1
            m >>= 1
        m = res_mask2
        idx = 0
        while m:
            if m & 1:
                indices.append(mid + idx + 1)
            idx += 1
            m >>= 1
        out.append("YES")
        out.append(" ".join(map(str, indices)))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()