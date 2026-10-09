import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    k = int(data[2])

    adj = [0] * n
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    def search(P, cur):
        if len(cur) >= k:
            return cur[:k]
        if len(cur) + P.bit_count() < k:
            return None

        # Choose pivot u in P that maximizes |P & adj[u]|
        pivot = -1
        max_deg = -1
        temp = P
        while temp:
            v = (temp & -temp).bit_length() - 1
            deg = (P & adj[v]).bit_count()
            if deg > max_deg:
                max_deg = deg
                pivot = v
            temp &= temp - 1

        cands = P & ~adj[pivot]
        while cands:
            v = (cands & -cands).bit_length() - 1
            cur.append(v + 1)
            res = search(P & ~adj[v] & ~(1 << v), cur)
            if res is not None:
                return res
            cur.pop()
            cands &= cands - 1
            P &= ~(1 << v)

        return None

    initial_P = (1 << n) - 1
    ans = search(initial_P, [])

    if ans is not None:
        print("YES")
        print(*(ans))
    else:
        print("NO")

if __name__ == '__main__':
    main()