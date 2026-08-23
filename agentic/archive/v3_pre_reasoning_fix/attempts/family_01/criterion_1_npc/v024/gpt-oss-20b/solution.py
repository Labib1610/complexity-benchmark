import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    allowed = [0b111] * (n + 1)  # bits 0,1,2 for colors 1,2,3
    assign = [0] * (n + 1)
    found = False

    def dfs(i: int):
        nonlocal found
        if found:
            return
        if i > n:
            found = True
            return
        # try colors in lexicographic order
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if allowed[i] & bit:
                assign[i] = c
                changes = []
                ok = True
                for j in adj[i]:
                    if j > i:
                        cur = allowed[j]
                        new = cur & ~bit
                        if new == 0:
                            ok = False
                            break
                        if new != cur:
                            changes.append((j, cur))
                            allowed[j] = new
                if ok:
                    dfs(i + 1)
                # revert
                for j, val in changes:
                    allowed[j] = val
                assign[i] = 0
                if found:
                    return

    dfs(1)
    out = []
    if found:
        out.append("YES")
        out.append(' '.join(str(assign[i]) for i in range(1, n + 1)))
    else:
        out.append("NO")
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()