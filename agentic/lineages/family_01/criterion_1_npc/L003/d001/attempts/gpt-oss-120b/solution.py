import sys

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

    color = [0] * n               # 0 = uncoloured, else 1..3
    mask = [0b111] * n            # possible colours bitmask

    sys.setrecursionlimit(10000)

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = pos
        # try colours 1,2,3
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (mask[v] & bit):
                continue

            # assign c to v
            saved = []                     # (vertex, old_mask)
            color[v] = c
            old_mask_v = mask[v]
            mask[v] = bit

            ok = True
            for u in adj[v]:
                if color[u]:
                    if color[u] == c:
                        ok = False
                        break
                    continue
                if mask[u] & bit:
                    new_mask = mask[u] & ~bit
                    saved.append((u, mask[u]))
                    mask[u] = new_mask
                    if new_mask == 0:
                        ok = False
                        break

            if ok and dfs(pos + 1):
                return True

            # backtrack
            for u, old in reversed(saved):
                mask[u] = old
            mask[v] = old_mask_v
            color[v] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c) for c in color)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()