import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    adj_mask = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            print("NO")
            return
        if not ((adj_mask[u] >> v) & 1):
            adj[u].append(v)
            adj[v].append(u)
            adj_mask[u] |= 1 << v
            adj_mask[v] |= 1 << u

    sys.setrecursionlimit(1000000)

    col = [0] * n          # 0 uncolored, otherwise bit color
    dom = [7] * n          # available colors as bit mask
    history = []           # undo stack

    def restore(target_len):
        while len(history) > target_len:
            rec = history.pop()
            if len(rec) == 3:
                v, old_col, old_dom = rec
                col[v] = old_col
                dom[v] = old_dom
            else:
                u, c = rec
                dom[u] |= c

    def assign(v, c):
        # c is a single bit (1, 2 or 4)
        if col[v] != 0:
            return col[v] == c
        if not (dom[v] & c):
            return False
        history.append((v, col[v], dom[v]))
        col[v] = c
        dom[v] = 0
        stack = [v]
        while stack:
            x = stack.pop()
            cx = col[x]
            for u in adj[x]:
                if col[u] == 0 and (dom[u] & cx):
                    history.append((u, cx))
                    dom[u] &= ~cx
                    if dom[u] == 0:
                        return False
                    if dom[u].bit_count() == 1:
                        fc = dom[u]
                        history.append((u, col[u], dom[u]))
                        col[u] = fc
                        dom[u] = 0
                        stack.append(u)
        return True

    def decision_dfs():
        # choose uncolored vertex with smallest domain size
        v = -1
        best = 4
        best_deg = -1
        for i in range(n):
            if col[i] == 0:
                sz = dom[i].bit_count()
                deg = len(adj[i])
                if sz < best or (sz == best and deg > best_deg):
                    best = sz
                    v = i
                    best_deg = deg
        if v == -1:
            return True
        if best == 0:
            return False
        mask = dom[v]
        for c in (1, 2, 4):
            if mask & c:
                hlen = len(history)
                if assign(v, c):
                    if decision_dfs():
                        return True
                restore(hlen)
        return False

    # decision check: fix vertex 0 to color 1 by symmetry of colors
    if not assign(0, 1):
        print("NO")
        return
    if not decision_dfs():
        print("NO")
        return

    # reset for lexicographically smallest search
    col = [0] * n
    dom = [7] * n
    history.clear()
    answer = None

    def lex_dfs():
        nonlocal answer
        v = -1
        for i in range(n):
            if col[i] == 0:
                v = i
                break
        if v == -1:
            answer = col[:]
            return True
        mask = dom[v]
        for c in (1, 2, 4):
            if mask & c:
                hlen = len(history)
                if assign(v, c):
                    if lex_dfs():
                        return True
                restore(hlen)
        return False

    if not lex_dfs():
        print("NO")
        return

    out = ' '.join(str(c.bit_length()) for c in answer)
    print("YES")
    print(out)

if __name__ == "__main__":
    solve()