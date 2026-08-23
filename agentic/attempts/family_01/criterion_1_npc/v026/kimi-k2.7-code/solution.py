import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    nbr = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            print("NO")
            return
        nbr[u].append(v)
        nbr[v].append(u)

    colors = [-1] * n
    forbidden = [0] * n
    uncolored_mask = (1 << n) - 1
    stack = []
    sys.setrecursionlimit(10000)

    def color_vertex(v, c):
        nonlocal uncolored_mask
        for u in nbr[v]:
            if colors[u] == c:
                return False
        stack.append(('c', v, colors[v], forbidden[v], uncolored_mask))
        colors[v] = c
        uncolored_mask &= ~(1 << v)
        for u in nbr[v]:
            if colors[u] == -1:
                old = forbidden[u]
                new = old | (1 << c)
                if new != old:
                    stack.append(('f', u, old))
                    forbidden[u] = new
                    if new == 7:
                        return False
                    if new.bit_count() == 2:
                        miss = (new ^ 7).bit_length() - 1
                        if not color_vertex(u, miss):
                            return False
        return True

    def undo(to_len):
        nonlocal uncolored_mask
        while len(stack) > to_len:
            typ = stack.pop()
            if typ[0] == 'c':
                _, v, oldc, oldf, oldmask = typ
                colors[v] = oldc
                forbidden[v] = oldf
                uncolored_mask = oldmask
            else:
                _, u, oldf = typ
                forbidden[u] = oldf

    def dfs():
        if uncolored_mask == 0:
            return True
        v = (uncolored_mask & -uncolored_mask).bit_length() - 1
        forb = forbidden[v]
        for c in range(3):
            if (forb >> c) & 1:
                continue
            saved = len(stack)
            if color_vertex(v, c) and dfs():
                return True
            undo(saved)
        return False

    if dfs():
        print("YES")
        print(' '.join(str(colors[i] + 1) for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()