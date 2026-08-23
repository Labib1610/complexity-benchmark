import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    # connected components
    visited = [False] * n
    components = []
    for i in range(n):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            comp = []
            while stack:
                v = stack.pop()
                comp.append(v)
                for u in adj[v]:
                    if not visited[u]:
                        visited[u] = True
                        stack.append(u)
            comp.sort()
            components.append(comp)

    color = [0] * n          # 0 = uncolored, 1..3 = hopper
    avail = [7] * n          # bitmask of allowed colors

    def assign(v: int, c: int, changes: list) -> bool:
        """Assign color c to v, propagate forced singleton assignments.
           Append undo records to changes. Return False on contradiction."""
        stack = [(v, c)]
        while stack:
            x, col = stack.pop()
            if color[x] != 0:
                if color[x] == col:
                    continue
                return False
            bit = 1 << (col - 1)
            if not (avail[x] & bit):
                return False
            color[x] = col
            changes.append((0, x, col))
            for y in adj[x]:
                if color[y] == 0:
                    old = avail[y]
                    new = avail[y] & ~bit
                    if new == old:
                        continue
                    avail[y] = new
                    changes.append((1, y, old))
                    if new == 0:
                        return False
                    if new & (new - 1) == 0:
                        stack.append((y, new.bit_length()))
        return True

    def undo(changes: list) -> None:
        for typ, x, val in reversed(changes):
            if typ == 0:
                color[x] = 0
            else:
                avail[x] = val

    sys.setrecursionlimit(10000)

    def dfs(comp: list, idx: int) -> bool:
        while idx < len(comp) and color[comp[idx]] != 0:
            idx += 1
        if idx == len(comp):
            return True
        v = comp[idx]
        bits = avail[v]
        for c in (1, 2, 3):
            if bits & (1 << (c - 1)):
                changes = []
                if assign(v, c, changes):
                    if dfs(comp, idx + 1):
                        return True
                undo(changes)
        return False

    for comp in components:
        changes = []
        # For an isolated component the smallest vertex can be fixed to 1
        # because colors are symmetric.
        if not assign(comp[0], 1, changes):
            print("NO")
            return
        if not dfs(comp, 1):
            print("NO")
            return

    print("YES")
    sys.stdout.write(' '.join(str(c) for c in color))

solve()