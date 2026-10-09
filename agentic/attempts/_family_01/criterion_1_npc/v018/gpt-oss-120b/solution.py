import sys

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

    # possible colors mask for each vertex (bits 0,1,2 for colors 1,2,3)
    poss = [0b111] * n
    assign = [-1] * n
    unassigned = set(range(n))

    # precompute popcount for 0..7
    popcnt = [bin(i).count('1') for i in range(8)]

    sys.setrecursionlimit(10000)

    def dfs(assigned_cnt: int) -> bool:
        if assigned_cnt == n:
            return True
        # choose vertex with smallest domain (>0)
        v = min(unassigned, key=lambda x: popcnt[poss[x]])
        domain = poss[v]
        if domain == 0:
            return False
        # try each possible color
        for c in range(3):
            if not (domain >> c) & 1:
                continue
            # assign color c to v
            assign[v] = c
            unassigned.remove(v)
            # record changes to revert later
            changes = []
            mask_c = 1 << c
            neigh_mask = adj[v]
            u = 0
            while neigh_mask:
                lsb = neigh_mask & -neigh_mask
                u = (lsb.bit_length() - 1)
                if assign[u] == -1 and (poss[u] & mask_c):
                    old = poss[u]
                    new = old & ~mask_c
                    changes.append((u, old))
                    poss[u] = new
                neigh_mask ^= lsb
            # recurse
            if dfs(assigned_cnt + 1):
                return True
            # revert
            for u, old in reversed(changes):
                poss[u] = old
            assign[v] = -1
            unassigned.add(v)
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c + 1) for c in assign)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()