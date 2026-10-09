import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neighbors = [[] for _ in range(n)]
    bad = False
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            bad = True
        else:
            neighbors[u].append(v)
            neighbors[v].append(u)

    if bad:
        sys.stdout.write("NO")
        return

    color = [-1] * n
    domain = [7] * n  # bits 0,1,2 correspond to grids 1,2,3
    ans = None

    def assign(v, c, changed):
        color[v] = c
        old = domain[v]
        domain[v] = 1 << c
        changed.append((v, old))
        q = [v]
        while q:
            x = q.pop()
            cx = color[x]
            mask = 1 << cx
            for u in neighbors[x]:
                if color[u] != -1:
                    continue
                if domain[u] & mask:
                    nd = domain[u] & ~mask
                    if nd == 0:
                        return False
                    oldd = domain[u]
                    domain[u] = nd
                    changed.append((u, oldd))
                    if nd & (nd - 1) == 0:
                        cu = nd.bit_length() - 1
                        color[u] = cu
                        q.append(u)
        return True

    sys.setrecursionlimit(10000)

    def dfs(i):
        nonlocal ans
        if ans is not None:
            return True
        while i < n and color[i] != -1:
            i += 1
        if i == n:
            ans = color.copy()
            return True
        dom = domain[i]
        for c in (0, 1, 2):
            if dom & (1 << c):
                changed = []
                if assign(i, c, changed):
                    if dfs(i + 1):
                        return True
                for v, old in reversed(changed):
                    color[v] = -1
                    domain[v] = old
        return False

    if dfs(0):
        sys.stdout.write("YES\n")
        sys.stdout.write(' '.join(str(c + 1) for c in ans))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()