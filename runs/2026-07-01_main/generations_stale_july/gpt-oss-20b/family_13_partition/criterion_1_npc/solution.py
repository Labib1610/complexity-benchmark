import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    d = [int(next(it)) for _ in range(n)]
    total = sum(d)
    if total % 2 != 0:
        print("NO")
        return
    target = total // 2
    mid = n // 2
    first = d[:mid]
    second = d[mid:]

    sum_to_mask = {}
    # enumerate first half
    for mask in range(1 << mid):
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
        # early exit if exact target found
        if s == target:
            res = []
            for i in range(mid):
                if mask >> i & 1:
                    res.append(str(i + 1))
            print("YES")
            print(' '.join(res))
            return

    # enumerate second half
    for mask2 in range(1 << (n - mid)):
        s2 = 0
        m = mask2
        idx = 0
        while m:
            if m & 1:
                s2 += second[idx]
            idx += 1
            m >>= 1
        need = target - s2
        if need in sum_to_mask:
            mask1 = sum_to_mask[need]
            res = []
            for i in range(mid):
                if mask1 >> i & 1:
                    res.append(str(i + 1))
            for j in range(n - mid):
                if mask2 >> j & 1:
                    res.append(str(mid + j + 1))
            print("YES")
            print(' '.join(res))
            return
        # early exit if second half alone matches target
        if s2 == target:
            res = []
            for j in range(n - mid):
                if mask2 >> j & 1:
                    res.append(str(mid + j + 1))
            print("YES")
            print(' '.join(res))
            return

    print("NO")

if __name__ == "__main__":
    solve()