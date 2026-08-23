import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_sets = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        adj_sets[u].add(v)
        adj_sets[v].add(u)
    adj = [list(s) for s in adj_sets]
    deg = [len(adj[i]) for i in range(n + 1)]

    sys.setrecursionlimit(10000)

    def extendable(fixed):
        color = fixed[:]
        sat = [0] * (n + 1)
        uncolored = 0
        for v in range(1, n + 1):
            c = color[v]
            if c:
                bit = 1 << (c - 1)
                for u in adj[v]:
                    if color[u] == 0:
                        sat[u] |= bit
            else:
                uncolored += 1
        for v in range(1, n + 1):
            if color[v] == 0 and sat[v] == 7:
                return False

        stack = []

        def dfs():
            nonlocal uncolored
            if uncolored == 0:
                return True
            best = -1
            best_sat = -1
            best_deg = -1
            for v in range(1, n + 1):
                if color[v] != 0:
                    continue
                sb = sat[v].bit_count()
                d = deg[v]
                if sb > best_sat or (sb == best_sat and d > best_deg):
                    best_sat = sb
                    best_deg = d
                    best = v
            v = best
            forb = sat[v]
            for c in (1, 2, 3):
                bit = 1 << (c - 1)
                if forb & bit:
                    continue
                color[v] = c
                uncolored -= 1
                stack.append(('c', v))
                ok = True
                for u in adj[v]:
                    if color[u] == 0:
                        if not (sat[u] & bit):
                            sat[u] |= bit
                            stack.append(('s', u, bit))
                        if sat[u] == 7:
                            ok = False
                            break
                if ok and dfs():
                    return True
                while stack:
                    typ = stack.pop()
                    if typ[0] == 'c':
                        color[typ[1]] = 0
                        uncolored += 1
                        break
                    else:
                        sat[typ[1]] ^= typ[2]
            return False

        return dfs()

    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        chosen = 0
        for c in (1, 2, 3):
            conflict = False
            for v in adj[i]:
                if ans[v] == c:
                    conflict = True
                    break
            if conflict:
                continue
            ans[i] = c
            if extendable(ans):
                chosen = c
                break
            ans[i] = 0
        if chosen == 0:
            print("NO")
            return

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()