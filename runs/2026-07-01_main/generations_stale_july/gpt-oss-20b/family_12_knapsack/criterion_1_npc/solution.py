import sys, bisect

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    B = int(next(it))
    costs = []
    values = []
    for _ in range(n):
        costs.append(int(next(it)))
        values.append(int(next(it)))
    k = n // 2
    first_costs = costs[:k]
    first_values = values[:k]
    second_costs = costs[k:]
    second_values = values[k:]
    # generate subsets for first half
    first_subs = []
    for mask in range(1 << k):
        c = 0
        v = 0
        for i in range(k):
            if mask >> i & 1:
                c += first_costs[i]
                v += first_values[i]
        first_subs.append((c, v, mask))
    # generate subsets for second half
    m = n - k
    second_subs = []
    for mask in range(1 << m):
        c = 0
        v = 0
        for i in range(m):
            if mask >> i & 1:
                c += second_costs[i]
                v += second_values[i]
        second_subs.append((c, v, mask))
    # sort second half by cost
    second_subs.sort(key=lambda x: x[0])
    # prune dominated
    pruned = []
    best_val = -1
    for c, v, mask in second_subs:
        if v > best_val:
            pruned.append((c, v, mask))
            best_val = v
    # prepare cost list for binary search
    pruned_costs = [c for c, _, _ in pruned]
    best_total = 0
    best_mask1 = 0
    best_mask2 = 0
    for c1, v1, mask1 in first_subs:
        if c1 > B:
            continue
        rem = B - c1
        idx = bisect.bisect_right(pruned_costs, rem) - 1
        if idx >= 0:
            c2, v2, mask2 = pruned[idx]
            total = v1 + v2
            if total > best_total:
                best_total = total
                best_mask1 = mask1
                best_mask2 = mask2
    # output
    out_lines = []
    out_lines.append(str(best_total))
    if best_total == 0:
        out_lines.append('')
    else:
        indices = []
        for i in range(k):
            if best_mask1 >> i & 1:
                indices.append(str(i + 1))
        for j in range(m):
            if best_mask2 >> j & 1:
                indices.append(str(k + j + 1))
        out_lines.append(' '.join(indices))
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    solve()