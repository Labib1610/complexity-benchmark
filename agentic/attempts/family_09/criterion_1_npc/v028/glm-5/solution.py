import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    if k == 1:
        print("YES")
        print(1)
        return

    full = (1 << (n + 1)) - 1
    for i in range(1, n + 1):
        adj[i] = full ^ adj[i] ^ (1 << i)

    if k == 2:
        for u in range(1, n + 1):
            if adj[u] & ((1 << (n + 1)) - 2):
                v = (adj[u] & ((1 << (n + 1)) - 2)).bit_length() - 1
                print("YES")
                print(u, v)
                return
        print("NO")
        return

    half = n // 2
    left = list(range(1, half + 1))
    right = list(range(half + 1, n + 1))

    def get_mask(nodes):
        res = 0
        for x in nodes:
            res |= 1 << x
        return res

    left_mask = get_mask(left)
    right_mask = get_mask(right)

    def popcount(x):
        return bin(x).count('1')

    best_left = {}
    for s in range(1 << len(left)):
        mask = 0
        cnt = 0
        for i, v in enumerate(left):
            if s & (1 << i):
                mask |= 1 << v
                cnt += 1
        if cnt > k:
            continue
        ok = True
        for v in left:
            if mask & (1 << v):
                if (adj[v] & mask) != mask:
                    ok = False
                    break
        if not ok:
            continue
        inter = mask & right_mask
        if cnt <= k:
            if inter not in best_left or cnt > best_left[inter]:
                best_left[inter] = cnt

    best_right = {}
    for s in range(1 << len(right)):
        mask = 0
        cnt = 0
        for i, v in enumerate(right):
            if s & (1 << i):
                mask |= 1 << v
                cnt += 1
        if cnt > k:
            continue
        ok = True
        for v in right:
            if mask & (1 << v):
                if (adj[v] & mask) != mask:
                    ok = False
                    break
        if not ok:
            continue
        inter = mask & left_mask
        if cnt <= k:
            if inter not in best_right or cnt > best_right[inter]:
                best_right[inter] = cnt

    for inter, lc in best_left.items():
        need = k - lc
        if need < 0:
            continue
        if need == 0:
            if inter == 0:
                print("YES")
                res = []
                for v in left:
                    if inter & (1 << v):
                        res.append(v)
                print(' '.join(map(str, res)))
                return
            continue
        if need in best_right.values():
            for r_inter, rc in best_right.items():
                if rc == need:
                    if (inter & r_inter) == 0:
                        print("YES")
                        res = []
                        for v in left:
                            if inter & (1 << v):
                                res.append(v)
                        for v in right:
                            if r_inter & (1 << v):
                                res.append(v)
                        print(' '.join(map(str, res)))
                        return

    print("NO")

solve()