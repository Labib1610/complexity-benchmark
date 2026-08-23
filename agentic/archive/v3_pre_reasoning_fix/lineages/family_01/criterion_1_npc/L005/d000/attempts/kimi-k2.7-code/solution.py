import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    adj_list = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        adj_list[u].append(v)
        adj_list[v].append(u)

    sys.setrecursionlimit(10000)

    def is_extendable(col):
        cm = [0, 0, 0, 0]
        colored = 0
        for v in range(n):
            c = col[v]
            if c:
                bit = 1 << v
                if cm[c] & adj[v]:
                    return False
                cm[c] |= bit
                colored |= bit

        def dfs(colored_mask, cm):
            best = -1
            best_sat = -1
            best_deg = -1
            for v in range(n):
                if (colored_mask >> v) & 1:
                    continue
                av = adj[v]
                sat = 0
                if av & cm[1]:
                    sat += 1
                if av & cm[2]:
                    sat += 1
                if av & cm[3]:
                    sat += 1
                if sat == 3:
                    return False
                deg = (av & ~colored_mask).bit_count()
                if sat > best_sat or (sat == best_sat and deg > best_deg):
                    best_sat = sat
                    best_deg = deg
                    best = v
            if best == -1:
                return True

            v = best
            av = adj[v]
            forbidden = 0
            if av & cm[1]:
                forbidden |= 1
            if av & cm[2]:
                forbidden |= 2
            if av & cm[3]:
                forbidden |= 4

            nb = [0, 0, 0, 0]
            for c in (1, 2, 3):
                mask = cm[c]
                umask = 0
                while mask:
                    lsb = mask & -mask
                    u = lsb.bit_length() - 1
                    umask |= adj[u]
                    mask ^= lsb
                nb[c] = umask

            opts = []
            if not (forbidden & 1):
                cnt = (av & ~colored_mask & ~nb[1]).bit_count()
                opts.append((cnt, 1))
            if not (forbidden & 2):
                cnt = (av & ~colored_mask & ~nb[2]).bit_count()
                opts.append((cnt, 2))
            if not (forbidden & 4):
                cnt = (av & ~colored_mask & ~nb[3]).bit_count()
                opts.append((cnt, 3))
            opts.sort()

            vbit = 1 << v
            new_colored = colored_mask | vbit
            for _, c in opts:
                cm[c] |= vbit
                if dfs(new_colored, cm):
                    return True
                cm[c] ^= vbit
            return False

        return dfs(colored, cm)

    if not is_extendable([0] * n):
        sys.stdout.write("NO")
        return

    colors = [0] * n
    for i in range(n):
        chosen = 0
        for c in (1, 2, 3):
            ok = True
            for j in adj_list[i]:
                if j < i and colors[j] == c:
                    ok = False
                    break
            if not ok:
                continue
            colors[i] = c
            if is_extendable(colors):
                chosen = c
                break
            colors[i] = 0
        if chosen == 0:
            sys.stdout.write("NO")
            return

    out = ["YES", " ".join(map(str, colors))]
    sys.stdout.write("\n".join(out))

solve()