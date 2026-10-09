import sys
import threading

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    if k == 1:
        print("YES")
        print(1)
        return
    if k > n:
        print("NO")
        return

    found = False
    result = []

    def popcount(x):
        return x.bit_count()

    def bronk(R_mask, P_mask, X_mask):
        nonlocal found, result
        if found:
            return
        if popcount(R_mask) == k:
            # extract vertices
            res = []
            mask = R_mask
            while mask:
                v = (mask & -mask).bit_length() - 1
                res.append(v + 1)
                mask &= mask - 1
            result = res
            found = True
            return
        if popcount(R_mask) + popcount(P_mask) < k:
            return
        # pivot selection
        u = -1
        max_deg = -1
        union = P_mask | X_mask
        temp = union
        while temp:
            v = (temp & -temp).bit_length() - 1
            deg = popcount(P_mask & adj[v])
            if deg > max_deg:
                max_deg = deg
                u = v
            temp &= temp - 1
        if u == -1:
            cand = P_mask
        else:
            cand = P_mask & ~adj[u]
        temp = cand
        while temp:
            v = (temp & -temp).bit_length() - 1
            temp &= temp - 1
            bronk(R_mask | (1 << v), P_mask & adj[v], X_mask & adj[v])
            if found:
                return
            P_mask &= ~(1 << v)
            X_mask |= (1 << v)

    all_mask = (1 << n) - 1
    bronk(0, all_mask, 0)

    if found:
        print("YES")
        print(' '.join(map(str, result)))
    else:
        print("NO")

def main():
    solve()

threading.Thread(target=main).start()