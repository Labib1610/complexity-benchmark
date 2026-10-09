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
        adj[u].append(v)
        adj[v].append(u)

    # domain masks: bit 0 -> colour 0 (phase 1), etc.
    domains = [0b111] * n
    colour = [-1] * n          # -1 = unassigned, else 0..2

    # ---------- propagation ----------
    def propagate(changes):
        """unit propagation, record all modifications in changes,
           return False if a conflict appears."""
        while True:
            progress = False
            for v in range(n):
                if colour[v] == -1 and (domains[v] & (domains[v] - 1)) == 0:
                    # exactly one possible colour
                    c = (domains[v].bit_length() - 1)
                    # record old state
                    changes.append((v, domains[v], colour[v]))
                    domains[v] = 1 << c
                    colour[v] = c
                    for u in adj[v]:
                        if colour[u] == -1 and (domains[u] & (1 << c)):
                            changes.append((u, domains[u], colour[u]))
                            domains[u] &= ~(1 << c)
                            if domains[u] == 0:
                                return False
                    progress = True
            if not progress:
                break
        return True

    # ---------- depth‑first search ----------
    def dfs() -> bool:
        # all coloured ?
        if all(col != -1 for col in colour):
            return True

        # choose vertex with smallest domain (>1)
        v = -1
        best = 4
        for i in range(n):
            if colour[i] == -1:
                sz = bin(domains[i]).count('1')
                if sz < best:
                    best = sz
                    v = i
                    if sz == 2:   # cannot be 1 because then it would be forced
                        pass
        mask = domains[v]
        for c in range(3):
            if mask & (1 << c):
                changes = []
                # assign v = c
                changes.append((v, domains[v], colour[v]))
                domains[v] = 1 << c
                colour[v] = c
                conflict = False
                for u in adj[v]:
                    if colour[u] == -1 and (domains[u] & (1 << c)):
                        changes.append((u, domains[u], colour[u]))
                        domains[u] &= ~(1 << c)
                        if domains[u] == 0:
                            conflict = True
                            break
                if not conflict and propagate(changes):
                    if dfs():
                        return True
                # backtrack
                for vertex, old_mask, old_col in reversed(changes):
                    domains[vertex] = old_mask
                    colour[vertex] = old_col
        return False

    possible = dfs()
    out = []
    if possible:
        out.append("YES")
        out.append(' '.join(str(colour[i] + 1) for i in range(n)))
    else:
        out.append("NO")
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()