import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            neighbors[u].append(u)
        else:
            neighbors[u].append(v)
            neighbors[v].append(u)

    color = [0] * n          # 0 = uncolored, otherwise 1..3
    allowed = [7] * n        # bit mask of allowed colors, 1,2,4
    history = []             # undo stack
    bit_to_col = {1: 1, 2: 2, 4: 3}
    sys.setrecursionlimit(10000)

    def set_color(v, cbit):
        if not (allowed[v] & cbit):
            return False
        history.append(('c', v, color[v], allowed[v]))
        color[v] = bit_to_col[cbit]
        allowed[v] = cbit
        stack = [v]
        while stack:
            x = stack.pop()
            cx = color[x]
            bit = 1 << (cx - 1)
            for u in neighbors[x]:
                cu = color[u]
                if cu:
                    if cu == cx:
                        return False
                    continue
                if allowed[u] & bit:
                    history.append(('a', u, allowed[u]))
                    allowed[u] &= ~bit
                    if allowed[u] == 0:
                        return False
                    # forced to a single remaining color
                    if allowed[u] & (allowed[u] - 1) == 0:
                        history.append(('c', u, color[u], allowed[u]))
                        color[u] = bit_to_col[allowed[u]]
                        stack.append(u)
        return True

    def check_2sat():
        # Variables are uncolored vertices with exactly two allowed colors.
        var_id = [-1] * n
        col_order = []
        vid = 0
        for i in range(n):
            if color[i] == 0:
                a = allowed[i]
                if a == 3 or a == 5 or a == 6:
                    var_id[i] = vid
                    cols = []
                    if a & 1:
                        cols.append(1)
                    if a & 2:
                        cols.append(2)
                    if a & 4:
                        cols.append(4)
                    col_order.append(cols)
                    vid += 1
        if vid == 0:
            return True
        size = 2 * vid
        g = [[] for _ in range(size)]

        def add_imp(i, j):
            g[i].append(j)

        # exactly-one constraints for each variable
        for i in range(vid):
            t = 2 * i
            f = t + 1
            add_imp(t, f ^ 1)      # t -> not f
            add_imp(f, t ^ 1)      # f -> not t
            add_imp(t ^ 1, f)      # not t -> f
            add_imp(f ^ 1, t)      # not f -> t

        # edge constraints
        for u in range(n):
            uid = var_id[u]
            if uid == -1:
                continue
            cu1, cu2 = col_order[uid]
            for v in neighbors[u]:
                if u > v:
                    continue
                vidv = var_id[v]
                if vidv == -1:
                    continue
                cv1, cv2 = col_order[vidv]
                inter = allowed[u] & allowed[v]
                if inter & 1:
                    lu = uid * 2 + (0 if cu1 == 1 else 1)
                    lv = vidv * 2 + (0 if cv1 == 1 else 1)
                    add_imp(lu, lv ^ 1)
                    add_imp(lv, lu ^ 1)
                if inter & 2:
                    lu = uid * 2 + (0 if cu1 == 2 else 1)
                    lv = vidv * 2 + (0 if cv1 == 2 else 1)
                    add_imp(lu, lv ^ 1)
                    add_imp(lv, lu ^ 1)
                if inter & 4:
                    lu = uid * 2 + (0 if cu1 == 4 else 1)
                    lv = vidv * 2 + (0 if cv1 == 4 else 1)
                    add_imp(lu, lv ^ 1)
                    add_imp(lv, lu ^ 1)

        index = 0
        stack = []
        onstack = [False] * size
        indices = [-1] * size
        low = [0] * size
        comp = [-1] * size
        comp_cnt = 0

        def strongconnect(v):
            nonlocal index, comp_cnt
            indices[v] = index
            low[v] = index
            index += 1
            stack.append(v)
            onstack[v] = True
            for w in g[v]:
                if indices[w] == -1:
                    strongconnect(w)
                    if low[w] < low[v]:
                        low[v] = low[w]
                elif onstack[w]:
                    if indices[w] < low[v]:
                        low[v] = indices[w]
            if low[v] == indices[v]:
                while True:
                    w = stack.pop()
                    onstack[w] = False
                    comp[w] = comp_cnt
                    if w == v:
                        break
                comp_cnt += 1

        for v in range(size):
            if indices[v] == -1:
                strongconnect(v)

        for i in range(vid):
            if comp[2 * i] == comp[2 * i + 1]:
                return False
        return True

    def dfs():
        v = -1
        for i in range(n):
            if color[i] == 0:
                v = i
                break
        if v == -1:
            return True
        av = allowed[v]
        for cbit in (1, 2, 4):
            if av & cbit:
                history.append('mark')
                if set_color(v, cbit) and check_2sat():
                    if dfs():
                        return True
                while history[-1] != 'mark':
                    entry = history.pop()
                    if entry[0] == 'c':
                        _, u, oc, oa = entry
                        color[u] = oc
                        allowed[u] = oa
                    else:
                        _, u, oa = entry
                        allowed[u] = oa
                history.pop()
        return False

    if dfs():
        out = 'YES\n' + ' '.join(str(c) for c in color)
        sys.stdout.write(out)
    else:
        sys.stdout.write('NO')

if __name__ == '__main__':
    solve()