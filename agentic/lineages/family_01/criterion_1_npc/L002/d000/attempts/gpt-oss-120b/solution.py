import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
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
            continue
        adj[u].append(v)
        adj[v].append(u)

    ALL = 0b111  # bits 0,1,2 -> colours 1,2,3
    domains = [ALL] * n
    col = [0] * n          # 0 = uncoloured, else 1..3

    # ---------- propagation ----------
    def propagate(queue, dom, col):
        while queue:
            v = queue.pop()
            mask = dom[v]
            # mask is guaranteed to be a power of two
            colour = (mask & -mask).bit_length() - 1   # 0,1,2
            col[v] = colour + 1
            for u in adj[v]:
                if col[u]:
                    continue
                if dom[u] & (1 << colour):
                    dom[u] &= ~(1 << colour)
                    if dom[u] == 0:
                        return False
                    if dom[u].bit_count() == 1:
                        queue.append(u)
        return True

    # ---------- backtracking ----------
    def search(dom, col):
        # check for completion / dead end
        unassigned = -1
        min_sz = 4
        for i in range(n):
            if col[i]:
                continue
            sz = dom[i].bit_count()
            if sz == 0:
                return None
            if sz < min_sz:
                min_sz = sz
                unassigned = i
                if sz == 1:
                    break
        if unassigned == -1:          # all coloured
            return col

        v = unassigned
        possible = dom[v]
        # try colours in arbitrary order
        for c in range(3):
            if not (possible & (1 << c)):
                continue
            ndom = dom[:]
            ncol = col[:]
            ndom[v] = 1 << c
            queue = [v]
            if not propagate(queue, ndom, ncol):
                continue
            res = search(ndom, ncol)
            if res is not None:
                return res
        return None

    answer = search(domains, col)
    out = sys.stdout
    if answer is None:
        out.write("NO\n")
    else:
        out.write("YES\n")
        out.write(" ".join(str(x) for x in answer) + "\n")

if __name__ == "__main__":
    solve()