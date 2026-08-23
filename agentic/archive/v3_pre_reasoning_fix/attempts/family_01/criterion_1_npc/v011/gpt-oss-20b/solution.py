import sys

def solve() -> None:
    sys.setrecursionlimit(1000000)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if v not in adj[u]:
            adj[u].add(v)
            adj[v].add(u)

    color = [0] * n          # 0 = uncolored, else 1..3
    avail = [0b111] * n      # bitmask of available colors for each vertex

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = pos
        for c in (1, 2, 3):
            if not (avail[v] & (1 << (c - 1))):
                continue
            # Tentatively assign color c
            color[v] = c
            changed = []
            conflict = False
            for u in adj[v]:
                if color[u] == 0:
                    new_mask = avail[u] & ~(1 << (c - 1))
                    if new_mask == 0:
                        conflict = True
                        break
                    if new_mask != avail[u]:
                        changed.append((u, avail[u]))
                        avail[u] = new_mask
            if not conflict:
                if dfs(pos + 1):
                    return True
            # Undo changes
            for u, old_mask in reversed(changed):
                avail[u] = old_mask
            color[v] = 0
        return False

    if dfs(0):
        out_lines = ["YES", " ".join(str(x) for x in color)]
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()