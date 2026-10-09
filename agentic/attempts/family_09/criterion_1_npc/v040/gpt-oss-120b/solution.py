import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    ALL = (1 << n) - 1
    # complement adjacency (including self‑loops removed)
    cadj = [ALL ^ (adj[i] | (1 << i)) for i in range(n)]

    solution_mask = 0
    found = False

    # ---------- greedy coloring, returns (verts, colours) ----------
    def greedy_color(P_mask: int):
        verts = []
        colours = []
        available = P_mask
        colour = 0
        while available:
            colour += 1
            cur = available
            colour_mask = 0
            while cur:
                v = (cur & -cur).bit_length() - 1
                cur &= cur - 1
                verts.append(v)
                colours.append(colour)
                colour_mask |= 1 << v
                # remove neighbours of v (in complement) from cur
                cur &= ~ (cadj[v] | (1 << v))
            # vertices coloured this round are removed from further rounds
            available &= ~colour_mask
        return verts, colours

    # ---------- recursive search ----------
    def dfs(R_mask: int, P_mask: int, size: int):
        nonlocal solution_mask, found
        if found:
            return True
        if size == k:
            solution_mask = R_mask
            found = True
            return True

        verts, colours = greedy_color(P_mask)
        # iterate in reverse order (most promising first)
        for i in range(len(verts) - 1, -1, -1):
            if size + colours[i] < k:          # bound, cannot reach k
                return False
            v = verts[i]
            newR = R_mask | (1 << v)
            newP = P_mask & cadj[v]
            if size + 1 == k:
                solution_mask = newR
                found = True
                return True
            if dfs(newR, newP, size + 1):
                return True
            # discard v from P for the next iterations
            P_mask &= ~(1 << v)
        return False

    dfs(0, ALL, 0)

    out = []
    if found:
        out.append("YES")
        ans = [str(i + 1) for i in range(n) if (solution_mask >> i) & 1]
        out.append(" ".join(ans))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()