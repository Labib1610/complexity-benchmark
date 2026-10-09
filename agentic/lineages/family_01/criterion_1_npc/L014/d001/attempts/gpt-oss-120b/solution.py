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
        if u == v:
            continue
        adj[u].append(v)
        adj[v].append(u)

    # order vertices by decreasing degree (stronger constraints first)
    order = sorted(range(n), key=lambda x: -len(adj[x]))

    colour = [0] * n               # 0 = uncoloured, else 1..3
    allowed = [7] * n               # bitmask 0b111 : all three colours possible

    # depth‑first search with backtracking
    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = order[pos]
        mask = allowed[v]
        while mask:
            low = mask & -mask
            c = low.bit_length()          # colour number 1..3
            mask ^= low

            colour[v] = c
            bit = 1 << (c - 1)
            changed = []                   # (vertex, previous_allowed)

            conflict = False
            for u in adj[v]:
                if colour[u] == 0:          # only affect still uncoloured neighbours
                    if allowed[u] & bit:
                        prev = allowed[u]
                        allowed[u] = prev & ~bit
                        changed.append((u, prev))
                        if allowed[u] == 0:
                            conflict = True
                            break
            if not conflict:
                if dfs(pos + 1):
                    return True

            # undo changes
            for u, prev in changed:
                allowed[u] = prev
            colour[v] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(colour[i]) for i in range(n))]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()