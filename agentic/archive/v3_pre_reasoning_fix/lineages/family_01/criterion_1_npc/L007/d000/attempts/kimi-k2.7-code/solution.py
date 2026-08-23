import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_mask = [0] * n
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            sys.stdout.write("NO\n")
            return
        if not ((adj_mask[u] >> v) & 1):
            adj_mask[u] |= 1 << v
            adj_mask[v] |= 1 << u
            neighbors[u].append(v)
            neighbors[v].append(u)

    deg = [len(neighbors[i]) for i in range(n)]

    def feasible(init_color):
        color = init_color[:]
        allowed = [7] * n
        stack = []
        for v in range(n):
            c = color[v]
            if c != -1:
                allowed[v] = 1 << c
                stack.append(v)

        def propagate(st, mod):
            while st:
                v = st.pop()
                c = color[v]
                if not (allowed[v] & (1 << c)):
                    return False
                for u in neighbors[v]:
                    if color[u] == -1:
                        mask = 1 << c
                        if allowed[u] & mask:
                            mod.append((u, allowed[u], color[u]))
                            allowed[u] &= ~mask
                            if allowed[u] == 0:
                                return False
                            if allowed[u] & (allowed[u] - 1) == 0:
                                newc = allowed[u].bit_length() - 1
                                color[u] = newc
                                st.append(u)
                    elif color[u] == c:
                        return False
            return True

        if not propagate(stack, []):
            return False

        def dfs():
            v = -1
            mincnt = 4
            for i in range(n):
                if color[i] == -1:
                    cnt = allowed[i].bit_count()
                    if v == -1 or cnt < mincnt or (cnt == mincnt and deg[i] > deg[v]):
                        mincnt = cnt
                        v = i
            if v == -1:
                return True
            opts = allowed[v]
            o = opts
            while o:
                lsb = o & -o
                c = lsb.bit_length() - 1
                mod = [(v, allowed[v], color[v])]
                color[v] = c
                allowed[v] = 1 << c
                if propagate([v], mod) and dfs():
                    return True
                for u, old_a, old_c in mod:
                    allowed[u] = old_a
                    color[u] = old_c
                o ^= lsb
            return False

        return dfs()

    colors = [-1] * n
    for i in range(n):
        chosen = -1
        for c in (0, 1, 2):
            conflict = False
            for u in neighbors[i]:
                if colors[u] == c:
                    conflict = True
                    break
            if conflict:
                continue
            colors[i] = c
            if feasible(colors):
                chosen = c
                break
            colors[i] = -1
        if chosen == -1:
            sys.stdout.write("NO\n")
            return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(c + 1) for c in colors))
    sys.stdout.write("\n")

if __name__ == "__main__":
    solve()