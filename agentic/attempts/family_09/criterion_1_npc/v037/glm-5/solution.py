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
        adj[i] = (adj[i] << 1) & full

    size = [0] * (1 << n)
    for i in range(1, 1 << n):
        lsb = i & (-i)
        v = lsb.bit_length() - 1
        size[i] = size[i ^ lsb] + 1

    best = [0] * (1 << n)
    for i in range(1, 1 << n):
        lsb = i & (-i)
        v = lsb.bit_length() - 1
        best[i] = best[i ^ lsb] | (1 << (v + 1))

    for i in range(1, 1 << n):
        if size[i] == 1:
            continue
        lsb = i & (-i)
        v = lsb.bit_length() - 1
        rest = i ^ lsb
        cand = best[rest] & ~adj[v + 1]
        if size[cand] > size[best[i]]:
            best[i] = cand

    for i in range(1, 1 << n):
        if size[i] >= k and size[best[i]] >= k:
            print("YES")
            bits = best[i]
            out = []
            cnt = 0
            while bits:
                lsb = bits & (-bits)
                v = lsb.bit_length() - 1
                out.append(v)
                cnt += 1
                if cnt == k:
                    break
                bits ^= lsb
            print(' '.join(map(str, out)))
            return

    print("NO")

solve()