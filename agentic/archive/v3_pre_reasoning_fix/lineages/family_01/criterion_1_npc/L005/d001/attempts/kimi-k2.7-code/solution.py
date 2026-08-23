import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    deg = [0] * n
    bad = False
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            bad = True
        else:
            adj[u].append(v)
            adj[v].append(u)
            deg[u] += 1
            deg[v] += 1
    if bad:
        print("NO")
        return

    FULL = 7  # bits for colors 1,2,3

    def assign(col, dom, v, c, undo):
        if col[v]:
            return col[v] == c
        if not (dom[v] & c):
            return False
        undo.append((v, 0, dom[v]))
        col[v] = c
        dom[v] = c
        stack = [v]
        while stack:
            x = stack.pop()
            cx = col[x]
            for u in adj[x]:
                if col[u] == 0:
                    if dom[u] & cx:
                        old = dom[u]
                        new = old & ~cx
                        if new == 0:
                            return False
                        dom[u] = new
                        undo.append((u, 0, old))
                        if new & (new - 1) == 0:
                            col[u] = new
                            dom[u] = new
                            undo.append((u, 0, new))
                            stack.append(u)
        return True

    def revert(col, dom, undo, target):
        while len(undo) > target:
            u, oc, od = undo.pop()
            col[u] = oc
            dom[u] = od

    sys.setrecursionlimit(10000)

    def search(col, dom):
        v = -1
        best_sz = 4
        best_deg = -1
        for i in range(n):
            if col[i] == 0:
                sz = dom[i].bit_count()
                if sz == 0:
                    return False
                if sz < best_sz or (sz == best_sz and deg[i] > best_deg):
                    best_sz = sz
                    best_deg = deg[i]
                    v = i
        if v == -1:
            return True
        mask = dom[v]
        cbit = 1
        while cbit <= 4:
            if mask & cbit:
                undo = []
                if assign(col, dom, v, cbit, undo):
                    if search(col, dom):
                        revert(col, dom, undo, 0)
                        return True
                revert(col, dom, undo, 0)
            cbit <<= 1
        return False

    color = [0] * n
    domain = [FULL] * n
    for i in range(n):
        if color[i]:
            continue
        found = False
        for cbit in (1, 2, 4):
            if not (domain[i] & cbit):
                continue
            col = color[:]
            dom = domain[:]
            if assign(col, dom, i, cbit, []):
                if search(col, dom):
                    color = col
                    domain = dom
                    found = True
                    break
        if not found:
            print("NO")
            return

    out = [str(color[i].bit_length()) for i in range(n)]
    print("YES")
    print(" ".join(out))

if __name__ == "__main__":
    solve()