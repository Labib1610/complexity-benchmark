import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # order vertices by degree descending
    order = sorted(range(n), key=lambda x: -adj[x].bit_count())
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [-1] * n          # -1 uncolored, else 0,1,2
    # possible colors mask for each vertex (bits 0,1,2)
    poss = [0b111] * n

    # initial propagation: none

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        v = order[idx]
        # compute allowed colors from neighbors already colored
        forbidden = 0
        nb = adj[v]
        while nb:
            u = (nb & -nb).bit_length() - 1
            nb &= nb - 1
            c = colors[u]
            if c != -1:
                forbidden |= 1 << c
        allowed = poss[v] & (~forbidden) & 0b111
        if allowed == 0:
            return False
        # try colors in order 0,1,2
        for col in range(3):
            if allowed >> col & 1:
                # assign
                colors[v] = col
                saved = []
                # forward checking: remove this color from neighbors' possibilities
                nb2 = adj[v]
                consistent = True
                while nb2:
                    u = (nb2 & -nb2).bit_length() - 1
                    nb2 &= nb2 - 1
                    if colors[u] == -1:
                        if poss[u] & (1 << col):
                            saved.append((u, poss[u]))
                            poss[u] &= ~ (1 << col)
                            if poss[u] == 0:
                                consistent = False
                                break
                if consistent and dfs(idx + 1):
                    return True
                # rollback
                for u, old in saved:
                    poss[u] = old
                colors[v] = -1
        return False

    if dfs(0):
        print("YES")
        # convert 0,1,2 to 1,2,3
        print(' '.join(str(c+1) for c in colors))
    else:
        print("NO")

if __name__ == "__main__":
    solve()