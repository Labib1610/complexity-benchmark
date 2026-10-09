import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n               # -1 = uncoloured, else 0/1/2
    mask = [0b111] * n             # possible colours bitmask
    changes = []                    # stack of (vertex, old_mask)

    # helper: popcount of 3-bit mask
    popcnt = lambda x: (x & 1) + ((x >> 1) & 1) + ((x >> 2) & 1)

    def assign(v: int, c: int) -> bool:
        """assign colour c to vertex v, update neighbours, record changes.
           return False if conflict arises."""
        color[v] = c
        old_mask = mask[v]
        mask[v] = 1 << c
        changes.append((v, old_mask))
        for nb in adj[v]:
            if color[nb] == -1:
                old = mask[nb]
                if old & (1 << c):
                    new = old & ~(1 << c)
                    if new == 0:
                        # conflict, record change then fail
                        mask[nb] = new
                        changes.append((nb, old))
                        return False
                    if new != old:
                        mask[nb] = new
                        changes.append((nb, old))
        return True

    def undo(to_len: int) -> None:
        """undo changes back to given stack length."""
        while len(changes) > to_len:
            v, old = changes.pop()
            mask[v] = old
            if color[v] != -1 and (old & (1 << color[v])) == 0:
                # vertex was coloured, revert
                color[v] = -1

    def dfs(colored_cnt: int) -> bool:
        if colored_cnt == n:
            return True
        # MRV: choose uncoloured vertex with smallest domain
        best_v = -1
        best_sz = 4
        for v in range(n):
            if color[v] == -1:
                sz = popcnt(mask[v])
                if sz < best_sz:
                    best_sz = sz
                    best_v = v
                    if sz == 1:
                        break
        if best_v == -1 or best_sz == 0:
            return False
        cur_mask = mask[best_v]
        for c in range(3):
            if cur_mask & (1 << c):
                stack_len = len(changes)
                if assign(best_v, c):
                    if dfs(colored_cnt + 1):
                        return True
                undo(stack_len)
        return False

    possible = dfs(0)
    if not possible:
        print("NO")
    else:
        print("YES")
        # convert 0/1/2 to 1/2/3
        print(' '.join(str(color[i] + 1) for i in range(n)))

if __name__ == "__main__":
    solve()