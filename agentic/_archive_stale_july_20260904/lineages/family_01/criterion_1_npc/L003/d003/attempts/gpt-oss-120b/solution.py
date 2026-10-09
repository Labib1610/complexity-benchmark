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

    # possible colours mask: bit0->1, bit1->2, bit2->3
    possible = [0b111] * n
    colour = [0] * n          # final answer, 0 = unassigned

    # depth‑first search
    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        # try colours 1,2,3
        mask = possible[pos]
        for c in range(3):
            bit = 1 << c
            if mask & bit:
                # assign colour c+1
                colour[pos] = c + 1
                # remember changes to neighbours to restore later
                changed = []
                neigh = adj[pos]
                v = 0
                while neigh:
                    lsb = neigh & -neigh
                    v = (lsb.bit_length() - 1)
                    if colour[v] == 0:          # still uncoloured
                        if possible[v] & bit:
                            possible[v] &= ~bit
                            changed.append(v)
                            if possible[v] == 0:
                                # dead end, restore and continue
                                break
                    neigh ^= lsb
                else:
                    # no break -> all neighbours still have a colour
                    if dfs(pos + 1):
                        return True
                # restore
                for v in changed:
                    possible[v] |= bit
                colour[pos] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, colour)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()