import sys

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

    # residues: 0 -> value 3, 1 -> value 1, 2 -> value 2
    # allowed_mask[r] : bitmask of residues s such that (r, s) is allowed
    allowed_mask = [0] * 3
    for r in range(3):
        mask = 0
        for s in range(3):
            if (r + 2 * s) % 3 != 0:   # allowed
                mask |= 1 << s
        allowed_mask[r] = mask

    color = [-1] * n               # -1 = unassigned, else residue 0..2
    possible = [0b111] * n         # three bits set

    sys.setrecursionlimit(10000)

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = pos
        # try residues in order 0,1,2 (values 3,1,2) but we need lexicographic on values 1,2,3
        # mapping: residue 0 -> value 3, residue 1 -> value 1, residue 2 -> value 2
        # lexicographic on values means order 1,2,3 i.e. residues 1,2,0
        for r in (1, 2, 0):
            if not (possible[v] >> r) & 1:
                continue
            # compatibility with already coloured neighbours
            ok = True
            for w in adj[v]:
                cw = color[w]
                if cw != -1:
                    if (r + 2 * cw) % 3 == 0:
                        ok = False
                        break
            if not ok:
                continue

            saved = []
            consistent = True
            for w in adj[v]:
                if color[w] == -1:
                    old = possible[w]
                    new = old & allowed_mask[r]
                    if new == 0:
                        consistent = False
                        break
                    if new != old:
                        saved.append((w, old))
                        possible[w] = new
            if not consistent:
                for w, old in saved:
                    possible[w] = old
                continue

            color[v] = r
            if dfs(pos + 1):
                return True
            color[v] = -1
            for w, old in saved:
                possible[w] = old
        return False

    if dfs(0):
        # translate residues to required values 1,2,3
        out = []
        for r in color:
            if r == 0:
                out.append('3')
            elif r == 1:
                out.append('1')
            else:
                out.append('2')
        sys.stdout.write("YES\n")
        sys.stdout.write(' '.join(out))
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()