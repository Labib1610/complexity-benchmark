import sys
from itertools import combinations

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
        if u == v:
            sys.stdout.write("NO")
            return
        if not ((adj[u] >> v) & 1):
            adj[u] |= 1 << v
            adj[v] |= 1 << u
            adj_list[u].append(v)
            adj_list[v].append(u)

    # A K4 makes 3-coloring impossible.
    if m >= 6 and n >= 4:
        for quad in combinations(range(n), 4):
            mask = (1 << quad[0]) | (1 << quad[1]) | (1 << quad[2]) | (1 << quad[3])
            ok = True
            for v in quad:
                if (adj[v] & mask) != (mask ^ (1 << v)):
                    ok = False
                    break
            if ok:
                sys.stdout.write("NO")
                return

    domains = [7] * n      # bit 0 -> color 1, bit 1 -> color 2, bit 2 -> color 3
    assign = [0] * n       # 0 unassigned, otherwise 1/2/3
    sys.setrecursionlimit(10000)

    # The subgraph of vertices that cannot use color 1 must be bipartite
    # (they can only use colors 2 and 3).
    def check_h1() -> bool:
        in_s = [False] * n
        side = [-1] * n
        for v in range(n):
            a = assign[v]
            if a:
                col = a - 1
                if col == 0:
                    continue
                in_s[v] = True
                side[v] = col - 1          # color 2 -> side 0, color 3 -> side 1
            else:
                d = domains[v]
                if d & 1:                  # can still use color 1
                    continue
                in_s[v] = True
                if d == 2:                 # only color 2
                    side[v] = 0
                elif d == 4:               # only color 3
                    side[v] = 1

        visited = [False] * n
        for s in range(n):
            if not in_s[s] or visited[s]:
                continue
            stack = [s]
            visited[s] = True
            if side[s] == -1:
                side[s] = 0
            while stack:
                v = stack.pop()
                sv = side[v]
                for u in adj_list[v]:
                    if not in_s[u]:
                        continue
                    if side[u] == -1:
                        side[u] = 1 - sv
                    elif side[u] == sv:
                        return False
                    if not visited[u]:
                        visited[u] = True
                        stack.append(u)
        return True

    def propagate(v: int, c: int, changes: list) -> bool:
        stack = [(v, c)]
        bit = 1 << c
        while stack:
            v, c = stack.pop()
            a = assign[v]
            if a:
                if a - 1 == c:
                    continue
                return False
            if not (domains[v] & bit):
                return False
            changes.append((v, domains[v]))
            assign[v] = c + 1
            domains[v] = 0

            for u in adj_list[v]:
                au = assign[u]
                if au:
                    if au - 1 == c:
                        return False
                    continue
                if domains[u] & bit:
                    changes.append((u, domains[u]))
                    domains[u] &= ~bit
                    if domains[u] == 0:
                        return False
                    # single remaining color -> force it
                    if domains[u] & (domains[u] - 1) == 0:
                        c2 = domains[u].bit_length() - 1
                        stack.append((u, c2))
        return check_h1()

    def dfs(pos: int) -> bool:
        while pos < n and assign[pos]:
            pos += 1
        if pos == n:
            return True
        d = domains[pos]
        for c in (0, 1, 2):
            if d & (1 << c):
                changes = []
                if propagate(pos, c, changes):
                    if dfs(pos + 1):
                        return True
                for v, old in changes:
                    domains[v] = old
                    if old:
                        assign[v] = 0
        return False

    if dfs(0):
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, assign)))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()