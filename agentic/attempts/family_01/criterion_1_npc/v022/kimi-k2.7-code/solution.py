import sys

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_sets = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj_sets[u].add(v)
        adj_sets[v].add(u)

    adj = [list(s) for s in adj_sets]
    degree = [len(a) for a in adj]

    def propagate(color, sat, uncolored, stack):
        color = color.copy()
        sat = sat.copy()
        while stack:
            x, cx = stack.pop()
            if color[x] != -1:
                if color[x] == cx:
                    continue
                return None
            if sat[x] & (1 << cx):
                return None
            color[x] = cx
            uncolored -= 1
            for u in adj[x]:
                if color[u] == -1:
                    old = sat[u]
                    new = old | (1 << cx)
                    if new == old:
                        continue
                    sat[u] = new
                    if new == 7:
                        return None
                    if new == 6:
                        stack.append((u, 0))
                    elif new == 5:
                        stack.append((u, 1))
                    elif new == 3:
                        stack.append((u, 2))
        return color, sat, uncolored

    def dfs(color, sat, uncolored):
        if uncolored == 0:
            return color
        for v in range(n):
            if color[v] == -1 and sat[v] == 7:
                return None
        best = -1
        best_sat = -1
        for v in range(n):
            if color[v] == -1:
                pc = sat[v].bit_count()
                if pc > best_sat:
                    best_sat = pc
                    best = v
        v = best
        avail = (~sat[v]) & 7
        for c in (0, 1, 2):
            if avail & (1 << c):
                res = propagate(color, sat, uncolored, [(v, c)])
                if res is not None:
                    ans = dfs(res[0], res[1], res[2])
                    if ans is not None:
                        return ans
        return None

    def can_color(fixed):
        color = fixed[:]
        sat = [0] * n
        uncolored = n
        for v in range(n):
            cv = color[v]
            if cv != -1:
                uncolored -= 1
                for u in adj[v]:
                    if color[u] == -1:
                        sat[u] |= 1 << cv
                    elif color[u] == cv:
                        return None
        stack = []
        for v in range(n):
            if color[v] == -1:
                s = sat[v]
                if s == 7:
                    return None
                if s == 6:
                    stack.append((v, 0))
                elif s == 5:
                    stack.append((v, 1))
                elif s == 3:
                    stack.append((v, 2))
        res = propagate(color, sat, uncolored, stack)
        if res is None:
            return None
        return dfs(res[0], res[1], res[2])

    ans = can_color([-1] * n)
    if ans is None:
        sys.stdout.write("NO")
        return

    fixed = [-1] * n
    for i in range(n):
        cur = ans[i]
        chosen = cur
        for c in range(cur):
            fixed[i] = c
            new = can_color(fixed)
            if new is not None:
                ans = new
                chosen = c
                break
        else:
            fixed[i] = cur

    out = []
    out.append("YES")
    out.append(' '.join(str(c + 1) for c in fixed))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()